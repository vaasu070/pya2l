"""
@project: pya2l
@file: dump_test.py
@author: Guillaume Sottas
@date: 19.02.2019
"""

import pytest

from pya2l.parser.a2l_node import *
from pya2l.parser.a2ml_node import *


def concatenate_generator(g, indent=4, line_ending='\n', indent_char=' '):
    return line_ending.join((((indent_char * indent) * i) + s) for i, s in g)


@pytest.mark.parametrize('a, s', [pytest.param((0, 0), 'A2ML_VERSION 0 0')])
def test_a2ml_version(a, s):
    n = A2ML_VERSION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ADDR_EPK 0')])
def test_addr_epk(a, s):
    n = ADDR_EPK(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ALIGNMENT_BYTE 0')])
def test_alignment_byte(a, s):
    n = ALIGNMENT_BYTE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ALIGNMENT_FLOAT32_IEEE 0')])
def test_alignment_float32_ieee(a, s):
    n = ALIGNMENT_FLOAT32_IEEE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ALIGNMENT_FLOAT64_IEEE 0')])
def test_alignment_float64_ieee(a, s):
    n = ALIGNMENT_FLOAT64_IEEE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ALIGNMENT_LONG 0')])
def test_alignment_long(a, s):
    n = ALIGNMENT_LONG(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ALIGNMENT_WORD 0')])
def test_alignment_word(a, s):
    n = ALIGNMENT_WORD(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([tuple()], '/begin ANNOTATION\n/end ANNOTATION'),
    pytest.param([(('annotation_label', ANNOTATION_LABEL('')),)],
                 '/begin ANNOTATION\n    ANNOTATION_LABEL ""\n/end ANNOTATION')])
def test_annotation(a, s):
    n = ANNOTATION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'ANNOTATION_LABEL ""')])
def test_annotation_label(a, s):
    n = ANNOTATION_LABEL(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'ANNOTATION_ORIGIN ""')])
def test_annotation_origin(a, s):
    n = ANNOTATION_ORIGIN(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin ANNOTATION_TEXT\n/end ANNOTATION_TEXT')])
def test_annotation_text(a, s):
    n = ANNOTATION_TEXT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ARRAY_SIZE 0')])
def test_array_size(a, s):
    n = ARRAY_SIZE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 0], 'ASAP2_VERSION 0 0')])
def test_asap2_version(a, s):
    n = ASAP2_VERSION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '_', '_', 0, 0.0, 0.0, tuple()], '/begin AXIS_DESCR _ _ _ 0 0.0 0.0\n/end AXIS_DESCR')])
def test_axis_descr(a, s):
    n = AXIS_DESCR(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 0, '_', '_', 0.0, '_', 0, 0.0, 0.0, tuple()], '''/begin AXIS_PTS _ "" 0 _ _ 0.0 _ 0 0.0 0.0
/end AXIS_PTS''')])
def test_axis_pts(a, s):
    n = AXIS_PTS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'AXIS_PTS_REF _')])
def test_axis_pts_ref(a, s):
    n = AXIS_PTS_REF(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([0, 'UBYTE', 'INDEX_INCR', 'PBYTE'], 'AXIS_PTS_X 0 UBYTE INDEX_INCR PBYTE')])
def test_axis_pts_x(a, s):
    n = AXIS_PTS_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([0, 'UBYTE', 'INDEX_INCR', 'PBYTE'], 'AXIS_PTS_Y 0 UBYTE INDEX_INCR PBYTE')])
def test_axis_pts_y(a, s):
    n = AXIS_PTS_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([0, 'UBYTE', 'INDEX_INCR', 'PBYTE'], 'AXIS_PTS_Z 0 UBYTE INDEX_INCR PBYTE')])
def test_axis_pts_z(a, s):
    n = AXIS_PTS_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([0, 'UBYTE', 0, 'INDEX_INCR', 'PBYTE'], 'AXIS_RESCALE_X 0 UBYTE 0 INDEX_INCR PBYTE')])
