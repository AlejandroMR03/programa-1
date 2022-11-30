from Linked import linked_list
from os import system



class menu:
    def __init__(self,linked_list):

        self.linked_list = linked_list



    def menu_principal(self):
        system('cls')
        print(" Menu Alejandro")
        print("1 = Digitar nodo")
        print("2 = salir")

    while True:

        resp = (int(input("Digite la opcion: ")))

        if resp == 1:
            print("su nodo es",resp)
            input()

        if resp == 2:
            break

        else:
            print("opción no existe")


        
        