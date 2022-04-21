# -----------------------------------------------------------------------------
# This file was autogenerated by symforce from template:
#     python_templates/ops/CLASS/group_ops.py.jinja
# Do NOT modify by hand.
# -----------------------------------------------------------------------------

import math
import numpy
import typing as T

import sym  # pylint: disable=unused-import


class GroupOps(object):
    """
    Python GroupOps implementation for <class 'symforce.geo.rot3.Rot3'>.
    """

    @staticmethod
    def identity():
        # type: () -> sym.Rot3

        # Total ops: 0

        # Input arrays

        # Intermediate terms (0)

        # Output terms
        _res = [0.0] * 4
        _res[0] = 0
        _res[1] = 0
        _res[2] = 0
        _res[3] = 1
        return sym.Rot3.from_storage(_res)

    @staticmethod
    def inverse(a):
        # type: (sym.Rot3) -> sym.Rot3

        # Total ops: 3

        # Input arrays
        _a = a.data

        # Intermediate terms (0)

        # Output terms
        _res = [0.0] * 4
        _res[0] = -_a[0]
        _res[1] = -_a[1]
        _res[2] = -_a[2]
        _res[3] = _a[3]
        return sym.Rot3.from_storage(_res)

    @staticmethod
    def compose(a, b):
        # type: (sym.Rot3, sym.Rot3) -> sym.Rot3

        # Total ops: 28

        # Input arrays
        _a = a.data
        _b = b.data

        # Intermediate terms (0)

        # Output terms
        _res = [0.0] * 4
        _res[0] = _a[0] * _b[3] + _a[1] * _b[2] - _a[2] * _b[1] + _a[3] * _b[0]
        _res[1] = -_a[0] * _b[2] + _a[1] * _b[3] + _a[2] * _b[0] + _a[3] * _b[1]
        _res[2] = _a[0] * _b[1] - _a[1] * _b[0] + _a[2] * _b[3] + _a[3] * _b[2]
        _res[3] = -_a[0] * _b[0] - _a[1] * _b[1] - _a[2] * _b[2] + _a[3] * _b[3]
        return sym.Rot3.from_storage(_res)

    @staticmethod
    def between(a, b):
        # type: (sym.Rot3, sym.Rot3) -> sym.Rot3

        # Total ops: 28

        # Input arrays
        _a = a.data
        _b = b.data

        # Intermediate terms (0)

        # Output terms
        _res = [0.0] * 4
        _res[0] = -_a[0] * _b[3] - _a[1] * _b[2] + _a[2] * _b[1] + _a[3] * _b[0]
        _res[1] = _a[0] * _b[2] - _a[1] * _b[3] - _a[2] * _b[0] + _a[3] * _b[1]
        _res[2] = -_a[0] * _b[1] + _a[1] * _b[0] - _a[2] * _b[3] + _a[3] * _b[2]
        _res[3] = _a[0] * _b[0] + _a[1] * _b[1] + _a[2] * _b[2] + _a[3] * _b[3]
        return sym.Rot3.from_storage(_res)

    @staticmethod
    def inverse_with_jacobian(a):
        # type: (sym.Rot3) -> T.Tuple[sym.Rot3, numpy.ndarray]

        # Total ops: 34

        # Input arrays
        _a = a.data

        # Intermediate terms (13)
        _tmp0 = _a[2] ** 2
        _tmp1 = _a[0] ** 2
        _tmp2 = -_a[3] ** 2
        _tmp3 = _a[1] ** 2
        _tmp4 = _tmp2 + _tmp3
        _tmp5 = 2 * _a[2]
        _tmp6 = _a[3] * _tmp5
        _tmp7 = -2 * _a[0] * _a[1]
        _tmp8 = 2 * _a[3]
        _tmp9 = _a[1] * _tmp8
        _tmp10 = -_a[0] * _tmp5
        _tmp11 = _a[0] * _tmp8
        _tmp12 = -_a[1] * _tmp5

        # Output terms
        _res = [0.0] * 4
        _res[0] = -_a[0]
        _res[1] = -_a[1]
        _res[2] = -_a[2]
        _res[3] = _a[3]
        _res_D_a = numpy.zeros((3, 3))
        _res_D_a[0, 0] = _tmp0 - _tmp1 + _tmp4
        _res_D_a[1, 0] = -_tmp6 + _tmp7
        _res_D_a[2, 0] = _tmp10 + _tmp9
        _res_D_a[0, 1] = _tmp6 + _tmp7
        _res_D_a[1, 1] = _tmp0 + _tmp1 + _tmp2 - _tmp3
        _res_D_a[2, 1] = -_tmp11 + _tmp12
        _res_D_a[0, 2] = _tmp10 - _tmp9
        _res_D_a[1, 2] = _tmp11 + _tmp12
        _res_D_a[2, 2] = -_tmp0 + _tmp1 + _tmp4
        return sym.Rot3.from_storage(_res), _res_D_a

    @staticmethod
    def compose_with_jacobians(a, b):
        # type: (sym.Rot3, sym.Rot3) -> T.Tuple[sym.Rot3, numpy.ndarray, numpy.ndarray]

        # Total ops: 224

        # Input arrays
        _a = a.data
        _b = b.data

        # Intermediate terms (94)
        _tmp0 = _a[3] * _b[0]
        _tmp1 = _a[2] * _b[1]
        _tmp2 = _a[0] * _b[3]
        _tmp3 = _a[1] * _b[2]
        _tmp4 = _tmp0 - _tmp1 + _tmp2 + _tmp3
        _tmp5 = _a[3] * _b[1]
        _tmp6 = _a[2] * _b[0]
        _tmp7 = _a[0] * _b[2]
        _tmp8 = _a[1] * _b[3]
        _tmp9 = _tmp5 + _tmp6 - _tmp7 + _tmp8
        _tmp10 = _a[3] * _b[2]
        _tmp11 = _a[2] * _b[3]
        _tmp12 = _a[0] * _b[1]
        _tmp13 = _a[1] * _b[0]
        _tmp14 = _tmp10 + _tmp11 + _tmp12 - _tmp13
        _tmp15 = _a[3] * _b[3]
        _tmp16 = _a[2] * _b[2]
        _tmp17 = _a[0] * _b[0]
        _tmp18 = _a[1] * _b[1]
        _tmp19 = _tmp15 - _tmp16 - _tmp17 - _tmp18
        _tmp20 = (1.0 / 2.0) * _tmp13
        _tmp21 = -_tmp20
        _tmp22 = (1.0 / 2.0) * _tmp11
        _tmp23 = _tmp21 + _tmp22
        _tmp24 = (1.0 / 2.0) * _tmp10
        _tmp25 = -_tmp24
        _tmp26 = (1.0 / 2.0) * _tmp12
        _tmp27 = -_tmp26
        _tmp28 = _tmp25 + _tmp27
        _tmp29 = _tmp23 + _tmp28
        _tmp30 = 2 * _tmp14
        _tmp31 = (1.0 / 2.0) * _tmp3
        _tmp32 = (1.0 / 2.0) * _tmp0
        _tmp33 = -_tmp32
        _tmp34 = (1.0 / 2.0) * _tmp1
        _tmp35 = -_tmp34
        _tmp36 = (1.0 / 2.0) * _tmp2
        _tmp37 = -_tmp36
        _tmp38 = _tmp35 + _tmp37
        _tmp39 = _tmp31 + _tmp33 + _tmp38
        _tmp40 = 2 * _tmp4
        _tmp41 = (1.0 / 2.0) * _tmp5
        _tmp42 = (1.0 / 2.0) * _tmp6
        _tmp43 = -_tmp42
        _tmp44 = (1.0 / 2.0) * _tmp7
        _tmp45 = -_tmp44
        _tmp46 = (1.0 / 2.0) * _tmp8
        _tmp47 = -_tmp46
        _tmp48 = _tmp45 + _tmp47
        _tmp49 = _tmp41 + _tmp43 + _tmp48
        _tmp50 = 2 * _tmp9
        _tmp51 = (1.0 / 2.0) * _tmp17
        _tmp52 = -_tmp51
        _tmp53 = (1.0 / 2.0) * _tmp16
        _tmp54 = (1.0 / 2.0) * _tmp15
        _tmp55 = (1.0 / 2.0) * _tmp18
        _tmp56 = _tmp54 + _tmp55
        _tmp57 = _tmp52 + _tmp53 + _tmp56
        _tmp58 = 2 * _tmp19
        _tmp59 = _tmp54 - _tmp55
        _tmp60 = _tmp51 + _tmp53 + _tmp59
        _tmp61 = -_tmp41
        _tmp62 = _tmp42 + _tmp48 + _tmp61
        _tmp63 = _tmp35 + _tmp36
        _tmp64 = -_tmp31
        _tmp65 = _tmp33 + _tmp64
        _tmp66 = _tmp63 + _tmp65
        _tmp67 = -_tmp22
        _tmp68 = _tmp21 + _tmp67
        _tmp69 = _tmp24 + _tmp27 + _tmp68
        _tmp70 = _tmp32 + _tmp38 + _tmp64
        _tmp71 = _tmp25 + _tmp26 + _tmp68
        _tmp72 = -_tmp53
        _tmp73 = _tmp51 + _tmp56 + _tmp72
        _tmp74 = _tmp45 + _tmp46
        _tmp75 = _tmp43 + _tmp61
        _tmp76 = _tmp74 + _tmp75
        _tmp77 = _tmp23 + _tmp24 + _tmp26
        _tmp78 = _tmp44 + _tmp47 + _tmp75
        _tmp79 = -_tmp50 * _tmp78
        _tmp80 = _tmp34 + _tmp37 + _tmp65
        _tmp81 = _tmp52 + _tmp59 + _tmp72
        _tmp82 = _tmp58 * _tmp81
        _tmp83 = -_tmp40 * _tmp80 + _tmp82
        _tmp84 = _tmp30 * _tmp81
        _tmp85 = _tmp40 * _tmp78
        _tmp86 = _tmp30 * _tmp80
        _tmp87 = _tmp50 * _tmp81
        _tmp88 = _tmp31 + _tmp32 + _tmp63
        _tmp89 = _tmp20 + _tmp28 + _tmp67
        _tmp90 = -_tmp30 * _tmp89
        _tmp91 = _tmp40 * _tmp81
        _tmp92 = _tmp50 * _tmp89
        _tmp93 = _tmp41 + _tmp42 + _tmp74

        # Output terms
        _res = [0.0] * 4
        _res[0] = _tmp4
        _res[1] = _tmp9
        _res[2] = _tmp14
        _res[3] = _tmp19
        _res_D_a = numpy.zeros((3, 3))
        _res_D_a[0, 0] = _tmp29 * _tmp30 - _tmp39 * _tmp40 - _tmp49 * _tmp50 + _tmp57 * _tmp58
        _res_D_a[1, 0] = _tmp29 * _tmp58 - _tmp30 * _tmp57 - _tmp39 * _tmp50 + _tmp40 * _tmp49
        _res_D_a[2, 0] = -_tmp29 * _tmp40 - _tmp30 * _tmp39 + _tmp49 * _tmp58 + _tmp50 * _tmp57
        _res_D_a[0, 1] = _tmp30 * _tmp60 - _tmp40 * _tmp62 - _tmp50 * _tmp66 + _tmp58 * _tmp69
        _res_D_a[1, 1] = -_tmp30 * _tmp69 + _tmp40 * _tmp66 - _tmp50 * _tmp62 + _tmp58 * _tmp60
        _res_D_a[2, 1] = -_tmp30 * _tmp62 - _tmp40 * _tmp60 + _tmp50 * _tmp69 + _tmp58 * _tmp66
        _res_D_a[0, 2] = _tmp30 * _tmp70 - _tmp40 * _tmp71 - _tmp50 * _tmp73 + _tmp58 * _tmp76
        _res_D_a[1, 2] = -_tmp30 * _tmp76 + _tmp40 * _tmp73 - _tmp50 * _tmp71 + _tmp58 * _tmp70
        _res_D_a[2, 2] = -_tmp30 * _tmp71 - _tmp40 * _tmp70 + _tmp50 * _tmp76 + _tmp58 * _tmp73
        _res_D_b = numpy.zeros((3, 3))
        _res_D_b[0, 0] = _tmp30 * _tmp77 + _tmp79 + _tmp83
        _res_D_b[1, 0] = -_tmp50 * _tmp80 + _tmp58 * _tmp77 - _tmp84 + _tmp85
        _res_D_b[2, 0] = -_tmp40 * _tmp77 + _tmp58 * _tmp78 - _tmp86 + _tmp87
        _res_D_b[0, 1] = -_tmp50 * _tmp88 + _tmp58 * _tmp89 + _tmp84 - _tmp85
        _res_D_b[1, 1] = _tmp40 * _tmp88 + _tmp79 + _tmp82 + _tmp90
        _res_D_b[2, 1] = -_tmp30 * _tmp78 + _tmp58 * _tmp88 - _tmp91 + _tmp92
        _res_D_b[0, 2] = -_tmp40 * _tmp89 + _tmp58 * _tmp93 + _tmp86 - _tmp87
        _res_D_b[1, 2] = -_tmp30 * _tmp93 + _tmp58 * _tmp80 + _tmp91 - _tmp92
        _res_D_b[2, 2] = _tmp50 * _tmp93 + _tmp83 + _tmp90
        return sym.Rot3.from_storage(_res), _res_D_a, _res_D_b

    @staticmethod
    def between_with_jacobians(a, b):
        # type: (sym.Rot3, sym.Rot3) -> T.Tuple[sym.Rot3, numpy.ndarray, numpy.ndarray]

        # Total ops: 161

        # Input arrays
        _a = a.data
        _b = b.data

        # Intermediate terms (78)
        _tmp0 = _a[3] * _b[0]
        _tmp1 = _a[2] * _b[1]
        _tmp2 = _a[0] * _b[3]
        _tmp3 = _a[1] * _b[2]
        _tmp4 = _tmp0 + _tmp1 - _tmp2 - _tmp3
        _tmp5 = _a[3] * _b[1]
        _tmp6 = _a[2] * _b[0]
        _tmp7 = _a[0] * _b[2]
        _tmp8 = _a[1] * _b[3]
        _tmp9 = _tmp5 - _tmp6 + _tmp7 - _tmp8
        _tmp10 = _a[3] * _b[2]
        _tmp11 = _a[2] * _b[3]
        _tmp12 = _a[0] * _b[1]
        _tmp13 = _a[1] * _b[0]
        _tmp14 = _tmp10 - _tmp11 - _tmp12 + _tmp13
        _tmp15 = _a[3] * _b[3]
        _tmp16 = _a[2] * _b[2]
        _tmp17 = _a[0] * _b[0]
        _tmp18 = _a[1] * _b[1]
        _tmp19 = _tmp15 + _tmp16 + _tmp17 + _tmp18
        _tmp20 = (1.0 / 2.0) * _tmp15
        _tmp21 = (1.0 / 2.0) * _tmp16
        _tmp22 = (1.0 / 2.0) * _tmp17
        _tmp23 = (1.0 / 2.0) * _tmp18
        _tmp24 = -_tmp20 - _tmp21 - _tmp22 - _tmp23
        _tmp25 = 2 * _tmp19
        _tmp26 = _tmp24 * _tmp25
        _tmp27 = (1.0 / 2.0) * _tmp0
        _tmp28 = (1.0 / 2.0) * _tmp1
        _tmp29 = (1.0 / 2.0) * _tmp2
        _tmp30 = (1.0 / 2.0) * _tmp3
        _tmp31 = _tmp27 + _tmp28 - _tmp29 - _tmp30
        _tmp32 = 2 * _tmp4
        _tmp33 = _tmp31 * _tmp32
        _tmp34 = (1.0 / 2.0) * _tmp10
        _tmp35 = (1.0 / 2.0) * _tmp11
        _tmp36 = (1.0 / 2.0) * _tmp12
        _tmp37 = (1.0 / 2.0) * _tmp13
        _tmp38 = _tmp34 - _tmp35 - _tmp36 + _tmp37
        _tmp39 = 2 * _tmp14
        _tmp40 = _tmp38 * _tmp39
        _tmp41 = (1.0 / 2.0) * _tmp5
        _tmp42 = (1.0 / 2.0) * _tmp6
        _tmp43 = (1.0 / 2.0) * _tmp7
        _tmp44 = (1.0 / 2.0) * _tmp8
        _tmp45 = -_tmp41 + _tmp42 - _tmp43 + _tmp44
        _tmp46 = 2 * _tmp9
        _tmp47 = -_tmp45 * _tmp46
        _tmp48 = _tmp40 + _tmp47
        _tmp49 = -_tmp31 * _tmp46
        _tmp50 = 2 * _tmp24
        _tmp51 = _tmp14 * _tmp50
        _tmp52 = _tmp32 * _tmp45
        _tmp53 = _tmp25 * _tmp38 + _tmp52
        _tmp54 = _tmp50 * _tmp9
        _tmp55 = -_tmp32 * _tmp38
        _tmp56 = _tmp25 * _tmp45 + _tmp55
        _tmp57 = _tmp41 - _tmp42 + _tmp43 - _tmp44
        _tmp58 = -2 * _tmp34 + 2 * _tmp35 + 2 * _tmp36 - 2 * _tmp37
        _tmp59 = _tmp19 * _tmp58 + _tmp49
        _tmp60 = _tmp46 * _tmp57
        _tmp61 = -_tmp14 * _tmp58
        _tmp62 = _tmp33 + _tmp61
        _tmp63 = -_tmp39 * _tmp57
        _tmp64 = _tmp4 * _tmp50
        _tmp65 = _tmp58 * _tmp9
        _tmp66 = _tmp25 * _tmp31 + _tmp65
        _tmp67 = -_tmp27 - _tmp28 + _tmp29 + _tmp30
        _tmp68 = _tmp39 * _tmp67
        _tmp69 = _tmp25 * _tmp57 + _tmp68
        _tmp70 = _tmp25 * _tmp67 + _tmp63
        _tmp71 = -_tmp32 * _tmp67
        _tmp72 = _tmp20 + _tmp21 + _tmp22 + _tmp23
        _tmp73 = _tmp25 * _tmp72
        _tmp74 = _tmp71 + _tmp73
        _tmp75 = _tmp39 * _tmp72
        _tmp76 = _tmp46 * _tmp72
        _tmp77 = _tmp32 * _tmp72

        # Output terms
        _res = [0.0] * 4
        _res[0] = _tmp4
        _res[1] = _tmp9
        _res[2] = _tmp14
        _res[3] = _tmp19
        _res_D_a = numpy.zeros((3, 3))
        _res_D_a[0, 0] = _tmp26 - _tmp33 + _tmp48
        _res_D_a[1, 0] = _tmp49 - _tmp51 + _tmp53
        _res_D_a[2, 0] = -_tmp31 * _tmp39 + _tmp54 + _tmp56
        _res_D_a[0, 1] = -_tmp32 * _tmp57 + _tmp51 + _tmp59
        _res_D_a[1, 1] = _tmp26 - _tmp60 + _tmp62
        _res_D_a[2, 1] = _tmp63 - _tmp64 + _tmp66
        _res_D_a[0, 2] = -_tmp54 + _tmp55 + _tmp69
        _res_D_a[1, 2] = -_tmp38 * _tmp46 + _tmp64 + _tmp70
        _res_D_a[2, 2] = _tmp26 - _tmp40 + _tmp60 + _tmp71
        _res_D_b = numpy.zeros((3, 3))
        _res_D_b[0, 0] = _tmp48 + _tmp74
        _res_D_b[1, 0] = -_tmp46 * _tmp67 + _tmp53 - _tmp75
        _res_D_b[2, 0] = _tmp56 - _tmp68 + _tmp76
        _res_D_b[0, 1] = -_tmp52 + _tmp59 + _tmp75
        _res_D_b[1, 1] = _tmp47 + _tmp62 + _tmp73
        _res_D_b[2, 1] = -_tmp39 * _tmp45 + _tmp66 - _tmp77
        _res_D_b[0, 2] = -_tmp4 * _tmp58 + _tmp69 - _tmp76
        _res_D_b[1, 2] = -_tmp65 + _tmp70 + _tmp77
        _res_D_b[2, 2] = _tmp60 + _tmp61 + _tmp74
        return sym.Rot3.from_storage(_res), _res_D_a, _res_D_b
