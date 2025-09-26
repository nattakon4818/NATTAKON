def dec_to_bin(number):
    binary = bin(number)[2:]  # ตัด '0b' ออก
    # เติม 0 ด้านหน้าให้ครบกลุ่มละ 4 บิต
    padded = binary.zfill((4 - len(binary) % 4) % 4 + len(binary))
    # แบ่งเป็นกลุ่มละ 4
    grouped = ' '.join(padded[i:i+4] for i in range(0, len(padded), 4))
    return grouped

# ทดสอบ
print(dec_to_bin(142))  # ผลลัพธ์: 1000 1110