def test_axis_rescale_x(a, s):
    n = AXIS_RESCALE_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([0, 'UBYTE', 0, 'INDEX_INCR', 'PBYTE'], 'AXIS_RESCALE_Y 0 UBYTE 0 INDEX_INCR PBYTE')])
def test_axis_rescale_y(a, s):
    n = AXIS_RESCALE_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param([0, 'UBYTE', 0, 'INDEX_INCR', 'PBYTE'], 'AXIS_RESCALE_Z 0 UBYTE 0 INDEX_INCR PBYTE')])
def test_axis_rescale_z(a, s):
    n = AXIS_RESCALE_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'BIT_MASK 0')])
def test_bit_mask(a, s):
    n = BIT_MASK(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin BIT_OPERATION\n/end BIT_OPERATION')])
def test_bit_operation(a, s):
    n = BIT_OPERATION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['MSB_FIRST'], 'BYTE_ORDER MSB_FIRST')])
def test_byte_order(a, s):
    n = BYTE_ORDER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['CALIBRATION'], 'CALIBRATION_ACCESS CALIBRATION')])
def test_calibration_access(a, s):
    n = CALIBRATION_ACCESS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin CALIBRATION_HANDLE\n/end CALIBRATION_HANDLE')])
def test_calibration_handle(a, s):
    n = CALIBRATION_HANDLE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['', 0, tuple()], '/begin CALIBRATION_METHOD "" 0\n/end CALIBRATION_METHOD')])
def test_calibration_method(a, s):
    n = CALIBRATION_METHOD(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 'VALUE', 0, '_', 0.0, '_', 0.0, 0.0, tuple()],
                 '/begin CHARACTERISTIC _ "" VALUE 0 _ 0.0 _ 0.0 0.0\n/end CHARACTERISTIC')])
def test_characteristic(a, s):
    n = CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0.0, 0.0, 0.0, 0.0, 0.0, 0.0], 'COEFFS 0.0 0.0 0.0 0.0 0.0 0.0')])
def test_coeffs(a, s):
    n = COEFFS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'COMPARISON_QUANTITY _')])
def test_comparison_quantity(a, s):
    n = COMPARISON_QUANTITY(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 'TAB_INTP', '', '', tuple()], '/begin COMPU_METHOD _ "" TAB_INTP "" ""\n/end COMPU_METHOD')])
def test_compu_method(a, s):
    n = COMPU_METHOD(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 'TAB_INTP', 0, tuple()], '/begin COMPU_TAB _ "" TAB_INTP 0\n/end COMPU_TAB')])
def test_compu_tab(a, s):
    n = COMPU_TAB(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'COMPU_TAB_REF _')])
def test_compu_tab_ref(a, s):
    n = COMPU_TAB_REF(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 'TAB_INTP', 0, tuple()], '/begin COMPU_VTAB _ "" TAB_INTP 0\n/end COMPU_VTAB')])
def test_compu_vtab(a, s):
    n = COMPU_VTAB(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 0, tuple()], '/begin COMPU_VTAB_RANGE _ "" 0\n/end COMPU_VTAB_RANGE')])
def test_compu_vtab_range(a, s):
    n = COMPU_VTAB_RANGE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'CPU_TYPE ""')])
def test_cpu_type(a, s):
    n = CPU_TYPE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'CURVE_AXIS_REF _')])
def test_curve_axis_ref(a, s):
    n = CURVE_AXIS_REF(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'CUSTOMER ""')])
def test_customer(a, s):
    n = CUSTOMER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'CUSTOMER_NO ""')])
def test_customer_no(a, s):
    n = CUSTOMER_NO(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'DATA_SIZE 0')])
def test_data_size(a, s):
    n = DATA_SIZE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'DEFAULT_VALUE ""')])
def test_default_value(a, s):
    n = DEFAULT_VALUE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin DEF_CHARACTERISTIC\n/end DEF_CHARACTERISTIC')])
