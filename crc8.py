import pandas as pd

def crc8_compute(data, initial_crc=0x00, polynomial=0x07):
    crc = initial_crc
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ polynomial
            else:
                crc <<= 1
            crc &= 0xFF  # Ensure CRC remains an 8-bit value
    return crc

def calculate_crc_from_hex_string(hex_string):
    data_bytes = bytes.fromhex(hex_string)
    return crc8_compute(data_bytes)

# Read the Excel file
input_file = 'trame.xlsx'  # Replace with your input file path
df = pd.read_excel(input_file, engine='openpyxl')

# Ensure there is a column named 'HexString'
if 'HexString' not in df.columns:
    raise ValueError("The input Excel file must contain a column named 'HexString'.")

# Calculate CRC-8 for each hex string
df['CRC-8'] = df['HexString'].apply(calculate_crc_from_hex_string)

# Write the results back to a new Excel file
output_file = 'output_with_crc.xlsx'  # Replace with your desired output file path
df.to_excel(output_file, index=False, engine='openpyxl')

print(f"CRC-8 results have been written to {output_file}")


