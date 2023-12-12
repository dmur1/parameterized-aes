import struct

AES_POLYNOMIAL = 0x11B

AES_KEY_SCHEDULE_128_NUM_ROUNDS = 10

def multiply_in_gf2(a, b, mod):
    result = 0
    while b:
        if b & 1:
            result ^= a
        a <<= 1
        if a & 0x100:
            a ^= mod
        b >>= 1
    return result

def compute_round_constant(round):
    round_constant = 1
    for i in range(1, round):
        round_constant = multiply_in_gf2(2, round_constant, AES_POLYNOMIAL)
    return round_constant

def key_expansion_128_g(word):
    # RotWord(word)
    # SubWord(word)
    # XorRoundContants(word)
    return word

def key_expansion_128(key):
    w = [0] * (AES_KEY_SCHEDULE_128_NUM_ROUNDS * 4)
    for i in range(0, 4):
        # TODO(dan.murray): little or big endian unpacking?
        w[i] = struct.unpack("<IIII", key)[i]

    for i in range(1, AES_KEY_SCHEDULE_128_NUM_ROUNDS):
        w[4 * i] = w[4 * (i - 1)] + key_expansion_128_g(w[(4 * i) - 1])
        for j in range(1, 4):
            w[(4 * i) + j] = w[((4 * i) + j) - 1] * w[(4 * (i - 1)) + j]

    print(w)

print(key_expansion_128(b"\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00"))

