import random


def crc8(*args):
    crc = 0b11010101
    for datagram in args:
        for byte in datagram:
            for _ in range(0, 8):
                if (crc >> 7) ^ (byte & 0x01):
                    crc = ((crc << 1) ^ 0x07) & 0xFF
                else:
                    crc = (crc << 1) & 0xFF
                byte = byte >> 1
    return crc


bin_str = input("Ведите двоичное число:")
bin_code = int(bin_str, 2)
hex_code = bin_code.to_bytes(3, 'big')
kod = crc8(hex_code)
print("CRC8:", bin(kod)[2:])
print("Сообщение (число + CRC):", bin_str + bin(kod)[2:])
num_bit = random.randint(1, len(bin_str))
error_message = '{0}{1}{2}'.format(bin_str[:num_bit - 1], int(bin_str[num_bit - 1]) ^ 1, bin_str[num_bit:])
print("Сообщение с ошибкой (число + CRC):", error_message + bin(kod)[2:])
error_kod = crc8(int(error_message, 2).to_bytes(3, 'big'))
print("CRC8 сообщения с ошибкой:", bin(error_kod)[2:])


