/* ----------------------------------------------------------------------------
 * SymForce - Copyright 2022, Skydio, Inc.
 * This source code is under the Apache 2.0 license found in the LICENSE file.
 * ---------------------------------------------------------------------------- */

#pragma once

#include <unordered_set>

#include <Eigen/Sparse>

#include <lcmtypes/sym/linearization_dense_factor_helper_t.hpp>
#include <lcmtypes/sym/linearization_sparse_factor_helper_t.hpp>

#include "./factor.h"
#include "./internal/linearized_dense_factor_pool.h"
#include "./linearization.h"
#include "./values.h"

namespace sym {

/**
 * Class for evaluating multiple Factors at the linearization point given by a Values.
 *
 * Stores the original Factors as well as the LinearizedFactors, and provides tools for
 * aggregating keys and building a large jacobian / hessian for optimization.
 *
 * For efficiency, prefer calling Relinearize instead of re-constructing this object!
 */
template <typename ScalarType>
class Linearizer {
 public:
  using Scalar = ScalarType;
  using LinearizedDenseFactor = typename Factor<Scalar>::LinearizedDenseFactor;
  using LinearizedSparseFactor = typename Factor<Scalar>::LinearizedSparseFactor;

  /**
   * Construct a Linearizer from factors and optional keys
   *
   * Args:
   *     factors: Only stores a pointer, MUST be in scope for the lifetime of this object!
   *     key_order: If provided, acts as an ordered set of keys that form the state vector
   *                to optimize. Can equal the set of all factor keys or a subset of all
   *                factor keys. If not provided, it is computed from all keys for all
   *                factors using a default ordering.
   */
  Linearizer(const std::string& name, const std::vector<Factor<Scalar>>& factors,
             const std::vector<Key>& key_order = {}, bool include_jacobians = false);

  /**
   * Update linearization at a new evaluation point. Returns the total residual dimension M.
   * This is more efficient than reconstructing this object repeatedly.  On the first call, it will
   * allocate memory and perform analysis needed for efficient repeated relinearization.
   *
   * TODO(aaron): This should be const except that it can initialize the object
   */
  void Relinearize(const Values<Scalar>& values, Linearization<Scalar>& linearization);

  /**
   * Check whether the keys in `keys` correspond 1-1 (and in the same order) with the start of the
   * key ordering in the problem linearization
   *
   * If block_dim is provided, it will be filled out with the (tangent) dimension of the problem
   * hessian and rhs which is occupied by the given keys
   *
   * TODO(aaron): Maybe kill this once we have general marginalization
   */
  bool CheckKeysAreContiguousAtStart(const std::vector<Key>& keys,
                                     size_t* block_dim = nullptr) const;

  /**
   * Extract covariances for optimized variables individually from the full problem covariance.  For
   * each variable in `keys`, the returned matrix is the corresponding block from the diagonal of
   * the full covariance matrix.  Requires that the Linearizer has already been initialized
   */
  template <typename MatrixType>
  void SplitCovariancesByKey(const MatrixType& covariance_block, const std::vector<Key>& keys,
                             std::unordered_map<Key, MatrixX<Scalar>>& covariances_by_key) const;

  /**
   * Whether this contains values, versus having not been evaluated yet
   */
  bool IsInitialized() const;

  /**
   * Basic accessors.
   */
  const std::vector<LinearizedSparseFactor>& LinearizedSparseFactors() const;

  const std::vector<Key>& Keys() const;

  const std::unordered_map<key_t, index_entry_t>& StateIndex() const;

 private:
  /**
   * Allocate all factor storage and compute sparsity pattern. This does a lot of index
   * computation on the first linearization, such that repeated linearization can be fast.
   */
  void BuildInitialLinearization(const Values<Scalar>& values);

  /**
   * Update the sparse combined problem linearization from a single factor.
   */
  void UpdateFromLinearizedDenseFactorIntoSparse(
      const LinearizedDenseFactor& linearized_factor,
      const linearization_dense_factor_helper_t& factor_helper,
      Linearization<Scalar>& linearization) const;
  void UpdateFromLinearizedSparseFactorIntoSparse(
      const LinearizedSparseFactor& linearized_factor,
      const linearization_sparse_factor_helper_t& factor_helper,
      Linearization<Scalar>& linearization) const;

