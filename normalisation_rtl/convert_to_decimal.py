import re

def hex_to_signed_decimal(hex_str, bits=20):
    val = int(hex_str, 16)
    if val & (1 << (bits - 1)):
        val -= (1 << bits)
    return val

with open('check_norm.txt', 'r') as f:
    lines = f.readlines()

output_lines = []
for line in lines:
    match = re.search(r'Normalized row\s+(\d+):\s+([0-9a-fA-F]+)', line)
    if match:
        row_idx = match.group(1)
        hex_data = match.group(2)
        elements = []
        for i in range(0, len(hex_data), 5):
            hex_segment = hex_data[i:i+5]
            if len(hex_segment) == 5:
                elements.append(str(hex_to_signed_decimal(hex_segment)))
        output_lines.append(f"Row {row_idx}: " + "  ".join(elements))

with open('check_norm_decimal.txt', 'w') as f:
    f.write("\n".join(output_lines) + "\n")
