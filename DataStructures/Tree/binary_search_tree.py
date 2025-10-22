from DataStructures.Tree import bst_node as nd

def size(my_bst):
    return size_tree(my_bst["root"])

def size_tree(root):
    if root["left"]==None and root["right"]==None:
        return 1
    elif root["left"]!= None and root["right"]!= None:
        return 1+size_tree(root["left"])+size_tree(root["right"])
    elif root["left"]!= None and root["right"]== None:
        return 1+size_tree(root["left"])
    elif root["left"]== None and root["right"]!= None:
        return 1+size_tree(root["right"])
    elif root==None:
        return 0

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