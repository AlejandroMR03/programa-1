#se crea una clase lista
from typing import Self
from programa import Node


class lista:
    def __init__(self):
      Self.head = None
    
    #se agrega un metodo para agregar nuevos elementos a la lista
    def add_at_front(self,data):
        self.head = Node(data=data, next=self.head)
        
    #se mira si la estructura de datos esta vacia
    def is_empty(self):
        return self.head == None