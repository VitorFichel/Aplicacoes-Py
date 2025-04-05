class Node:
    
    def __init__(self, value):
        self.value = value
        self.ant = None
        
class Pilha:
    
    def __init__(self):
        self.topo = None
        
    def push(self, value):
        novo = Node(value)
        
        if not self.topo:
            self.topo = novo
            return
        
        novo.ant = self.topo
        self.topo = novo
        
    def pop(self):
        
        if not self.topo:
            print('não há vnenhum valor na pilha')
            return
            
        
        removido = self.topo
        self.topo = removido.ant
        removido = removido.value
        print(f'valor "{removido}" removido da pilha')
        
        
pilha_de_frutas = Pilha()

pilha_de_frutas.push('laranja')
pilha_de_frutas.push('banana')
pilha_de_frutas.push('melancia')
pilha_de_frutas.push('maçã')

pilha_de_frutas.pop()