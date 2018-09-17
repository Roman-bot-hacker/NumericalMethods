import pprint
from scipy import reshape
import scipy.linalg   # SciPy Linear Algebra Library

class Matrix:

    def __init__(self):
        k = 13
        p = 21
        c = 0.02*k
        b = 0.02*p
        self.n = 4
        self.A = [[8.3, 2.62+c, 4.1, 1.9], [3.92, 8.45, 7.78-c, 2.46], [3.77, 7.21+c, 8.04, 2.28], [2.21, 3.65-c, 1.69, 6.69]]
        self.B = [-10.65+b, 12.21, 15.45-b, -8.35]
        self.L = range(self.n*self.n)
        self.L = reshape(self.L, (self.n,self.n))
        self.U = range(self.n*self.n)
        self.U = reshape(self.U, (self.n,self.n))

    def LU(self):
        P, self.L, self.U = scipy.linalg.lu(self.A)

        print("A:")
        pprint.pprint(self.A)

        print("B: ")
        pprint.pprint(self.B)

        print("P:")
        pprint.pprint(P)

        print("L:")
        pprint.pprint(self.L)

        print("U:")
        pprint.pprint(self.U)

    def straight_move(self):
        Y = range(self.n)
        Y = reshape(Y, (self.n, 1))
        Y[0] = float(self.B[0] / self.L[0][0])
        for i in range(1, self.n-1):
            s = 0
            for m in range(0, i - 1):
                s += self.L[i][m] * Y[m]
            Y[i] = float((self.B[i] - s) / self.L[i][i])
        print("Y: ")
        pprint.pprint(Y)
        return Y

    def reverse_move(self,Y):
        X = range(self.n)
        X = reshape(X, (self.n, 1))
        X[self.n-1] = float(Y[self.n-1])
        for i in range(self.n - 2, 0, -1):
            s = 0
            for m in range(self.n-1, i-1, -1):
                s += self.U[i][m] * X[m]
            X[i] = float((Y[i] - s)/self.U[i][i])
        return X


if __name__ == "__main__":
    matrix = Matrix()
    matrix.LU()
    print("X: ")
    pprint.pprint(matrix.reverse_move(matrix.straight_move()))