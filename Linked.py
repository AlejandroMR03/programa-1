from archivo import lines
# Creamos la clase node
class node:
    def __init__(self, data = None, next = None):
        self.data = data
        self.next = next

# Creamos la clase linked_list
class linked_list: 
    def __init__(self):
        self.head = None
    
    # Método para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = node(data=data, next=self.head)  

    # Método para verificar si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None

    # Método para agregar elementos al final de la linked list
    def add_at_end(self, data):
        if not self.head:
            self.head = node(data=data)
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node(data=data)
    
    # Método para eleminar nodos
    def delete_node(self, key):
        curr = self.head
        prev = None
        while curr and curr.data != key:
            prev = curr
            curr = curr.next
        if prev is None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None

    # Método para obtener el ultimo nodo
    def get_last_node(self):
        temp = self.head
        while(temp.next is not None):
            temp = temp.next
        return temp.data

    # Método para imprimir la lista de nodos
    def print_list( self ):
        node = self.head
        while node != None:
            print(node.data, end =" => ")
            node = node.next
    
    def mostrar_lista( self ):
        node = self.head #node será la cabeza
        while node != None: #mientras node sea diferente a nada
            print(node.data, end =" => ") #se mostrarán los nodes
            #end = para que me muesre enseguida el proximo node
            node = node.next #y node será el siguiente

    

    def enlazada_txt(self):
            nume = lines
            s = linked_list()
            print(lines)
            
            lista = []
            v = 0
            for i in range(len(nume)):
                
                lista.append(i)
                v = nume[i]
                s.mostrar_lista(v)

           

              
s = linked_list() # Instancia de la clase
            
a = float(input("digite un numero para agregar a la lista enblazada: "))
                        

s.add_at_front(a) # Agregamos un elemento al frente del nodo
s.add_at_end(8) # Agregamos un elemento al final del nodo
s.add_at_front(9) # Agregamos otro elemento al frente del nodo
s.print_list() # Imprimimos la lista de nodos 
 