def test_def_characteristic(a, s):
    n = DEF_CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(["", tuple()], '/begin DEPENDENT_CHARACTERISTIC ""\n/end DEPENDENT_CHARACTERISTIC')])
def test_dependent_characteristic(a, s):
    n = DEPENDENT_CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['ABSOLUTE'], 'DEPOSIT ABSOLUTE')])
def test_deposit(a, s):
    n = DEPOSIT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'DISPLAY_IDENTIFIER _')])
def test_display_identifier(a, s):
    n = DISPLAY_IDENTIFIER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'DIST_OP_X 0 UBYTE')])
def test_dist_op_x(a, s):
    n = DIST_OP_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'DIST_OP_Y 0 UBYTE')])
def test_dist_op_y(a, s):
    n = DIST_OP_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'DIST_OP_Z 0 UBYTE')])
def test_dist_op_z(a, s):
    n = DIST_OP_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'ECU ""')])
def test_ecu(a, s):
    n = ECU(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ECU_ADDRESS 0')])
def test_ecu_address(a, s):
    n = ECU_ADDRESS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ECU_ADDRESS_EXTENSION 0')])
def test_ecu_address_extension(a, s):
    n = ECU_ADDRESS_EXTENSION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ECU_CALIBRATION_OFFSET 0')])
def test_ecu_calibration_offset(a, s):
    n = ECU_CALIBRATION_OFFSET(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'EPK ""')])
def test_epk(a, s):
    n = EPK(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'ERROR_MASK 0')])
def test_error_mask(a, s):
    n = ERROR_MASK(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0.0, 0.0], 'EXTENDED_LIMITS 0.0 0.0')])
def test_extended_limits(a, s):
    n = EXTENDED_LIMITS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 0, 0], 'FIX_AXIS_PAR 0 0 0')])
def test_fix_axis_par(a, s):
    n = FIX_AXIS_PAR(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 0, 0], 'FIX_AXIS_PAR_DIST 0 0 0')])
def test_fix_axis_par_dist(a, s):
    n = FIX_AXIS_PAR_DIST(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin FIX_AXIS_PAR_LIST\n/end FIX_AXIS_PAR_LIST')])
def test_fix_axis_par_list(a, s):
    n = FIX_AXIS_PAR_LIST(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'FIX_NO_AXIS_PTS_X 0')])
def test_fix_no_axis_pts_x(a, s):
    n = FIX_NO_AXIS_PTS_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'FIX_NO_AXIS_PTS_Y 0')])
def test_fix_no_axis_pts_y(a, s):
    n = FIX_NO_AXIS_PTS_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'FIX_NO_AXIS_PTS_Z 0')])
def test_fix_no_axis_pts_z(a, s):
    n = FIX_NO_AXIS_PTS_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE', 'ROW_DIR', 'PBYTE'], 'FNC_VALUES 0 UBYTE ROW_DIR PBYTE')])
def test_fnc_values(a, s):
    n = FNC_VALUES(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'FORMAT ""')])
def test_format(a, s):
    n = FORMAT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['', tuple()], '/begin FORMULA ""\n/end FORMULA')])
def test_formula(a, s):
    n = FORMULA(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'FORMULA_INV ""')])
def test_formula_inv(a, s):
    n = FORMULA_INV(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', '', 0, 0, tuple()], '/begin FRAME _ "" 0 0\n/end FRAME')])
def test_frame(a, s):
    n = FRAME(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin FRAME_MEASUREMENT\n/end FRAME_MEASUREMENT')])
def test_frame_measurement(a, s):
    n = FRAME_MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', '', tuple()], '/begin FUNCTION _ ""\n/end FUNCTION')])
def test_function(a, s):
    n = FUNCTION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin FUNCTION_LIST\n/end FUNCTION_LIST')])
def test_function_list(a, s):
    n = FUNCTION_LIST(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'FUNCTION_VERSION ""')])
