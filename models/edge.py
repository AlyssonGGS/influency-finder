class Edge():
    
    def __init__(self, destiny = None, cost = None):
        self.destiny = destiny
        self.cost = cost
    
    def get_destiny_value(self):
        return self.destiny.value

