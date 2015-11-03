def read_matrix(filename):
    matrix = []
    f = open(filename, "r")
    i = 0
    for line in f:
        matrix.append(line.split())
        i += 1
    f.close()
    return matrix

class Matrix(object):
    def __init__(self, matrix):
        self.matrix = matrix
        
    def __repr__(self):
        str_matrix = ""
        for line in self.matrix:
            str_matrix += " ".join(line) + "\n"
        return str_matrix
    
    def transpose(self):
        row_lens = []
        for row in self.matrix:
            row_lens.append(len(row))            

        tr_rows = max(row_lens)
        tr_cols = len(self.matrix)
        tr_matrix = []

        for i in range(tr_rows):
            tr_matrix.append([" "] * tr_cols)
            
        for row in range(len(self.matrix)):
            for col in range(len(self.matrix[row])):
                tr_matrix[col][row] = str(self.matrix[row][col])
        return tr_matrix
            

class SeqMatrix(Matrix):
    """this class allows to operate matrices based on cols and rows
    number provided, and also based on start value and sequnce step provided"""
    def __init__(self, rows, cols, start, step):
        self.rows = rows
        self.cols = cols
        self.start = start
        self.step = step
        self.matrix = self.build_matrix("str")
        
    def build_matrix(self, mtype):
        matrix = []
        elem = self.start
        for i in range(self.rows):
            matrix.append([])
            for j in range(self.cols):
                if mtype == "str":
                    matrix[i].append(str(elem))
                elif mtype == "num":
                    matrix[i].append(elem)
                elem += self.step
        return matrix
            
                
matrix1 = Matrix(read_matrix(input("Please enter the file name: ")))
matrix2 = SeqMatrix(4, 3, 5, 2)

print("Matrix from file:\n" + str(matrix1))
print("Sequenced matrix:\n" + str(matrix2))
print("Matrix from file transposed:\n" + str(Matrix(matrix1.transpose())))
print("Sequenced matrix transposed:\n" + str(Matrix(matrix2.transpose())))
input('Press any key')
