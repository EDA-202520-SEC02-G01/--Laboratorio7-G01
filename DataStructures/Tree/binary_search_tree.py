from DataStructures.Tree import bst_node as nd
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    # root is a bst_node or None
    if root is None:
        return 0
    return root.get("size", 0)


def get(my_bst,key):
    return get_node(my_bst["root"],key)

def get_node (node, k):
    if node is None:
        return None
    elif k == node["key"]:
        return node["value"]
    elif k < node["key"]:
        actual = node["left"]
        respuesta = get_node(actual, k)
        return respuesta
    else:
        actual = node["right"]
        respuesta = get_node(actual, k)
        return respuesta
    
def new_map():
    bst={"root":None}
    return bst

def put(bst, key, value):
    bst["root"] = insert_node(bst["root"], key, value)
    return bst

def insert_node(node, key, value):
    if node is None:
        nuevo = nd.new_node(key, value)
        return nuevo
    elif key == node["key"]:
        node["value"] = value
        return node
    elif key < node["key"]:
        node["left"] = insert_node(node["left"], key, value)
    else:
        node["right"] = insert_node(node["right"], key, value)
    node["size"] = size_tree(node["left"]) + size_tree(node["right"]) + 1
    return node

def key_set_tree(root, my_list):
    if root is not None:
        key_set_tree(root["left"], my_list)
        sl.add_last(my_list, root["key"])
        key_set_tree(root["right"], my_list)
    return my_list

def key_set(my_bst):
    if my_bst is None or my_bst.get("root") is None:
        return sl.new_list()
    return key_set_tree(my_bst["root"], sl.new_list())

def is_empty(my_bst):
    return size(my_bst) == 0

def get_min_node(node):
    if node["left"] is None:
        return node
    else:
        return get_min_node(node["left"])
    
def get_min(my_bst):
    if my_bst is None or my_bst["root"] is None:
        return None
    min_node = get_min_node(my_bst["root"])
    if min_node is None:
        return None   
    return (min_node["key"], min_node["value"])

def delete_max_tree(node):
    if node["right"] is None:
        return node["left"]
    node["right"] = delete_max_tree(node["right"])
    node["size"] = size_tree(node["left"]) + size_tree(node["right"]) + 1
    return node

def delete_max(my_bst):
    if my_bst is None or my_bst["root"] is None:
        return my_bst
    my_bst["root"] = delete_max_tree(my_bst["root"])
    return my_bst

def values(my_bst, low_key, high_key):
    if my_bst is None or my_bst["root"] is None:
        return al.new_list()
    result = al.new_list()
    values_range(my_bst["root"], low_key, high_key, result)
    return result

def values_range(node, low_key, high_key, result):
    if node is None:
        return
    if low_key < node["key"]:
        values_range(node["left"], low_key, high_key, result)
    if low_key <= node["key"] <= high_key:
        al.add_last(result, node["value"])
    if high_key > node["key"]:
        values_range(node["right"], low_key, high_key, result)



def get_max_node(root):
    if root is None:
        return None
    while root["right"] is not None:
        root = root["right"]
    return root


def get_max(bst):
    if bst is None or bst["root"] is None:
        return None
    max_node = get_max_node(bst["root"])
    return max_node["key"]

def height_tree(root):
    if root is None:
        return 0
    left_height = height_tree(root["left"])
    right_height = height_tree(root["right"])
    if left_height>right_height:
        return left_height+1
    else:
        return right_height+1


def height(my_bst):
    if my_bst is None or my_bst["root"] is None:
        return 0
    return height_tree(my_bst["root"])
