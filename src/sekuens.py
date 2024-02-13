class Sekuens: 
    def __init__(self, sekuens, reward):
        self.sekuens = sekuens
        self.reward = reward
    
    @classmethod
    def construct_sekuens(cls, sekuens_matrix, reward_array, buffer_size):
        result_matrix = []
        for i in range(len(sekuens_matrix)):
            if len(sekuens_matrix[i]) <= buffer_size:
                result_matrix.append(cls(sekuens_matrix[i], reward_array[i]))
        return result_matrix

def is_match (array_sequence, array_token) :
    i = 0
    j = 0
    if len(array_sequence.sekuens) <= len(array_token) :
            while i < len(array_token) and j < len(array_sequence.sekuens) :
                if array_token[i].alphanumeric == array_sequence.sekuens[j] :
                   i += 1
                   j += 1
                else : 
                    if i > 0 and j > 0 and array_token[i-1].alphanumeric == array_sequence.sekuens[j-1] :
                        j = 0
                    elif j == 0 :
                        i += 1

            if (j == len(array_sequence.sekuens)) :
                return True
            else :
                return False
    else : 
        return False

def sequence_matching(sequence_matrix, route_matrix) :
    j = 0
    totalreward_array = [[0 for a in range (len(route_matrix[b]))] for b in range (len(route_matrix))]
    while j < len(sequence_matrix) :
        i = 0
        while i < len(route_matrix) :
            k = 0
            while k < len(route_matrix[i]) :
                if is_match(sequence_matrix[j], route_matrix[i][k]) :
                    totalreward_array[i][k] += sequence_matrix[j].reward
                k += 1
            i += 1
        j += 1
    return totalreward_array

def all_zero(matrix):
    for i in range (len(matrix)):
        for j in range (len(matrix[i])):
            if matrix[i][j] != 0:
                return False
    return True

def all_positive(array) : 
    for i in range (len(array)) :
        if array[i] <= 0 :
            return False
    return True

def all_negative(array) : 
    for i in range (len(array)) :
        if array[i] >= 0 :
            return False
    return True

def best_route_index(totalreward_array, reward_array, route_matrix):
    if all_zero(totalreward_array) and all_positive(reward_array) :
        output_string = "Tidak ditemukan kecocokkan pola dengan sekuens!\n"
    elif all_zero(totalreward_array) and all_negative(reward_array) :
        output_string = "Tidak ditemukan kecocokkan pola dengan sekuens!\n"
    else :
        i = 0
        j = 0
        max_reward = totalreward_array[0][0]
        a = 0
        b = 0
        while i < len(totalreward_array):
            j = 0
            while j < len(totalreward_array[i]):
                if max_reward < totalreward_array[i][j]:
                    max_reward = totalreward_array[i][j]
                    a = i
                    b = j
                elif max_reward == totalreward_array[i][j] and len(route_matrix[a][b]) > len(route_matrix[i][j]) :
                    max_reward = totalreward_array[i][j]
                    a = i
                    b = j
                j += 1
            i += 1

        output_string = f"{max_reward}\n"
        for x in range(len(route_matrix[a][b])):
            output_string += route_matrix[a][b][x].alphanumeric + " "
        output_string += "\n"
        for y in range(len(route_matrix[a][b])):
            output_string += f"{route_matrix[a][b][y].colposition + 1},{route_matrix[a][b][y].rowposition + 1}\n"

    return output_string