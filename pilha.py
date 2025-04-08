# classe que define um nó
class Node:

    def __init__(self, value):
        self.value = value
        self.ant = None

# classe que define a pilha 
class Pilha:
    # Método que define o inicio/head
    def __init__(self):
        self.topo = None

    # Método que mostra quantos elementos tem na pilha
    def tam(self):
      atual = self.topo
      cont = 0
      while atual is not None:
        cont += 1
        atual = atual.ant
      return cont

    # Método que mostra os elementos da pilha
    def display(self):
      atual = self.topo
      lista = []
      while atual is not None:
        lista.append(atual.value)
        atual = atual.ant
      print(lista)

    # Método que coloca um novo elemento na pilha
    def push(self, value):
        novo = Node(value)

        if not self.topo:
            self.topo = novo
            return

        novo.ant = self.topo
        self.topo = novo

    # Método que retira o elemento do topo elemento da pilha
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

pilha_de_frutas.display()

pilha_de_frutas.pop()

cont = pilha_de_frutas.tam()
print(cont)

pilha_de_frutas.display()

