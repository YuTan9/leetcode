class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        rev = 0
        for i in range(32):
            rev += (n%2) * (2**(31-i))
            n = n // 2

        return rev