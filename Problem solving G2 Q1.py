def to_twos_complement(val, bits):
    if val < 0:
        val = (1 << bits) + val
    return f"{val:0{bits}b}"

def from_twos_complement(binary_str, bits):
    val = int(binary_str, 2)
    if val & (1 << (bits - 1)):
        val -= (1 << bits)
    return val

def execute_arithmetic(op1, op2):
    mask = (1 << 16) - 1
    
    bin_op1_8 = to_twos_complement(op1, 8)
    bin_op2_8 = to_twos_complement(op2, 8)
    
    val1_16 = op1 & mask
    val2_16 = op2 & mask
    
    result_16 = (val1_16 - val2_16) & mask
    result_dec = from_twos_complement(f"{result_16:016b}", 16)
    bin_result_16 = to_twos_complement(result_dec, 16)
    
    sign_op1 = (val1_16 >> 15) & 1
    sign_op2 = (val2_16 >> 15) & 1
    sign_res = (result_16 >> 15) & 1
    
    overflow = (sign_op1 != sign_op2) and (sign_res != sign_op1)
    
    print(f"Operand 1 (8-bit): {bin_op1_8}")
    print(f"Operand 2 (8-bit): {bin_op2_8}")
    print(f"Result (16-bit Binary): {bin_result_16}")
    print(f"Result (Decimal): {result_dec}")
    print(f"Overflow Detected: {overflow}")
    print("-" * 40)

print("Expression a) (35 - (+29))")
execute_arithmetic(35, 29)

print("Expression b) ((-35) - (-12))")
execute_arithmetic(-35, -12)
