class TreeNode:
    def __init__(self, info):
        self.info = info
        self.children = []

def create_n_ary_trees(matrix, depth):
    trees = []
    for root_info in matrix[0]:
        root = TreeNode(root_info)
        construct_tree(matrix, root, depth, 1)
        trees.append(root)
    return trees

def construct_tree(matrix, node, depth, level):
    if level >= depth:
        return
    if level % 2 == 1:  # Pergerakan vertikal
        col_idx = None

        for i, row in enumerate(matrix): 
            if node.info in row:
                col_idx = row.index(node.info)
                break
        
        if col_idx is not None:
            for row_idx, row in enumerate(matrix):
                if row_idx != i:  
                    child_info = row[col_idx] 
                    child_node = TreeNode(child_info) 
                    node.children.append(child_node)
                    construct_tree(matrix, child_node, depth, level + 1)

    else:  # Pergerakan horizontal
        col_idx_found = None
        for i, row_found in enumerate(matrix): 
            if node.info in row_found:
                col_idx_found = row_found.index(node.info)
                break

        for row_idx, row in enumerate(matrix):
            if node.info in row: 
                for col_idx, info in enumerate(row):
                    if col_idx != col_idx_found : 
                        child_info = matrix[row_idx][col_idx] 
                        child_node = TreeNode(child_info)
                        node.children.append(child_node)
                        construct_tree(matrix, child_node, depth, level + 1)

# Mencari seluruh kemungkinan lintasan token dari tree yang telah tersusun
def find_all_path(root, path=[], result=[]):
    # Jika sudah mencapai leaf, return
    if root is None:
        return
    
    # Hanya menambahkan node yang belum masuk ke dalam susunan token sebagai lintasan 
    if root.info.isSelected == False : 
        path.append(root.info)
        root.info.isSelected = True

        # Menambahkan semua kemungkinan jalur dengan ketentukan sebuah lintasan terdiri dari minimal 2 karakter alfanumerik sesuai spesifikasi
        if len(path) > 1 :
            result.append(path[:])
        
        # Melakukan rekursi untuk semua child dari node saat ini
        for child in root.children:
            find_all_path(child, path, result)
    
        # Backtracking dengan popping elemen terakhir
        path[len(path)-1].isSelected = False
        path.pop()
    else : 
        return