def test_function_version(a, s):
    n = FUNCTION_VERSION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', '', tuple()], '/begin GROUP _ ""\n/end GROUP')])
def test_group(a, s):
    n = GROUP(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['', tuple()], '/begin HEADER ""\n/end HEADER')])
def test_header(a, s):
    n = HEADER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'IDENTIFICATION 0 UBYTE')])
def test_identification(a, s):
    n = IDENTIFICATION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin IN_MEASUREMENT\n/end IN_MEASUREMENT')])
def test_in_measurement(a, s):
    n = IN_MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'LEFT_SHIFT 0')])
def test_left_shift(a, s):
    n = LEFT_SHIFT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin LOC_MEASUREMENT\n/end LOC_MEASUREMENT')])
def test_loc_measurement(a, s):
    n = LOC_MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin MAP_LIST\n/end MAP_LIST')])
def test_map_list(a, s):
    n = MAP_LIST(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 0, 0], 'MATRIX_DIM 0 0 0')])
def test_matrix_dim(a, s):
    n = MATRIX_DIM(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0.0], 'MAX_GRAD 0.0')])
def test_max_grad(a, s):
    n = MAX_GRAD(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 0], 'MAX_REFRESH 0 0')])
def test_max_refresh(a, s):
    n = MAX_REFRESH(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', '', 'UBYTE', '_', 0, 0.0, 0.0, 0.0, tuple()],
                                               '/begin MEASUREMENT _ "" UBYTE _ 0 0.0 0.0 0.0\n/end MEASUREMENT')])
def test_measurement(a, s):
    n = MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['PRG_CODE', 0, 0, [0, 0, 0, 0, 0], tuple()],
                                               '/begin MEMORY_LAYOUT PRG_CODE 0 0 0 0 0 0 0\n/end MEMORY_LAYOUT')])
def test_memory_layout(a, s):
    n = MEMORY_LAYOUT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', 'CODE', 'RAM', 'INTERN', 0, 0, [0, 0, 0, 0, 0], tuple()],
                 '/begin MEMORY_SEGMENT _ "" CODE RAM INTERN 0 0 0 0 0 0 0\n/end MEMORY_SEGMENT')])
def test_memory_segment(a, s):
    n = MEMORY_SEGMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', '', tuple()], '/begin MODULE _ ""\n/end MODULE')])
def test_module(a, s):
    n = MODULE(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['', tuple()], '/begin MOD_COMMON ""\n/end MOD_COMMON')])
def test_mod_common(a, s):
    n = MOD_COMMON(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['', tuple()], '/begin MOD_PAR ""\n/end MOD_PAR')])
def test_mod_par(a, s):
    n = MOD_PAR(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['MON_INCREASE'], 'MONOTONY MON_INCREASE')])
def test_monotony(a, s):
    n = MONOTONY(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'NO_AXIS_PTS_X 0 UBYTE')])
def test_no_axis_pts_x(a, s):
    n = NO_AXIS_PTS_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'NO_AXIS_PTS_Y 0 UBYTE')])
def test_no_axis_pts_y(a, s):
    n = NO_AXIS_PTS_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'NO_AXIS_PTS_Z 0 UBYTE')])
def test_no_axis_pts_z(a, s):
    n = NO_AXIS_PTS_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'NO_OF_INTERFACES 0')])
def test_no_of_interfaces(a, s):
    n = NO_OF_INTERFACES(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'NO_RESCALE_X 0 UBYTE')])
def test_no_rescale_x(a, s):
    n = NO_RESCALE_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'NO_RESCALE_Y 0 UBYTE')])
def test_no_rescale_y(a, s):
    n = NO_RESCALE_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'NO_RESCALE_Z 0 UBYTE')])
def test_no_rescale_z(a, s):
    n = NO_RESCALE_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'NUMBER 0')])
def test_number(a, s):
    n = NUMBER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'OFFSET_X 0 UBYTE')])
