# Copyright (C) 2021-22 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause
# See: https://spdx.org/licenses/


def float_to_literal(learning_parameter: float) -> str:
    """Convert the floating point representation of the 
    learning parameter to the form mantissa * 2 ^ [+/1]exponent.

    Parameters
    ----------
    learning_parameters: float
        the float value of learning-related parameter
    
    Returns
    -------
    parameter_literal: str
        string representation of learning_parameter.
    """
    if number < 0:
        sign = -1
    else:
        sign = 1
    
    string_of_number = str(number)
    whole_number, decimal = string_of_number.split(".")

    result_whole_no = int(whole_number)
    binary_values_whole_number = ""

    while result_whole_no != 0 :
        binary_values_whole_number += str(result_whole_no % 2)
        result_whole_no = result_whole_no / 2

    result_decimal = float("0." + decimal)
    binary_values_decimal = ""
    
    while result_decimal != 0:
        result_decimal *= 2
        if result_decimal < 1:
            binary_values_decimal += "0"
        elif result_decimal >= 1:
            binary_values_decimal += "1"
            string_result_decimal = str(result_decimal)
            result_decimal = float("0." + string_result_decimal.split(".")[1])
    
    binary_learning_parameter = binary_values_whole_number[::-1] + binary_values_decimal

    """TODO: Shift the binary_learning_parameter and
    find the mantissa and exponent and return "str"

    Before that - find a better implementation. 
    """