from DataStructures.Tree import bst_node as nd
from DataStructures.List import array_list as al
from DataStructures.List import single_linked_list as sl

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    size=root["size"]
    return size

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

def put(bst,key,value):
    bst["root"]=insert_node(bst["root"],key,value)

def insert_node(node,key,value):
    if node is None:
        nuevo=nd.new_node(key,value)
        return nuevo
    elif key == node["key"]:
        node["value"]=value
        return node
    elif key < node["key"]:
        actual=node["left"]
        node["left"]=insert_node(actual,key,value)
        node["size"]=size_tree(node["left"])+size_tree(node["right"])+1
        return node
    else:
        actual=node["right"]
        node["right"]=insert_node(actual,key,value)
        node["size"]=size_tree(node["left"])+size_tree(node["right"])+1

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