__author__ = 'Victor Nieto'

import datetime

ultima_id = 0

class Nota:
    """
    Representa una nota en el cuaderno. Se compara con un string en las busquedas y las etiquetas por cada nota
    """

    def __init__(self, memo, tags=''):
        """
        Metodo constructor de la clase Nota
        """

        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()

        global ultima_id
        ultima_id += 1
        self.id = ultima_id

    def match(self, filtro):
        """
        Determina si esta nota concuerda con el filtro de texto. Devuelve True si concuerda y False en caso contrario
        """
        return filtro in self.memo or filtro in self.tags

class Cuaderno:
    """
    Representa un conjunto de notas que en su totalidad forman a la clase cuaderno. Pueden ser etiquetadas,
    modificadas y buscadas.
    """

    def __init__(self):
        """
        Inicializa el cuaderno como una lista vacia
        """

        self.notas = []

    def nueva_nota(self, memo, tags=''):
        """
        Crea nota nueva y la inserta al cuaderno
        :param memo: Contenido de la nota
        :param tags: Tags de la nota
        """
        nota = Nota(memo, tags)
        self.notas.append(nota)

    def modificar_nota(self, nota_id, memo):
        """
        Modifica el contenido de una nota del cuaderno
        :param nota_id: id de la nota a modificar
        :param memo: nuevo contenido de la nota
        :return: True si modifico y false si el id no existe
        """
        nota = self._encontrar_nota(nota_id)
        if nota:
            nota.memo = memo
            return True
        return False

    def modificar_tags(self, nota_id, tags):
        """
        Modifica la lista de tags adjunta a la nota
        """
        nota = self._encontrar_nota(nota_id)
        if nota:
            nota.tags = tags
            return True
        return False

    def search(self, filtro):
        """
        Busqueda de notas a partir de una cadena
        :param filtro: patron de busqueda
        :return: lista de notas que coinciden con el patron de busqueda
        """
        return [nota for nota in self.notas if nota.match(filtro)]

    def _encontrar_nota(self, nota_id):
        """
        Busca nota por id
        :param nota_id: ID de la nota a buscar
        :return: nota
        """
        for nota in self.notas:
            if nota.id == nota_id:
                return nota
        return None


