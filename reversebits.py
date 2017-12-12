def reverseBits(n):
    # first convert to bit stream (LSB is bits[0])
    bits = []
    while len(bits)<32:
        if n%2==1:
            bits.append(True)
            n = (n-1)/2
        else:
            bits.append(False)
            n = n/2
    print(bits)
    res = 0
    for b in bits:
        res *= 2
        res += int(b)
    return res
    
print(reverseBits(43261596))
        
