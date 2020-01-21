

#Vector class
class Vector:
    def __init__(self, array1D):
        if type(array1D) != list:
            raise Exception("INPUT MUST BE A LIST OF INTEGERS")
        for i in array1D:
            if type(i) != int:
                raise Exception("INPUT MUST BE A LIST OF INTEGERS")
        self.values = array1D

    def __repr__(self):
        out = ""
        for i in self.values:
            out += "[" + str(i) + "]\n"
        return out[:-1]

    def __mul__(self, other):
        if type(other) == int:
            res = []
            for i in self.values:
                res += [i * other]
            return Vector(res)
        else:
            raise Exception("OPERAND MUST BE INTEGER")

    def __len__(self):
        return len(self.values)

    def __getitem__(self, key):
        return self.values[key]

    def dot(self, other):
        """returns the dot product of two vectors"""
        if type(self) != type(other):
            raise Exception("OPERAND MUST BE VECTOR")
        if len(self) != len(other):
            raise Exception("VECTORS MUST BE OF EQUAL DIMENSION")
        res = 0
        for i in range(len(self)):
            res += self[i] * other[i]
        return res
        
        
        



#Matrix class
class Matrix:
    
    def __init__(self, array2D):
        for i in range(len(array2D)):
            if len (array2D[i]) != len(array2D[0]):
                raise Exception('INVALID MATRIX')
        self.values = array2D

    #override to-string method
    def __repr__(self):
        out = ""
        for i in self.values:
            out += str(i) + "\n"
        return out[0:-1]

    #override A * B operator
    def __mul__(self, other):
        res = []
        #for scalar multiplication
        if type(other) == 'int':
            for i in range(len(self.values)):
                res += [[]]
                for j in range(len(self.values[i])):
                    res[i] += [self.values[i][j] * 2]
            return res
        #for matrix multiplication
        if type(self) == type(other):
            if self.numCols() != other.numRows():
                raise Exception("INVALID METRIX DIMENSIONS")
            res = []
            for i in range(self.numRows()):
                res += [[]]
            for i in range(self.numRows()):
                for j in range(other.numCols()):
                    res[i] += [Vector(self[i]).dot(Vector(other.T()[j]))]

            return Matrix(res)
                

    __rmul__ = __mul__

    def __getitem__(self, key):
        return self.values[key]

    def __setitem__(self, key, value):
        self.values[key] = value
    
    def transpose(self):
        """returns the transpose matrix"""
        return Matrix(self.getCols())
    
    T = transpose

    def getRows(self):
        """returns list of rows"""
        return self.values

    def getCols(self):
        """returns list of columns"""
        res = []
        for i in range(self.numCols()):
            res += [[]]
        for i in range(self.numRows()):
            for j in range(self.numCols()):
                res[j] += [self.values[i][j]]
        return res

    def numRows(self):
        return len(self.values)

    def numCols(self):
        return len(self.values[0])



        




    
a = Vector([1, 2, 3])
b = Vector([10, 20, 30])

#A = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#B = Matrix([[10, 20, 30], [40, 50, 60], [70, 80, 90]])
A = Matrix([[1, 4], [2, 5], [3, 6]])
B = Matrix([[10, 20, 30], [40, 50, 60]])
























































