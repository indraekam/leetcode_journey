class Solution:
    MOD = 10**9 + 7 

    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        size = 26
        T = [[0] * size for _ in range(size)]
        for i in range(size):
            for j in range(1, nums[i] + 1):
                to_idx = (i + j) % 26
                T[i][to_idx] = (T[i][to_idx] + 1) % self.MOD

        T_pow = self.mat_pow(T, t)

        freq = [0] * size
        for ch in s:
            freq[ord(ch) - ord('a')] += 1

        result = 0
        for i in range(size):
            for j in range(size):
                result = (result + freq[i] * T_pow[i][j]) % self.MOD

        return result

    def mat_mult(self, A, B):
        size = len(A)
        result = [[0] * size for _ in range(size)]
        for i in range(size):
            for k in range(size):
                if A[i][k] == 0:
                    continue
                for j in range(size):
                    result[i][j] = (result[i][j] + A[i][k] * B[k][j]) % self.MOD
        return result

    def mat_pow(self, mat, power):
        size = len(mat)
        result = [[int(i == j) for j in range(size)] for i in range(size)]  # identity matrix
        while power:
            if power % 2 == 1:
                result = self.mat_mult(result, mat)
            mat = self.mat_mult(mat, mat)
            power //= 2
        return result
