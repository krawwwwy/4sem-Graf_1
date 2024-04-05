import write
import datetime
start_datetime_a = datetime.datetime.now()


def compare_by_structure(a, b):
    if not a and not b:
        return True
    if not a or not b:
        return False
    return compare_by_structure(a.left, b.left) and compare_by_structure(a.right, b.right)

def find_matching_subtrees(root, target):
    def dfs(node):
        if not node:
            return []
        left_matches = dfs(node.left)
        right_matches = dfs(node.right)
        matches = left_matches + right_matches
        if compare_by_structure(node, target):
            matches.append(node)
        return matches

    return dfs(root)

def read_tree_from_file(filename):
    root = None
    nodes = {}
    with open(filename, 'r') as file:
        for line in file:
            values = line.strip().split()
            parent_value = int(values[0])
            left_value = int(values[1]) if values[1] != "None" else None
            right_value = int(values[2]) if values[2] != 'None' else None
            parent = nodes.get(parent_value, write.TreeNode(parent_value))
            left = nodes.get(left_value, write.TreeNode(left_value)) if left_value is not None else None
            right = nodes.get(right_value, write.TreeNode(right_value)) if right_value is not None else None
            parent.left = left
            parent.right = right
            nodes[parent_value] = parent
            if left_value is not None:
                nodes[left_value] = left
            if right_value is not None:
                nodes[right_value] = right
            if not root:
                root = parent
    return root

# Чтение бинарных деревьев из файлов
main_tree_filename = 'tree_input.txt'
target_tree_filename = 'target_subtree_input.txt'
main_root = read_tree_from_file(main_tree_filename)
target_root = read_tree_from_file(target_tree_filename)

# Находим все поддеревья, структура которых совпадает с заданным
matching_subtrees = find_matching_subtrees(main_root, target_root)

# Выводим результат
for subtree in matching_subtrees:
    print("Matching subtree root value:", subtree.value)
end_datetime_a = datetime.datetime.now()
write.execution_time = write.execution_time + end_datetime_a - start_datetime_a
print(f"Время выполнения: {write.execution_time}")
print(f"Памяти в мегабайтайх на программу : {int(write.tracemalloc.get_traced_memory()[-1]) // 1028**2}")
write.tracemalloc.stop()
