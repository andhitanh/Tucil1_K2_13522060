import random

def random_matrix(height, width, tokens) :
    matrix = []
    for i in range(height) : 
        row =  [random.choice(tokens) for j in range (width)]
        matrix.append(row)
    return matrix

def random_sekuens(sekuens_count, sekuens_size, tokens):
    sekuens = []
    for i in range(sekuens_count):
        row = [random.choice(tokens) for j in range(random.randint(2, sekuens_size))]
        sekuens.append(row)
    return sekuens