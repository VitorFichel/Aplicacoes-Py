class Node:
    
    def __init__(self, value):
        self.value = value
        self.next = None
        
        
class Node_list:
    
    def __init__(self):
        self.head = None
        
    def add_start(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node
       
    def add_final(self, value):
        new_node = Node(value)
        if not self.head:
            self.head = new_node
            return
        
        current = self.head
        while current.next:
            current = current.next
            
        current.next = new_node
        
    def delete(self, value):
        
        current = self.head
        
        if not current:
            print('a lista nao possui valores')
            return
            
        while value != current.value:
            prev = current
            current = current.next
            
        if not current:
            print("valor nao encontrado")
            return
        
        if current.value == self.head:
            self.head = current.next
            return
            
        prev.next = current.next
        current = None
        
    def search(self, value):
        current = self.head
        
        if not current:
            print('a lista esta vazia')
            return
        
        while current:
            if current.value == value:
                print(f'o valor {value} foi encontrado!')
                return
            current = current.next
            
        print('o valor não foi encontrado')
        
        
    def show(self):
        current = self.head
        while current:
            print(current.value, end=" -> ")
            current = current.next
        print("None")

lista = Node_list()

lista.add_final(1)
lista.add_final(2)
lista.add_final(3)
lista.add_final(4)


lista.delete(2)


lista.show()