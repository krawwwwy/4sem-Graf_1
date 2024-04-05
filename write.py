import random
import datetime
import tracemalloc

start_datetime = datetime.datetime.now()
tracemalloc.start()

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def generate_random_binary_tree(size):
    if size == 0:
        return None

    left_size = random.randint(0, size - 1)
    right_size = size - 1 - left_size

    left_subtree = generate_random_binary_tree(left_size)
    right_subtree = generate_random_binary_tree(right_size)
    root = TreeNode(random.randint(0, 100000000))
    root.left = left_subtree
    root.right = right_subtree

    return root

def write_tree_to_file(root, filename):
    with open(filename, 'w') as file:
        def dfs(node):
            if not node:
                return
            file.write(f"{node.value} ")
            if node.left:
                file.write(f"{node.left.value} ")
            else:
                file.write("None ")
            if node.right:
                file.write(f"{node.right.value}\n")
            else:
                file.write("None\n")
            dfs(node.left)
            dfs(node.right)

        dfs(root)

# Пример использования
tree_size = int(input("Введите размер дерева "))
target_tree_size = int(input("Введите размер заданной структуры дерева "))
random_tree_root = generate_random_binary_tree(tree_size)
write_tree_to_file(random_tree_root, 'tree_input.txt')
random_tree_root = generate_random_binary_tree(target_tree_size)
write_tree_to_file(random_tree_root, 'target_subtree_input.txt')
end_datetime = datetime.datetime.now()
execution_time = end_datetime - start_datetime
