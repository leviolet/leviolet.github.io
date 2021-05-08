# author: Leviolet
# license: MIT

class Matrix(object):
    data: list
    rows: int       # 行数
    cols: int       # 列数
    def __init__(self,data):
        self.data = data
        self.rows = len(data)
        self.cols = len(data[1])
        
    def __repr__(self):
        s = f"<Matrix {self.rows}*{self.cols}>"
        return '\n'.join([' '.join([str(y) for y in x]) for x in self.data])

    def show(self):
        for line in self.data:
            for elem in line:
                print(elem,end=' ')
            print('')
        print('')

#    def transpose(self):      # transpose:转置
#        self.data = [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
#        return self

    def t(self):                # 转置
        return Matrix(
            [[self.data[i][j] for i in range(self.rows)] for j in range(self.cols)]
        )
    
    def __add__(self,b):        # 加
        assert (self.rows,self.cols) == (b.rows,b.cols)
        return Matrix(
            [[self.data[i][j] + b.data[i][j] for j in range(self.cols)] for i in range(self.rows)]
        )
    
    def __mul__(self,mb):       # 乘
        a = self.data
        b = mb.data
        assert self.cols == mb.rows,f"{self.cols} {mb.rows}"
        return Matrix([
            [
                sum(
                    [a[i][n]*b[n][j] for n in range(self.cols)]
                ) for j in range(mb.cols)
            ] for i in range(self.rows)
        ])
    
    def mul_num(self,n: int):   # 数乘
        return Matrix(
            [[self.data[i][j] * n for j in range(self.cols)] for i in range(self.rows)]
        )
    
    def get(self,i,j):
        return self.data[i-1][j-1]

def create_matrix_from_str(s):
    data = [[int(y) for y in x.split(" ") if y] for x in s.split("\n") if x]
    return Matrix(data)


# m = Matrix([
#     [1,2,3,4],
#     [2,3,4,5],
#     [3,3,4,6]
# ])
# m.show()
# m.t().show()
# (m+m).show()
# m * m.t()
# m.mul_num(2).show()
# print(m.get(2,2))