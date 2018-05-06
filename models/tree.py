#Estrutura para a árvore que será usada na Busca Gulosa.

class Tree():

    #Método construtor
    def __init__(self, id, name = None, value = 0, children = None, parent = None):
        self.id = id          #O id contido nos arquivos
        self.name = name      #O nome do pesquisador escreveu o artigo
        self.value = value    #O valor da heurística para esse nó
        self.hSum = 0         #A soma das heurísticas da raiz até esse nó
        self.parent = parent  #O nó pai deste nó
        self.children = []    #Uma lista contendo os filhos deste nó
        self.visited = False  #Flag utilizada na função "dfs_tree()"

    def set_node_by_vertex(self,vertex, parent):
        self.id = vertex.id          #O id contido nos arquivos
        self.name = vertex.name      #O nome do pesquisador escreveu o artigo
        self.value = vertex.value    #O valor da heurística para esse nó
        self.hSum = 0         #A soma das heurísticas da raiz até esse nó
        self.parent = parent  #O nó pai deste nó
        self.children = []    #Uma lista contendo os filhos deste nó
        self.visited = False  #Flag utilizada na função "dfs_tree()"        
        
    def find_child(self, id):
        for node in self.children:
            if (node.id == id):
                return node
            else:
                return None

    #Adiciona um filho ao nó
    #Toda vez que um filho é adicionado na árvore,
    #o valor total de sua heurística é o seu valor mais o de seu pai.
    def add_child(self, id, name, value):
        child = dfs_tree(tree,id)
        if not(child):
            child = Tree(id,name,value,None,self)
            child.hSum = self.hSum + value
            self.children.append(child)
            return child
        else:
            print("Nó já existe na árvore")
            return None


    #Remove um filho da árvore a partir do seu id.
    #Caso deseje remover um nó da árvore chame este método
    #para self.parent passando como parâmetro o id do nó desejado
    #mas note que ele removerá todos os filhos dele também.
    def remove_child(self, id):
        for node in self.children:
            if (node.id == id):
                return self.children.remove(child)
            else:
                print("Esse filho não existe")
                return None

    #Métodos get auxiliares
    def get_id(self):
        return self.id

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent

    def set_id(self,id):
        self.id = id

    def set_name(self, name):
        self.name = name

    def set_value(self, value):
        self.value = value

    def set_children(self, children):
        self.children = children

    def set_parent(self, parent):
        self.parent = parent

#Limpa todas as visitas anteriores em uma árvore.
#Para ser usado na raiz da árvore.
def clear_tree(tree):
    if tree is not(None):
        tree.visited = False
        for node in tree.children:
            clearing = clear_tree(node)
        return

#Método que busca um nó com determinada id em uma árvore.
def search(tree,id):
    if tree is not(None):
        #Checa se já visitou esse nó para evitar repetições no loop abaixo
        tree.visited = True

        #Achou o nó, retorna-o
        if tree.id == id:
            return tree

        #Para cada filho não visitado, procura re
        for child in tree.children:
            if not(child.visited):
                node = search(child,id)
                if (node):
                    return node
    else:
        return None

#Limpa a árvore e chama search()
def dfs_tree(tree, id):
    clear_tree(tree)
    node = search(tree,id)
    return node