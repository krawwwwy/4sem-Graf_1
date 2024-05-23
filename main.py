import json
import random
from anytree import Node, RenderTree, AsciiStyle
import time

class TreeNode:
    def __init__(self, id, val=0, left=None, right=None):
        self.id = id
        self.val = val
        self.left = left
        self.right = right


def generate_random_tree_with_nodes(num_nodes):
    if num_nodes == 0:
        return None

    values = [(i, random.randint(1, 10) if random.random() > 0.1 else None) for i in range(num_nodes)]
    values[0] = (0, random.randint(1, 10))  # Root node must be non-null

    def build_tree(index):
        if index >= num_nodes or values[index][1] is None:
            return None
        node = TreeNode(values[index][0], values[index][1])
        left_index = 2 * index + 1
        right_index = 2 * index + 2
        if left_index < num_nodes:
            node.left = build_tree(left_index)
        if right_index < num_nodes:
            node.right = build_tree(right_index)
        return node

    return build_tree(0)


def tree_to_dict(root):
    if not root:
        return None
    return {
        'id': root.id,
        'val': root.val,
        'left': tree_to_dict(root.left),
        'right': tree_to_dict(root.right)
    }


def generate_input_files(num_main_nodes, num_sub_nodes):
    main_tree = generate_random_tree_with_nodes(num_main_nodes)
    subtree = generate_random_tree_with_nodes(num_sub_nodes)

    with open('main_tree.json', 'w') as f:
        json.dump(tree_to_dict(main_tree), f)

    with open('subtree.json', 'w') as f:
        json.dump(tree_to_dict(subtree), f)


def read_tree_from_file(filename):
    with open(filename, 'r') as f:
        tree_dict = json.load(f)
    return dict_to_tree(tree_dict)


def dict_to_tree(tree_dict):
    if not tree_dict:
        return None
    root = TreeNode(tree_dict['id'], tree_dict['val'])
    root.left = dict_to_tree(tree_dict.get('left'))
    root.right = dict_to_tree(tree_dict.get('right'))
    return root


def is_same_structure(s, t):
    if not s and not t:
        return True
    if not s or not t:
        return False
    return is_same_structure(s.left, t.left) and is_same_structure(s.right, t.right)


def find_subtree_structure(root, subtree):
    result = []

    def traverse(node):
        if not node:
            return
        if is_same_structure(node, subtree):
            result.append(node)
        traverse(node.left)
        traverse(node.right)

    traverse(root)
    return result


def build_anytree(root, parent=None):
    if not root:
        return None
    node = Node(str(root.val), parent=parent)  # Используем значения узлов для вывода
    if root.left:
        build_anytree(root.left, parent=node)
    if root.right:
        build_anytree(root.right, parent=node)
    return node


def print_tree(root):
    anytree_root = build_anytree(root)
    if anytree_root:
        for pre, fill, node in RenderTree(anytree_root):
            print("%s%s" % (pre, node.name))
    else:
        print("Empty tree")


# Основная часть программы
if __name__ == "__main__":
    num_main_nodes = int(input("Введите количество узлов в основном дереве: "))  # Количество узлов в основном дереве
    num_sub_nodes = int(input("Введите количество узлов в поддереве: ")) # Количество узлов в поддереве
    start = time.time()


    #generate_input_files(num_main_nodes, num_sub_nodes)

    main_tree = read_tree_from_file('main_tree.json')
    subtree = read_tree_from_file('subtree.json')

    print("Main Tree:")
    print_tree(main_tree)

    print("\nSubtree:")
    print_tree(subtree)

    matches = find_subtree_structure(main_tree, subtree)
    print("\nFound Subtrees:")
    for i, match in enumerate(matches, 1):
        print(f"\nMatch {i}:")
        print_tree(match)

    end = time.time()
    print()
    print('Time: ', end - start)
