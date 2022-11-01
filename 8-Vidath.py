import sys


class Graph:
    def __int__(self, vertix):
        self.vertix = vertix

    def minCost(self, c, r):
        min = sys.maxsize
        pos = -1
        v = 0
        while (v < self.vertix):
            if (r[v] == False and c[v] < min):
                min = c[v]
                pos = v
            v += 1
        return pos

    def prim(self, matrix):
        r = [False] * (self.vertix)
        parent = [0] * (self.vertix)
        c = [0] * (self.vertix)
        i = 0
        while (i < self.vertix):
            c[i] = sys.maxsize
            r[i] = False
            i += 1
        c[0] = 0
        parent[0] = -1
        node = 0
        while (node < self.vertix - 1):
            u = self.minCost(c, r)
            r[u] = True
            v = 0
            while (v < self.vertix):
                if (matrix[u][v] != 0 and
                        r[v] == False and matrix[u][v] < c[v]):
                    parent[v] = u
                    c[v] = matrix[u][v]

                v += 1

            node += 1

        result = 0
        i = 1
        while (i < self.vertix):
            print("(", parent[i], "-", i, ")-", matrix[i][parent[i]])
            result += matrix[i][parent[i]]
            i += 1
        print(" Total minimum weight : ", result)


def main():
    matrix = [
        [0, 3, 0, 0, 0, 0],
        [3, 0, 4, 0, 0, 0],
        [0, 3, 0, 8, 0, 0],
        [0, 0, 8, 16, 0, 0],
        [0, 0, 0, 16, 0, 15],
        [0, 0, 0, 0, 15, 0]
    ]
    n = len(matrix[0])
    g = Graph(n)
    g.prim(matrix)


if __name__== "__main__":
  main()