def test_offset_x(a, s):
    n = OFFSET_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'OFFSET_Y 0 UBYTE')])
def test_offset_y(a, s):
    n = OFFSET_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'OFFSET_Z 0 UBYTE')])
def test_offset_z(a, s):
    n = OFFSET_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin OUT_MEASUREMENT\n/end OUT_MEASUREMENT')])
def test_out_measurement(a, s):
    n = OUT_MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'PHONE_NO ""')])
def test_phone_no(a, s):
    n = PHONE_NO(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', '', tuple()], '/begin PROJECT _ ""\n/end PROJECT')])
def test_project(a, s):
    n = PROJECT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'PROJECT_NO _')])
def test_project_no(a, s):
    n = PROJECT_NO(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', tuple()], '/begin RECORD_LAYOUT _\n/end RECORD_LAYOUT')])
def test_record_layout(a, s):
    n = RECORD_LAYOUT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin REF_CHARACTERISTIC\n/end REF_CHARACTERISTIC')])
def test_ref_characteristic(a, s):
    n = REF_CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin REF_GROUP\n/end REF_GROUP')])
def test_ref_group(a, s):
    n = REF_GROUP(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin REF_MEASUREMENT\n/end REF_MEASUREMENT')])
def test_ref_measurement(a, s):
    n = REF_MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'REF_MEMORY_SEGMENT _')])
def test_ref_memory_segment(a, s):
    n = REF_MEMORY_SEGMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'REF_UNIT _')])
def test_ref_unit(a, s):
    n = REF_UNIT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'BYTE'], 'RESERVED 0 BYTE')])
def test_reserved(a, s):
    n = RESERVED(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0], 'RIGHT_SHIFT 0')])
def test_right_shift(a, s):
    n = RIGHT_SHIFT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'RIP_ADDR_W 0 UBYTE')])
def test_rip_addr_w(a, s):
    n = RIP_ADDR_W(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'RIP_ADDR_X 0 UBYTE')])
def test_rip_addr_x(a, s):
    n = RIP_ADDR_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'RIP_ADDR_Y 0 UBYTE')])
def test_rip_addr_y(a, s):
    n = RIP_ADDR_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'RIP_ADDR_Z 0 UBYTE')])
def test_rip_addr_z(a, s):
    n = RIP_ADDR_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'SHIFT_OP_X 0 UBYTE')])
def test_shift_op_x(a, s):
    n = SHIFT_OP_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'SHIFT_OP_Y 0 UBYTE')])
def test_shift_op_y(a, s):
    n = SHIFT_OP_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'SHIFT_OP_Z 0 UBYTE')])
def test_shift_op_z(a, s):
    n = SHIFT_OP_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 0, 0, 0, 0, 0, 0], 'SI_EXPONENTS 0 0 0 0 0 0 0')])
def test_si_exponents(a, s):
    n = SI_EXPONENTS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'SRC_ADDR_X 0 UBYTE')])
def test_src_addr_x(a, s):
    n = SRC_ADDR_X(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'SRC_ADDR_Y 0 UBYTE')])
def test_src_addr_y(a, s):
    n = SRC_ADDR_Y(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0, 'UBYTE'], 'SRC_ADDR_Z 0 UBYTE')])
def test_src_addr_z(a, s):
    n = SRC_ADDR_Z(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin SUB_FUNCTION\n/end SUB_FUNCTION')])
def test_sub_function(a, s):
    n = SUB_FUNCTION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin SUB_GROUP\n/end SUB_GROUP')])
def test_sub_group(a, s):
    n = SUB_GROUP(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'SUPPLIER ""')])
def test_supplier(a, s):
    n = SUPPLIER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['', ''], 'SYSTEM_CONSTANT "" ""')])
def test_system_constant(a, s):
    n = SYSTEM_CONSTANT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'S_REC_LAYOUT _')])
