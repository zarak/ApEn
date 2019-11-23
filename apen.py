# Source: https://en.wikipedia.org/wiki/Approximate_entropy#Python_implementation

import numpy as np

def ApEn(U, m, r):

    def _maxdist(x_i, x_j):
        return max([abs(ua - va) for ua, va in zip(x_i, x_j)])

    def _phi(m):
        x = [[U[j] for j in range(i, i + m - 1 + 1)] for i in range(N - m + 1)]
        C = [len([1 for x_j in x if _maxdist(x_i, x_j) <= r]) / (N - m + 1.0) for x_i in x]
        return (N - m + 1.0)**(-1) * sum(np.log(C))

    N = len(U)

    return abs(_phi(m+1) - _phi(m))

# Usage example
U = np.array([85, 80, 89] * 17)
print(ApEn(U, 2, 3))
1.0996541105257052e-05

randU = np.random.choice([85, 80, 89], size=17*3)
print(ApEn(randU, 2, 3))
0.8626664154888908
