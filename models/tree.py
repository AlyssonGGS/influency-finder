
class Tree():
    #mais algum atributo? atributo a menos?
    def __init__(self, name = None, value = None, parent = None):
        self.name = name
        self.value = value
        self.parent = parent
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    #remover pelo nome ou pelo valor?
    def remove_child(self, child_name):
        self.children.remove(child_name)

    def get_name(self):
        return self.name

    def get_value(self):
        return self.value

    def get_children(self):
        return self.children

    def get_parent(self):
        return self.parent
