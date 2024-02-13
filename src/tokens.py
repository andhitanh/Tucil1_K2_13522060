class Tokens:
    def __init__(self, alphanumeric: str, colposition: int, rowposition : int, isSelected: bool = False):
        self.alphanumeric = alphanumeric
        self.colposition = colposition
        self.rowposition = rowposition
        self.isSelected = isSelected
    
    @classmethod
    def instantiate_from_matrix(cls, matrix):
        tokens_list = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                alphanumeric = matrix[i][j]
                colposition = j
                rowposition = i
                token = cls(alphanumeric, colposition, rowposition)
                tokens_list.append(token)
        return tokens_list

def is_alphanumeric(char):
    return (48 <= ord(char) <= 57) or (65 <= ord(char) <= 90) or (97 <= ord(char) <= 122)
