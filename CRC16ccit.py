def crc16_ccitt(data, poly=0x1021, init_crc=0xFFFF, xor_out=0x0000):
    crc = init_crc
    for byte in data:
        crc ^= byte << 8
        for _ in range(8):
            if crc & 0x8000:
                crc = (crc << 1) ^ poly
            else:
                crc <<= 1
            crc &= 0xFFFF  
    return crc ^ xor_out


# Data 
data = bytes.fromhex("9000018C148F70")

# Calcul CRC16-CCITT
calculated_crc = crc16_ccitt(data)

# Format CRC 
crc_calculated_hex = format(calculated_crc, '04X')

print(crc_calculated_hex)

