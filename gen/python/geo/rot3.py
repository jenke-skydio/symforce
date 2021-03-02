# -----------------------------------------------------------------------------
# This file was autogenerated by symforce. Do NOT modify by hand.
# -----------------------------------------------------------------------------
import numpy as np
import typing as T

from .ops import rot3 as ops


class Rot3(object):
    """"
    Autogenerated Python implementation of <class 'symforce.geo.rot3.Rot3'>.

    Group of three-dimensional orthogonal matrices with determinant +1, representing
    rotations in 3D space. Backed by a quaternion with (x, y, z, w) storage.
    """

    __slots__ = ["data"]

    def __repr__(self):
        # type: () -> str
        return "<{} {}>".format(self.__class__.__name__, self.data)

    # --------------------------------------------------------------------------
    # StorageOps concept
    # --------------------------------------------------------------------------

    @staticmethod
    def storage_dim():
        # type: () -> int
        return 4

    def to_storage(self):
        # type: () -> T.List[float]
        return list(self.data)

    @classmethod
    def from_storage(cls, vec):
        # type: (T.Sequence[float]) -> Rot3
        instance = cls()

        if isinstance(vec, list):
            instance.data = vec
        else:
            instance.data = list(vec)

        assert len(vec) == cls.storage_dim(), "{} has storage dim {}, got {}.".format(
            cls.__name__, cls.storage_dim(), len(vec)
        )

        return instance

    # --------------------------------------------------------------------------
    # GroupOps concept
    # --------------------------------------------------------------------------

    @classmethod
    def identity(cls):
        # type: () -> Rot3
        return cls.from_storage(ops.GroupOps.identity())

    def inverse(self):
        # type: () -> Rot3
        return self.__class__.from_storage(ops.GroupOps.inverse(self))

    def compose(self, b):
        # type: (Rot3) -> Rot3
        return self.__class__.from_storage(ops.GroupOps.compose(self, b))

    def between(self, b):
        # type: (Rot3) -> Rot3
        return self.__class__.from_storage(ops.GroupOps.between(self, b))

    # --------------------------------------------------------------------------
    # LieGroupOps concept
    # --------------------------------------------------------------------------

    @staticmethod
    def tangent_dim():
        # type: () -> int
        return 3

    @classmethod
    def from_tangent(cls, vec, epsilon=1e-8):
        # type: (T.Sequence[float], float) -> Rot3
        assert len(vec) == cls.tangent_dim(), "{}, {}".format(len(vec), cls.tangent_dim())
        return cls.from_storage(ops.LieGroupOps.from_tangent(vec, epsilon))

    def to_tangent(self, epsilon=1e-8):
        # type: (float) -> T.List[float]
        return ops.LieGroupOps.to_tangent(self, epsilon)

    def retract(self, vec, epsilon=1e-8):
        # type: (T.Sequence[float], float) -> Rot3
        assert len(vec) == self.tangent_dim(), "{}, {}".format(len(vec), self.tangent_dim())
        return self.__class__.from_storage(ops.LieGroupOps.retract(self, vec, epsilon))

    def local_coordinates(self, b, epsilon=1e-8):
        # type: (Rot3, float) -> T.List[float]
        return ops.LieGroupOps.local_coordinates(self, b, epsilon)

    # --------------------------------------------------------------------------
    # General Helpers
    # --------------------------------------------------------------------------
    def __eq__(self, other):
        # type: (T.Any) -> bool
        if isinstance(other, Rot3):
            return self.data == other.data
        else:
            raise NotImplementedError("Cannot compare {} to {}".format(type(self), type(other)))

    def __mul__(self, other):
        # type: (Rot3) -> Rot3
        if isinstance(other, Rot3):
            return self.compose(other)
        elif isinstance(other, np.ndarray) and hasattr(self, "_apply_to_vector"):
            return self._apply_to_vector(other)
        else:
            raise NotImplementedError("Cannot compose {} with {}.".format(type(self), type(other)))

    # Included from "custom_methods/rot3.py.jinja":
    # --------------------------------------------------------------------------
    # Handwritten methods for Rot3
    # These will get included into the autogenerated class header.
    # --------------------------------------------------------------------------

    def __init__(self, q=None):
        # type: (T.Sequence[float]) -> None
        if q is None:
            self.data = ops.GroupOps.identity()
        else:
            assert len(q) == self.storage_dim()
            self.data = list(q)

    def to_rotation_matrix(self):
        # type: () -> np.ndarray
        x, y, z, w = self.data

        return np.array(
            [
                [1 - 2 * y ** 2 - 2 * z ** 2, 2 * x * y - 2 * z * w, 2 * x * z + 2 * y * w,],
                [2 * x * y + 2 * z * w, 1 - 2 * x ** 2 - 2 * z ** 2, 2 * y * z - 2 * x * w,],
                [2 * x * z - 2 * y * w, 2 * y * z + 2 * x * w, 1 - 2 * x ** 2 - 2 * y ** 2,],
            ]
        )

    def _apply_to_vector(self, v):
        # type: (np.ndarray) -> np.ndarray
        v_reshaped = np.reshape(v, (3, 1))
        return np.reshape(np.matmul(self.to_rotation_matrix(), v_reshaped), v.shape)

    @classmethod
    def from_rotation_matrix(cls, R, epsilon=0.0):
        # type: (np.ndarray, float) -> Rot3
        assert R.shape == (3, 3)
        w = np.sqrt(max(epsilon ** 2, 1 + R[0, 0] + R[1, 1] + R[2, 2])) / 2
        x = np.sqrt(max(epsilon ** 2, 1 + R[0, 0] - R[1, 1] - R[2, 2])) / 2
        y = np.sqrt(max(epsilon ** 2, 1 - R[0, 0] + R[1, 1] - R[2, 2])) / 2
        z = np.sqrt(max(epsilon ** 2, 1 - R[0, 0] - R[1, 1] + R[2, 2])) / 2

        x = abs(x)
        if (R[2, 1] - R[1, 2]) < 0:
            x = -x

        y = abs(y)
        if (R[0, 2] - R[2, 0]) < 0:
            y = -y

        z = abs(z)
        if (R[1, 0] - R[0, 1]) < 0:
            z = -z

        return Rot3.from_storage([x, y, z, w])

    @classmethod
    def from_euler_ypr(cls, yaw, pitch, roll):
        # type: (float, float, float) -> Rot3

        return (
            Rot3.from_tangent([0, 0, yaw])
            * Rot3.from_tangent([0, pitch, 0])
            * Rot3.from_tangent([roll, 0, 0])
        )

    def to_euler_ypr(self):
        # type: () -> T.Tuple[float, float, float]
        x, y, z, w = self.data
        yaw = np.arctan2(2 * x * y + 2 * w * z, x * x + w * w - z * z - y * y)
        pitch = -np.arcsin(2 * x * z - 2 * w * y)
        roll = np.arctan2(2 * y * z + 2 * w * x, z * z - y * y - x * x + w * w)
        return yaw, pitch, roll

    # TODO more rotation helpers
