__author__ = 'victor'

import sys
from cuaderno import Cuaderno,Nota

class Menu:
    """
    Clase objeto que maneja las acciones del menu
    """
    def __init__(self):
        self.cuaderno = Cuaderno()
        self.elecciones = {
            "1": self.mostrar_notas,
            "2": self.search_notas,
            "3": self.add_nota,
            "4": self.modificar_nota,
            "5": self.quit
        }

    def mostrar_menu(self):
        print("""
        Menu Cuaderno

        1.- Mostrar todas las notas
        2.- Buscar Notas
        3.- Nueva nota
        4.- Modificar nota
        5.- Salir
        """)

    def run(self):
        while True:
            self.mostrar_menu()
            seleccion = input("Seleccione una opcion: ")
            accion = self.elecciones.get(seleccion)
            if accion:
                accion()
            else:
                print("{0} no es una opcion valida".format(seleccion))

    def mostrar_notas(self, notas=None):
        if not notas:
            notas = self.cuaderno.notas
        for nota in notas:
            print("{0}: {1}\n{2}".format(nota.id, nota.memo, nota.tags))

    def search_notas(self):
        filtro = input("Escriba un patron de busqueda: ")
        notas = self.cuaderno.search(filtro)
        self.mostrar_notas(notas)

    def add_nota(self):
        memo = input("Escriba memorandum: ")
        tags = []
        while True:
            tag = input("Lista de tags {0} \n Escriba un nuevo tag y pulse intro o intro directamente para guardar: ".
                        format(tags))
            if tag == '':
                break
            tags.append(tag)
        self.cuaderno.nueva_nota(memo, tags)
        print("Nota añadida al cuaderno")

    def modificar_nota(self):
        ident = input("Escriba el id de la nota que desea modificar: ")
        memo = input("Escriba nuevo memo: ")
        tags = input("Escriba nueva lista de tags: ")
        if memo:
            self.cuaderno.modificar_nota(ident, memo)
            print("Memo modificado")
        if tags:
            self.cuaderno.modificar_tags(ident, tags)
            print("tags modificados")

    def quit(self):
        print("Gracias por usar el cuaderno.")
        sys.exit(0)

if __name__ == "__main__":
    Menu().run()