def test_s_rec_layout(a, s):
    n = S_REC_LAYOUT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', '', 'DERIVED', tuple()], '/begin UNIT _ "" "" DERIVED\n/end UNIT')])
def test_unit(a, s):
    n = UNIT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([0.0, 0.0], 'UNIT_CONVERSION 0.0 0.0')])
def test_unit_conversion(a, s):
    n = UNIT_CONVERSION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'USER ""')])
def test_user(a, s):
    n = USER(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', tuple()], '/begin USER_RIGHTS _\n/end USER_RIGHTS')])
def test_user_rights(a, s):
    n = USER_RIGHTS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin VARIANT_CODING\n/end VARIANT_CODING')])
def test_variant_coding(a, s):
    n = VARIANT_CODING(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin VAR_ADDRESS\n/end VAR_ADDRESS')])
def test_var_address(a, s):
    n = VAR_ADDRESS(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_', tuple()], '/begin VAR_CHARACTERISTIC _\n/end VAR_CHARACTERISTIC')])
def test_var_characteristic(a, s):
    n = VAR_CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['_', '', [], tuple()], '/begin VAR_CRITERION _ ""\n/end VAR_CRITERION')])
def test_var_criterion(a, s):
    n = VAR_CRITERION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin VAR_FORBIDDEN_COMB\n/end VAR_FORBIDDEN_COMB')])
def test_var_forbidden_comb(a, s):
    n = VAR_FORBIDDEN_COMB(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'VAR_MEASUREMENT _')])
def test_var_measurement(a, s):
    n = VAR_MEASUREMENT(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['NUMERIC'], 'VAR_NAMING NUMERIC')])
def test_var_naming(a, s):
    n = VAR_NAMING(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param(['_'], 'VAR_SELECTION_CHARACTERISTIC _')])
def test_var_selection_characteristic(a, s):
    n = VAR_SELECTION_CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'VAR_SEPARATOR ""')])
def test_var_separator(a, s):
    n = VAR_SEPARATOR(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([''], 'VERSION ""')])
def test_version(a, s):
    n = VERSION(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [pytest.param([tuple()], '/begin VIRTUAL\n/end VIRTUAL')])
def test_virtual(a, s):
    n = VIRTUAL(*a)
    assert concatenate_generator(n.dump()) == s


@pytest.mark.parametrize('a, s', [
    pytest.param(['', tuple()], '/begin VIRTUAL_CHARACTERISTIC ""\n/end VIRTUAL_CHARACTERISTIC')])
def test_virtual_characteristic(a, s):
    n = VIRTUAL_CHARACTERISTIC(*a)
    assert concatenate_generator(n.dump()) == s


def kwargs(**e):
    result = list()
    for k, v in e.items():
        result.append((k, v))
    return result


@pytest.mark.parametrize('a, s', [
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='char'))), 'block "_"\nchar'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='double'))), 'block "_"\ndouble'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='float'))), 'block "_"\nfloat'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='int'))), 'block "_"\nint'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='long'))), 'block "_"\nlong'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='uchar'))), 'block "_"\nuchar'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='uint'))), 'block "_"\nuint'),
    pytest.param(kwargs(tag='_', type_name=PredefinedTypeName(*kwargs(type_name='ulong'))), 'block "_"\nulong')])
def test_block(a, s):
    n = BlockDefinition(*a)
    assert concatenate_generator(n.dump()) == s


def test_declaration(a, s):
    n = Declaration(*a)
    assert concatenate_generator(n.dump()) == s


def test_enum():
    pass


def test_enumerator():
    pass


def test_member():
    pass


def test_predefined_type_name():
    pass


def test_struct():
    pass


def test_struct_member():
    pass


def test_tagged_struct():
    pass


def test_tagged_struct_definition():
    pass


def test_tagged_struct_member():
    pass


def test_tagged_union():
    pass


def test_tagged_union_member():
    pass


def test_type_definition():
    pass


def test_type_name():
    pass
