class Matrix:
    def __init__(self, matrix):
        self.matrix = matrix

    def __str__(self):
        my_str = ""
        for el in self.matrix:
            for ind in range(len(el)):
                my_str += " " + str(el[ind])
            my_str += "\n"
        return f"{my_str}"

    def __add__(self, other):
        my_list = []
        new_matrix = []
        ind = 0
        for ind_i, el in enumerate(self.matrix):
            for ind in range(len(el)):
                my_list.insert(ind, float(self.matrix[ind_i][ind]) + float(other.matrix[ind_i][ind]))
            new_matrix.insert(ind, my_list)
            my_list = []
        return Matrix(new_matrix)


try:
    mc_1 = Matrix([[31, 22, 44], [37, 43, 54], [51, 86, 32]])
    mc_2 = Matrix([[31, 22, 44], [37, 43, 54], [51, 86, 32]])
    mc_3 = Matrix([[31, 22, 44], [51, 86, 32], [51, 86, 32]])
    mc_4 = Matrix([[31, 22, 44], [37, 43, 54], [51, 86, 32]])
    print(mc_1 + mc_2 + mc_3 + mc_4)
except IndexError as error:
    print(f"The matrix has no same ranges: {error}")
