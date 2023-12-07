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

def compute_round_constant(round, aes_polynomial):
    round_constant = 1
    for i in range(1, round):
        round_constant = multiply_in_gf2(2, round_constant, aes_polynomial)
    return round_constant

for i in range(1, 10):
    print(hex(compute_round_constant(i, 0x11B)))