  /**
   * Update the combined residual and rhs, along with triplet lists for the sparse matrices, from a
   * single factor
   */
  void UpdateFromDenseFactorIntoTripletLists(
      const LinearizedDenseFactor& linearized_factor,
      const linearization_dense_factor_helper_t& factor_helper,
      std::vector<Eigen::Triplet<Scalar>>* const jacobian_triplets,
      std::vector<Eigen::Triplet<Scalar>>* const hessian_lower_triplets) const;
  void UpdateFromSparseFactorIntoTripletLists(
      const LinearizedSparseFactor& linearized_factor,
      const linearization_sparse_factor_helper_t& factor_helper,
      std::vector<Eigen::Triplet<Scalar>>* const jacobian_triplets,
      std::vector<Eigen::Triplet<Scalar>>* const hessian_lower_triplets) const;

  /**
   * Check if a Linearization has the correct sizes, and if not, initialize it
   */
  void EnsureLinearizationHasCorrectSize(Linearization<Scalar>& linearization) const;

  bool initialized_{false};

  // The name of this linearizer to be used for printing debug information.
  std::string name_;

  // Pointer to the nonlinear factors
  const std::vector<Factor<Scalar>>* factors_;

  // The index for each factor in the values.  Cached the first time we linearize, to avoid repeated
  // unordered_map lookups
  std::vector<std::vector<index_entry_t>> factor_indices_;

  bool include_jacobians_;

  // Linearized factors - stores individual factor residuals, jacobians, etc
  internal::LinearizedDenseFactorPool<Scalar> linearized_dense_factors_;  // one per Jacobian shape
  std::vector<LinearizedSparseFactor> linearized_sparse_factors_;         // one per sparse factor

  // Keys that form the state vector
  std::vector<Key> keys_;

  // Index of the keys in the state vector
  std::unordered_map<key_t, index_entry_t> state_index_;

  // Helpers for updating the combined problem from linearized factors
  std::vector<linearization_dense_factor_helper_t> dense_factor_update_helpers_;
  std::vector<linearization_sparse_factor_helper_t> sparse_factor_update_helpers_;

  // Numerical linearization from the very first linearization that is used to initialize new
  // LevenbergMarquardtState::StateBlocks (at most 3 times) and isn't touched on each subsequent
  // relinearization.
  Linearization<Scalar> init_linearization_;
};

// Free function as an alternate way to call.
template <typename Scalar>
Linearization<Scalar> Linearize(const std::vector<Factor<Scalar>>& factors,
                                const Values<Scalar>& values,
                                const std::vector<Key>& keys_to_optimize = {},
                                const std::string& linearizer_name = "Linearizer") {
  Linearization<Scalar> linearization;
  Linearizer<Scalar>(linearizer_name, factors, keys_to_optimize).Relinearize(values, linearization);
  return linearization;
}

/**
 * Compute the combined set of keys to optimize from the given factors. Order using the given
 * comparison function.
 */
template <typename Scalar, typename Compare>
std::vector<Key> ComputeKeysToOptimize(const std::vector<Factor<Scalar>>& factors,
                                       Compare key_compare) {
  // Some thoughts on efficiency at
  // https://stackoverflow.com/questions/1041620/whats-the-most-efficient-way-to-erase-duplicates-and-sort-a-vector

  // Aggregate uniques
  std::unordered_set<Key> key_set;
  for (const Factor<Scalar>& factor : factors) {
    key_set.insert(factor.OptimizedKeys().begin(), factor.OptimizedKeys().end());
  }

  // Copy to vector
  std::vector<Key> keys;
  keys.insert(keys.end(), key_set.begin(), key_set.end());

  // Order
  std::sort(keys.begin(), keys.end(), key_compare);

  return keys;
}

// If no comparator is specified, use sym::Key::LexicalLessThan.
template <typename Scalar>
std::vector<Key> ComputeKeysToOptimize(const std::vector<Factor<Scalar>>& factors) {
  return ComputeKeysToOptimize(factors, &sym::Key::LexicalLessThan);
}

}  // namespace sym

#include "./linearizer.tcc"

// Explicit instantiation declaration
extern template class sym::Linearizer<double>;
extern template class sym::Linearizer<float>;
