from DataStructures.Tree import bst_node as nd
from DataStructures.List import single_linked_list as sl


def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    if root==None:
        return 0
    elif root["left"]==None and root["right"]==None:
        return 1
    elif root["left"]!= None and root["right"]!= None:
        return 1+size_tree(root["left"])+size_tree(root["right"])
    elif root["left"]!= None and root["right"]== None:
        return 1+size_tree(root["left"])
    elif root["left"]== None and root["right"]!= None:
        return 1+size_tree(root["right"])
        

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

def contains(my_bst, key):
    if get(my_bst,key):
        return True
    else:
        return False

def value_set(my_bst):
    lista=sl.new_list()
    value_set_tree(my_bst["root"], lista)
    return lista

def value_set_tree(root, key_list):
    if root!=None:
        value_set_tree(root["left"], key_list)

        sl.add_last(key_list, root["value"])

        value_set_tree(root["right"], key_list)
        
def delete_min(my_bst):
    if my_bst["root"]!=None:
        my_bst["root"]=delete_min_tree(my_bst["root"])   
    return my_bst

def delete_min_tree(root):
    if root["left"]==None:
        return root["right"]
    root["left"] = delete_min_tree(root["left"])
    root["size"] = size_tree(root["left"]) + size_tree(root["right"]) + 1
    return root
    
def keys(my_bst, key_initial, key_final):
    lista=sl.new_list()
    keys_range(my_bst["root"],key_initial,key_final,lista)
    return lista
    
def keys_range(root, key_initial, key_final, list_key):
    if root == None:
        return 
    if root["key"] > key_initial:
        keys_range(root["left"], key_initial, key_final, list_key)
    if key_initial <= root["key"] <= key_final:
        sl.add_last(list_key, root["key"])
    if root["key"] < key_final:
        keys_range(root["right"], key_initial, key_final, list_key)
    