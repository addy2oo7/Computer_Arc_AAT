def rotate_left_no_carry(val_str, pos):
    val = int(val_str, 2)
    print(f"Original Binary: {val_str}")
    current = val
    for i in range(1, pos + 1):
        bit7 = (current >> 7) & 1
        current = ((current << 1) & 0xFF) | bit7
        print(f"  Step {i}: Bit 7 ({bit7}) shifted out -> Result: {current:08b}")
    return f"{current:08b}"

def rotate_left_with_carry(val_str, pos, initial_cf=0):
    val = int(val_str, 2)
    print(f"Original Binary: {val_str} | Initial Carry Flag: {initial_cf}")
    current_val = val
    cf = initial_cf
    for i in range(1, pos + 1):
        bit7 = (current_val >> 7) & 1
        current_val = ((current_val << 1) & 0xFF) | cf
        print(f"  Step {i}: Bit 7 ({bit7}) shifts to Carry | Old Carry ({cf}) shifts to Bit 0 -> Result: {current_val:08b} | New Carry: {bit7}")
        cf = bit7
    return f"{current_val:08b}", cf

print("=== a) Rotate Left Without Carry (ROL) ===")
final_rol = rotate_left_no_carry("11110110", 2)
print(f"Final 8-bit ROL Result: {final_rol}\n")

print("=== b) Rotate Left With Carry (RCL) ===")
final_rcl, final_cf = rotate_left_with_carry("10000110", 2, initial_cf=0)
print(f"Final 8-bit RCL Result: {final_rcl} | Final Carry Flag: {final_cf}")
