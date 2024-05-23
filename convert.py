import json


class TreeNode:
    def __init__(self, id, val, left=None, right=None):
        self.id = id
        self.val = val
        self.left = left
        self.right = right


def build_tree(nodes):
    node_dict = {node['id']: TreeNode(node['id'], node['val']) for node in nodes}

    for node in nodes:
        if node['left'] is not None:
            node_dict[node['id']].left = node_dict[node['left']]
        if node['right'] is not None:
            node_dict[node['id']].right = node_dict[node['right']]

    return node_dict[0]  # assuming the root node has id 0


def serialize(node):
    if node is None:
        return None
    return {
        "id": node.id,
        "val": node.val,
        "left": serialize(node.left),
        "right": serialize(node.right)
    }


def con():
    nodes = []
    print("Введите узлы дерева в формате: id val left right (где left и right - id дочерних узлов или 'None'):")
    while True:
        line = input("Введите узел (или оставьте строку пустой для завершения ввода): ").strip()
        if not line:
            break
        id, val, left, right = line.split()
        id = int(id)
        val = int(val)
        left = int(left) if left != 'None' else None
        right = int(right) if right != 'None' else None
        left, right = right, left
        nodes.append({"id": id, "val": val, "left": left, "right": right})

    root = build_tree(nodes)
    tree_json = serialize(root)
    with open("tree.json", "w", encoding="utf-8") as f:
        json.dump(tree_json, f, ensure_ascii=False, indent=4)
    print("Дерево сохранено в tree.json")


con()
