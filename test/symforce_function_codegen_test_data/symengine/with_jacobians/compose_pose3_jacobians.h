// -----------------------------------------------------------------------------
// This file was autogenerated by symforce from template:
//     cpp_templates/function/FUNCTION.h.jinja
// Do NOT modify by hand.
// -----------------------------------------------------------------------------

#pragma once

#include <Eigen/Dense>

#include <sym/pose3.h>

namespace sym {

/**
 * Composition of two elements in the group.
 *
 * Returns:
 *     res_D_a: (6x6) jacobian of res (6) wrt arg a (6)
 *     res_D_b: (6x6) jacobian of res (6) wrt arg b (6)
 */
template <typename Scalar>
void ComposePose3Jacobians(const sym::Pose3<Scalar>& a, const sym::Pose3<Scalar>& b,
                           Eigen::Matrix<Scalar, 6, 6>* const res_D_a = nullptr,
                           Eigen::Matrix<Scalar, 6, 6>* const res_D_b = nullptr) {
  // Total ops: 322

  // Input arrays
  const Eigen::Matrix<Scalar, 7, 1>& _a = a.Data();
  const Eigen::Matrix<Scalar, 7, 1>& _b = b.Data();

  // Intermediate terms (125)
  const Scalar _tmp0 = _a[0] * _b[1];
  const Scalar _tmp1 = (Scalar(1) / Scalar(2)) * _tmp0;
  const Scalar _tmp2 = -_tmp1;
  const Scalar _tmp3 = _a[2] * _b[3];
  const Scalar _tmp4 = (Scalar(1) / Scalar(2)) * _tmp3;
  const Scalar _tmp5 = _a[3] * _b[2];
  const Scalar _tmp6 = (Scalar(1) / Scalar(2)) * _tmp5;
  const Scalar _tmp7 = -_tmp6;
  const Scalar _tmp8 = _a[1] * _b[0];
  const Scalar _tmp9 = (Scalar(1) / Scalar(2)) * _tmp8;
  const Scalar _tmp10 = -_tmp9;
  const Scalar _tmp11 = _tmp10 + _tmp7;
  const Scalar _tmp12 = _tmp11 + _tmp2 + _tmp4;
  const Scalar _tmp13 = 2 * _tmp0 + 2 * _tmp3 + 2 * _tmp5 - 2 * _tmp8;
  const Scalar _tmp14 = _a[1] * _b[3];
  const Scalar _tmp15 = (Scalar(1) / Scalar(2)) * _tmp14;
  const Scalar _tmp16 = -_tmp15;
  const Scalar _tmp17 = _a[3] * _b[1];
  const Scalar _tmp18 = (Scalar(1) / Scalar(2)) * _tmp17;
  const Scalar _tmp19 = _a[0] * _b[2];
  const Scalar _tmp20 = (Scalar(1) / Scalar(2)) * _tmp19;
  const Scalar _tmp21 = -_tmp20;
  const Scalar _tmp22 = _a[2] * _b[0];
  const Scalar _tmp23 = (Scalar(1) / Scalar(2)) * _tmp22;
  const Scalar _tmp24 = -_tmp23;
  const Scalar _tmp25 = _tmp21 + _tmp24;
  const Scalar _tmp26 = _tmp16 + _tmp18 + _tmp25;
  const Scalar _tmp27 = 2 * _tmp14 + 2 * _tmp17 - 2 * _tmp19 + 2 * _tmp22;
  const Scalar _tmp28 = _a[0] * _b[3];
  const Scalar _tmp29 = (Scalar(1) / Scalar(2)) * _tmp28;
  const Scalar _tmp30 = -_tmp29;
  const Scalar _tmp31 = _a[3] * _b[0];
  const Scalar _tmp32 = (Scalar(1) / Scalar(2)) * _tmp31;
  const Scalar _tmp33 = -_tmp32;
  const Scalar _tmp34 = _tmp30 + _tmp33;
  const Scalar _tmp35 = _a[2] * _b[1];
  const Scalar _tmp36 = (Scalar(1) / Scalar(2)) * _tmp35;
  const Scalar _tmp37 = -_tmp36;
  const Scalar _tmp38 = _a[1] * _b[2];
  const Scalar _tmp39 = (Scalar(1) / Scalar(2)) * _tmp38;
  const Scalar _tmp40 = _tmp37 + _tmp39;
  const Scalar _tmp41 = _tmp34 + _tmp40;
  const Scalar _tmp42 = 2 * _tmp28 + 2 * _tmp31 - 2 * _tmp35 + 2 * _tmp38;
  const Scalar _tmp43 = _a[2] * _b[2];
  const Scalar _tmp44 = (Scalar(1) / Scalar(2)) * _tmp43;
  const Scalar _tmp45 = _a[0] * _b[0];
  const Scalar _tmp46 = (Scalar(1) / Scalar(2)) * _tmp45;
  const Scalar _tmp47 = -_tmp46;
  const Scalar _tmp48 = _a[3] * _b[3];
  const Scalar _tmp49 = (Scalar(1) / Scalar(2)) * _tmp48;
  const Scalar _tmp50 = _a[1] * _b[1];
  const Scalar _tmp51 = (Scalar(1) / Scalar(2)) * _tmp50;
  const Scalar _tmp52 = _tmp49 + _tmp51;
  const Scalar _tmp53 = _tmp44 + _tmp47 + _tmp52;
  const Scalar _tmp54 = -2 * _tmp43 - 2 * _tmp45 + 2 * _tmp48 - 2 * _tmp50;
  const Scalar _tmp55 = 2 * _a[0];
  const Scalar _tmp56 = _a[2] * _tmp55;
  const Scalar _tmp57 = 2 * _a[3];
  const Scalar _tmp58 = _a[1] * _tmp57;
  const Scalar _tmp59 = _tmp56 + _tmp58;
  const Scalar _tmp60 = _a[1] * _tmp55;
  const Scalar _tmp61 = -_tmp60;
  const Scalar _tmp62 = _a[2] * _tmp57;
  const Scalar _tmp63 = std::pow(_a[0], Scalar(2));
  const Scalar _tmp64 = std::pow(_a[1], Scalar(2));
  const Scalar _tmp65 = -_tmp64;
  const Scalar _tmp66 = _tmp63 + _tmp65;
  const Scalar _tmp67 = std::pow(_a[2], Scalar(2));
  const Scalar _tmp68 = std::pow(_a[3], Scalar(2));
  const Scalar _tmp69 = -_tmp68;
  const Scalar _tmp70 = _tmp67 + _tmp69;
  const Scalar _tmp71 = 2 * _a[1] * _a[2];
  const Scalar _tmp72 = _a[0] * _tmp57;
  const Scalar _tmp73 = -_tmp72;
  const Scalar _tmp74 = _tmp71 + _tmp73;
  const Scalar _tmp75 = -_tmp63;
  const Scalar _tmp76 = -_tmp71;
  const Scalar _tmp77 = _tmp49 - _tmp51;
  const Scalar _tmp78 = _tmp44 + _tmp46 + _tmp77;
  const Scalar _tmp79 = -_tmp39;
  const Scalar _tmp80 = _tmp37 + _tmp79;
  const Scalar _tmp81 = _tmp29 + _tmp33 + _tmp80;
  const Scalar _tmp82 = -_tmp18;
  const Scalar _tmp83 = _tmp16 + _tmp82;
  const Scalar _tmp84 = _tmp21 + _tmp23;
  const Scalar _tmp85 = _tmp83 + _tmp84;
  const Scalar _tmp86 = -_tmp4;
  const Scalar _tmp87 = _tmp2 + _tmp86;
  const Scalar _tmp88 = _tmp10 + _tmp6;
  const Scalar _tmp89 = _tmp87 + _tmp88;
  const Scalar _tmp90 = -_tmp67;
  const Scalar _tmp91 = _tmp68 + _tmp90;
  const Scalar _tmp92 = -_tmp56;
  const Scalar _tmp93 = -_tmp58;
  const Scalar _tmp94 = _tmp60 + _tmp62;
  const Scalar _tmp95 = _tmp56 + _tmp93;
  const Scalar _tmp96 = _tmp30 + _tmp32 + _tmp80;
  const Scalar _tmp97 = -_tmp44;
  const Scalar _tmp98 = _tmp46 + _tmp52 + _tmp97;
  const Scalar _tmp99 = _tmp1 + _tmp11 + _tmp86;
  const Scalar _tmp100 = _tmp15 + _tmp25 + _tmp82;
  const Scalar _tmp101 = _tmp64 + _tmp75;
  const Scalar _tmp102 = -_tmp62;
  const Scalar _tmp103 = _tmp102 + _tmp60;
  const Scalar _tmp104 = _tmp71 + _tmp72;
  const Scalar _tmp105 = _tmp1 + _tmp4 + _tmp88;
  const Scalar _tmp106 = _tmp34 + _tmp36 + _tmp79;
  const Scalar _tmp107 = -_tmp106 * _tmp42;
  const Scalar _tmp108 = _tmp20 + _tmp24 + _tmp83;
  const Scalar _tmp109 = _tmp47 + _tmp77 + _tmp97;
  const Scalar _tmp110 = _tmp109 * _tmp54;
  const Scalar _tmp111 = -_tmp108 * _tmp27 + _tmp110;
  const Scalar _tmp112 = _tmp109 * _tmp13;
  const Scalar _tmp113 = _tmp108 * _tmp42;
  const Scalar _tmp114 = _tmp106 * _tmp13;
  const Scalar _tmp115 = _tmp109 * _tmp27;
  const Scalar _tmp116 = _tmp29 + _tmp32 + _tmp40;
  const Scalar _tmp117 = _tmp7 + _tmp87 + _tmp9;
  const Scalar _tmp118 = -_tmp117 * _tmp13;
  const Scalar _tmp119 = _tmp117 * _tmp27;
  const Scalar _tmp120 = _tmp109 * _tmp42;
  const Scalar _tmp121 = _tmp15 + _tmp18 + _tmp84;
  const Scalar _tmp122 = -2 * _tmp67;
  const Scalar _tmp123 = -2 * _tmp64;
  const Scalar _tmp124 = 1 - 2 * _tmp63;

  // Output terms (2)
  if (res_D_a != nullptr) {
    Eigen::Matrix<Scalar, 6, 6>& _res_D_a = (*res_D_a);

    _res_D_a(0, 0) = _tmp12 * _tmp13 - _tmp26 * _tmp27 - _tmp41 * _tmp42 + _tmp53 * _tmp54;
    _res_D_a(1, 0) = _tmp12 * _tmp54 - _tmp13 * _tmp53 + _tmp26 * _tmp42 - _tmp27 * _tmp41;
    _res_D_a(2, 0) = -_tmp12 * _tmp42 - _tmp13 * _tmp41 + _tmp26 * _tmp54 + _tmp27 * _tmp53;
    _res_D_a(3, 0) = _b[5] * _tmp59 + _b[6] * (_tmp61 + _tmp62);
    _res_D_a(4, 0) = _b[5] * _tmp74 + _b[6] * (_tmp66 + _tmp70);
    _res_D_a(5, 0) = _b[5] * (_tmp65 + _tmp67 + _tmp68 + _tmp75) + _b[6] * (_tmp73 + _tmp76);
    _res_D_a(0, 1) = _tmp13 * _tmp78 - _tmp27 * _tmp81 - _tmp42 * _tmp85 + _tmp54 * _tmp89;
    _res_D_a(1, 1) = -_tmp13 * _tmp89 - _tmp27 * _tmp85 + _tmp42 * _tmp81 + _tmp54 * _tmp78;
    _res_D_a(2, 1) = -_tmp13 * _tmp85 + _tmp27 * _tmp89 - _tmp42 * _tmp78 + _tmp54 * _tmp81;
    _res_D_a(3, 1) = _b[4] * (_tmp92 + _tmp93) + _b[6] * (_tmp66 + _tmp91);
    _res_D_a(4, 1) = _b[4] * (_tmp72 + _tmp76) + _b[6] * _tmp94;
    _res_D_a(5, 1) = _b[4] * (_tmp63 + _tmp64 + _tmp69 + _tmp90) + _b[6] * _tmp95;
    _res_D_a(0, 2) = _tmp100 * _tmp54 + _tmp13 * _tmp96 - _tmp27 * _tmp98 - _tmp42 * _tmp99;
    _res_D_a(1, 2) = -_tmp100 * _tmp13 - _tmp27 * _tmp99 + _tmp42 * _tmp98 + _tmp54 * _tmp96;
    _res_D_a(2, 2) = _tmp100 * _tmp27 - _tmp13 * _tmp99 - _tmp42 * _tmp96 + _tmp54 * _tmp98;
    _res_D_a(3, 2) = _b[4] * _tmp103 + _b[5] * (_tmp101 + _tmp70);
    _res_D_a(4, 2) = _b[4] * (_tmp101 + _tmp91) + _b[5] * (_tmp102 + _tmp61);
    _res_D_a(5, 2) = _b[4] * _tmp104 + _b[5] * (_tmp58 + _tmp92);
    _res_D_a(0, 3) = 0;
    _res_D_a(1, 3) = 0;
    _res_D_a(2, 3) = 0;
    _res_D_a(3, 3) = 1;
    _res_D_a(4, 3) = 0;
    _res_D_a(5, 3) = 0;
    _res_D_a(0, 4) = 0;
    _res_D_a(1, 4) = 0;
    _res_D_a(2, 4) = 0;
    _res_D_a(3, 4) = 0;
    _res_D_a(4, 4) = 1;
    _res_D_a(5, 4) = 0;
    _res_D_a(0, 5) = 0;
    _res_D_a(1, 5) = 0;
    _res_D_a(2, 5) = 0;
    _res_D_a(3, 5) = 0;
    _res_D_a(4, 5) = 0;
    _res_D_a(5, 5) = 1;
  }

  if (res_D_b != nullptr) {
    Eigen::Matrix<Scalar, 6, 6>& _res_D_b = (*res_D_b);

    _res_D_b(0, 0) = _tmp105 * _tmp13 + _tmp107 + _tmp111;
    _res_D_b(1, 0) = _tmp105 * _tmp54 - _tmp106 * _tmp27 - _tmp112 + _tmp113;
    _res_D_b(2, 0) = -_tmp105 * _tmp42 + _tmp108 * _tmp54 - _tmp114 + _tmp115;
    _res_D_b(3, 0) = 0;
    _res_D_b(4, 0) = 0;
    _res_D_b(5, 0) = 0;
    _res_D_b(0, 1) = _tmp112 - _tmp113 - _tmp116 * _tmp27 + _tmp117 * _tmp54;
    _res_D_b(1, 1) = _tmp111 + _tmp116 * _tmp42 + _tmp118;
    _res_D_b(2, 1) = -_tmp108 * _tmp13 + _tmp116 * _tmp54 + _tmp119 - _tmp120;
    _res_D_b(3, 1) = 0;
    _res_D_b(4, 1) = 0;
    _res_D_b(5, 1) = 0;
    _res_D_b(0, 2) = _tmp114 - _tmp115 - _tmp117 * _tmp42 + _tmp121 * _tmp54;
    _res_D_b(1, 2) = _tmp106 * _tmp54 - _tmp119 + _tmp120 - _tmp121 * _tmp13;
    _res_D_b(2, 2) = _tmp107 + _tmp110 + _tmp118 + _tmp121 * _tmp27;
    _res_D_b(3, 2) = 0;
    _res_D_b(4, 2) = 0;
    _res_D_b(5, 2) = 0;
    _res_D_b(0, 3) = 0;
    _res_D_b(1, 3) = 0;
    _res_D_b(2, 3) = 0;
    _res_D_b(3, 3) = _tmp122 + _tmp123 + 1;
    _res_D_b(4, 3) = _tmp94;
    _res_D_b(5, 3) = _tmp95;
    _res_D_b(0, 4) = 0;
    _res_D_b(1, 4) = 0;
    _res_D_b(2, 4) = 0;
    _res_D_b(3, 4) = _tmp103;
    _res_D_b(4, 4) = _tmp122 + _tmp124;
    _res_D_b(5, 4) = _tmp104;
    _res_D_b(0, 5) = 0;
    _res_D_b(1, 5) = 0;
    _res_D_b(2, 5) = 0;
    _res_D_b(3, 5) = _tmp59;
    _res_D_b(4, 5) = _tmp74;
    _res_D_b(5, 5) = _tmp123 + _tmp124;
  }
}  // NOLINT(readability/fn_size)

// NOLINTNEXTLINE(readability/fn_size)
}  // namespace sym
