import time
from tokens import *
from sekuens import *
from tree import *
from randomize import *

def main() :
    choice = input("Input matrix dan sekuens dengan file txt atau generator melalui input CLI? (txt/cli) : ")

    while choice.lower() != "cli" and choice.lower() != "txt" :
        choice = input("Masukan tidak sesuai!\nInput matrix dan sekuens dengan file txt atau generator melalui input CLI? (txt/cli) : ")

    if choice.lower() == "cli" :
        while True:
            try:
                unique_token = int(input("Masukkan jumlah token unik: "))
                if unique_token <= 0:
                    print("Jumlah token unik harus berupa integer positif.")
                    continue 
                break 
            except ValueError:
                print("Input harus berupa bilangan bulat. Coba lagi.")

        tokens_input = []
        print("Masukkan token-token (dipisahkan oleh spasi): ")
        tokens_string = input().strip()
        tokens_list = tokens_string.split()

        while len(tokens_list) != unique_token:
            print("Jumlah token yang dimasukkan tidak sesuai dengan yang diminta.")
            tokens_string = input("Masukkan ulang token-token (dipisahkan oleh spasi): ").strip()
            tokens_list = tokens_string.split()
        
        for a in range (len(tokens_list)):
            while len(tokens_list[a]) != 2 or not is_alphanumeric(tokens_list[a][0]) or not is_alphanumeric(tokens_list[a][1]) :
                tokens_list[a]= input(f"Token harus berupa 2 karakter alfanumerik! Input ulang token ke-{a}: ")
            tokens_input.append(tokens_list[a])

        while True:
            try:
                buffer_size = int(input("Masukkan ukuran buffer: "))
                if buffer_size <= 0:
                    print("Ukuran buffer harus berupa integer positif.")
                    continue 
                break 
            except ValueError:
                print("Input harus berupa bilangan bulat. Coba lagi.")

        while True:
            try:
                matrix_width = int(input("Masukkan lebar matriks: "))
                if matrix_width <= 0:
                    print("Lebar matriks harus berupa integer positif.")
                    continue 
                break 
            except ValueError:
                print("Input harus berupa bilangan bulat. Coba lagi.")

        while True:
            try:
                matrix_height = int(input("Masukkan tinggi matriks: "))
                if matrix_height <= 0:
                    print("Tinggi matriks harus berupa integer positif.")
                    continue 
                break 
            except ValueError:
                print("Input harus berupa bilangan bulat. Coba lagi.")

        while True:
            try:
                sekuens_count = int(input("Masukkan jumlah sekuens yang ingin dibentuk : "))
                if sekuens_count <= 0:
                    print("Jumlah sekuens yang ingin dibentuk  harus berupa integer positif.")
                    continue 
                break 
            except ValueError:
                print("Input harus berupa bilangan bulat. Coba lagi.")
                
        while True:
            try:
                sekuens_size = int(input("Masukkan ukuran maksimal sekuens: "))
                if sekuens_size <= 0:
                    print("Ukuran maksimal sekuens harus berupa integer positif.")
                    continue 
                break 
            except ValueError:
                print("Input harus berupa bilangan bulat. Coba lagi.")

        input_matrix = random_matrix(matrix_height, matrix_width, tokens_input)
        print("Matrix : ")
        for i in range(len(input_matrix)) :
            for j in range(len(input_matrix[i])) :
                print(input_matrix[i][j], end=' ')
            print()

        sekuens_matrix = random_sekuens(sekuens_count, sekuens_size, tokens_input)
        print("Sekuens : ")
        for a in range (len(sekuens_matrix)) :
            print(a+1,". ", sekuens_matrix[a])

        reward_array = []
        print("Reward sekuens : ")
        for i in range(len(sekuens_matrix)) :
            random_value = random.randint(-50,50)
            if i > 0 :
                while (random_value == reward_array[i-1]) : 
                    random_value = random.randint(-50,50)
            reward_array.append(random_value)
        for b in range (len(reward_array)) :
            print(b+1,". ", reward_array[a])

    elif choice.lower() == "txt" :
        input_file = input("Tuliskan nama file : ")

        sekuens_count = 0
        buffer_size = 0

        file_path = r"../test/" + input_file
        with open(file_path, "r") as my_file:
            # your code to read the file
            i = 0 
            for line in my_file:
                i = i + 1
                if i == 1:
                    try:
                        buffer_size = int(line.strip())
                        if buffer_size <= 1:
                            raise ValueError("Input buffer harus berupa bilangan bulat lebih besar dari 1.")
                    except ValueError:
                        print("Input buffer harus berupa bilangan bulat lebih besar dari 1. Coba lagi!")
                        main()
                elif i == 2 :
                    j = 0   
                    status1 = True                
                    while j < len(line.strip()) and line.strip()[j] != " " and status1 :
                        if int(line.strip()[j]) >= 0 :
                            if j == 0 : 
                                matrix_width = line.strip()[j]
                            else : 
                                matrix_width += line.strip()[j]
                            
                        else : 
                            status1 = False
                        j += 1

                    try:
                        matrix_width = int(matrix_width)
                        if matrix_width < 0:
                            raise ValueError("Input lebar matriks harus berupa bilangan bulat lebih besar dari 1.")
                    except ValueError:
                        print("Input lebar matriks harus berupa bilangan bulat. Coba lagi!")
                        main()

                    while j < len(line.strip()) and line.strip()[j] == " " :
                        j += 1

                    k = j
                    status2 = True
                    while j < len(line.strip()) and line.strip()[j] != " " and status2 :
                        if int(line.strip()[j]) >= 0 :
                            if j == k : 
                                matrix_height = line.strip()[j]
                            elif j > k : 
                                matrix_height += line.strip()[j]
                        else : 
                            status2 = False
                        j += 1

                    try:
                        matrix_height = int(matrix_height)
                        if matrix_height < 0:
                            raise ValueError("Input tinggi matriks harus berupa bilangan bulat lebih besar dari 1.")
                    except ValueError:
                        print("Input tinggi matriks harus berupa bilangan bulat. Coba lagi!")
                        main()

                    input_matrix = [["*" for a in range (matrix_width)] for b in range (matrix_height)]
                elif 3 <= i < 3 + matrix_height :
                    try:
                        a = 0
                        while input_matrix[i - 3][matrix_width - 1] == "*" or len(input_matrix[i - 3][matrix_width - 1]) < 2:
                            if line.strip()[a] != " ":
                                if is_alphanumeric(line.strip()[a]) : 
                                    if a % 3 == 0:
                                        input_matrix[i - 3][a // 3] = line.strip()[a]
                                    elif a % 3 == 1:
                                        input_matrix[i - 3][a // 3] = input_matrix[i - 3][a // 3] + line.strip()[a]
                                else :
                                    print("Token dalam matrix bukan karakter alfanumerik! Periksa kembali file input!")
                                    main()
                            a += 1
                    except IndexError:
                        print("Data matriks yang dituliskan dalam file ini tidak dalam keadaan yang ideal (jumlah karakter tidak sesuai ukuran matrix ataupun spasi yang berlebihan antarkarakter)!")
                        print("Mohon cek format file dan ulangi masukan.")
                        main() 

                elif i == 3 + matrix_height :      
                    try:
                        sekuens_count = int(line.strip())
                        if sekuens_count <= 0:
                            raise ValueError("Input banyak sekuens harus berupa bilangan bulat.")
                    except ValueError:
                        print("Input banyak sekuens harus berupa bilangan bulat. Coba lagi!")
                        main()
                    sekuens_matrix = []
                    sekuens_array = []
                    reward_array = [0 for c in range (sekuens_count)]

                elif 3 + matrix_height < i <= 3 + matrix_height + sekuens_count*2:
                    x = i - (4 + matrix_height)
                    if x % 2 == 0 :
                        x = x // 2
                        for y in range(len(line.strip().replace(" ", ""))):
                            if y % 2 == 1 :
                                sekuens_array.append(line.strip().replace(" ", "")[y-1]+line.strip().replace(" ", "")[y])
                        sekuens_matrix.append(sekuens_array)
                        sekuens_array = []
                    else :
                        x = x // 2
                        try:
                            reward_array[x] = int(line.strip())
                        except ValueError:
                            print("Input nilai reward harus berupa bilangan bulat. Coba lagi!")
                            main()

    start_time = time.time()
    tokens = Tokens.instantiate_from_matrix(input_matrix)

    token_matrix = [["" for a in range(matrix_width)] for b in range(matrix_height)]
    for token in tokens:
        i = token.rowposition
        j = token.colposition
        token_matrix[i][j] = token

    trees = create_n_ary_trees(token_matrix, buffer_size)

    route_matrix = []
    paths = []
    for tree in trees : 
        find_all_path(tree, [], paths)
        route_matrix.append(paths)
        paths = []

    sekuens = Sekuens.construct_sekuens(sekuens_matrix, reward_array, buffer_size)

    route_reward_array = sequence_matching(sekuens, route_matrix)

    print()
    output_result = best_route_index(route_reward_array, reward_array, route_matrix)
    print(output_result)

    end_time = time.time()
    runtime_seconds = end_time - start_time
    runtime_ms = runtime_seconds * 1000
    print(f"{runtime_ms:.2f} ms")

    save_to_file = input("Apakah ingin menyimpan solusi? (y/n) : ")
    while save_to_file.lower() != "y" and save_to_file.lower() != "n" :
        save_to_file = input("Masukan tidak sesuai! Apakah ingin menyimpan solusi? (y/n) : ")  

    if save_to_file.lower() == "y":
        file_name = input("Masukkan nama file yang diinginkan : ")
        if not file_name.endswith('.txt'):
            file_name += '.txt'
        try:
            with open('../test/output/' + file_name, 'w') as f:
                f.write(output_result)
                f.write('\n')
                f.write(f"{runtime_ms:.2f} ms")
            print("File berhasil disimpan dengan nama:", file_name)
        except Exception as e:
            print("Terjadi kesalahan saat menyimpan file:", str(e))
    print()
    print("Terima kasih!")
    exit()

if __name__ == "__main__":
    print("   ______      __                                __      ___   ____  __________ ")
    print("  / ____/_  __/ /_  ___  _________  __  ______  / /__   |__ \ / __ \/__  /__  / ")
    print(" / /   / / / / __ \/ _ \/ ___/ __ \/ / / / __ \/ //_/   __/ // / / /  / /  / / ")
    print("/ /___/ /_/ / /_/ /  __/ /  / /_/ / /_/ / / / / ,<     / __// /_/ /  / /  / / ")
    print("\____/\__, /_.___/\___/_/  / .___/\__,_/_/ /_/_/|_|   /____/\____/  /_/  /_/")
    print("    _///__/               /_/  __       ____             __                   __")
    print("   / __ )________  ____ ______/ /_     / __ \_________  / /_____  _________  / /")
    print("  / __  / ___/ _ \/ __ `/ ___/ __ \   / /_/ / ___/ __ \/ __/ __ \/ ___/ __ \/ / ")
    print(" / /_/ / /  /  __/ /_/ / /__/ / / /  / ____/ /  / /_/ / /_/ /_/ / /__/ /_/ / /  ")
    print("/_____/_/   \___/\__,_/\___/_/ /_/  /_/   /_/   \____/\__/\____/\___/\____/_/ ")
    print()
    print("Selamat datang!")
    print()
    main()