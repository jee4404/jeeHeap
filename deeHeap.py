__author__ = 'Remy'


class DeeHeap:
    """
        constructeur - le tas est indexé à partir de
        zéro contrairement au tas binaire indexé à partir de 1
        a = tableau a convertir en tas
        d = nombre d'enfants max par noeud
    """
    def __init__(self, a, d):
        self.heap = a
        self.d = d
        self.length = len(a)

    '''
        construction d'un tas à la façon construire-tas-max binaire
    '''
    def build_heap(self):
        start_index = (self.length - 1) // self.d
        print("start index ", start_index)
        for index in range(start_index, -1, -1):  # attention range() exclue toujours la derniere valeur conditionnelle
            self.heap_max(index)

    '''
        verifie la propriétée de tas pour l'index
        passé (équivalent entasser-max())
    '''
    def heap_max(self, index):
        max_index = index  # on assume que la propriété de tas est respectée
        children_list = self.children(index)
        for i in children_list:
            if self.heap[i] > self.heap[max_index]:
                max_index = i

        if max_index != index:
            self.heap[max_index], self.heap[index] = self.heap[index], self.heap[max_index]
            self.heap_max(max_index)

    '''
        retourne les enfants du noeud passé en index
        sous forme de range(index premier enfants, index dernier enfant)
    '''
    def children(self, index):
        last_child = 0
        for i in range(1, self.d+1):
            if (self.d * index) + i < self.length:  # ajoute l'index seulement si ne dépasse pas la taille du tas
                last_child = (self.d * index) + i

        if last_child != 0:
            last_child += 1

        first_child = (self.d * index) + 1
        if first_child > (self.length-1):
            first_child = 0

        return range(first_child, last_child, 1)

    '''
        retourne le parent du noeud passé en index
    '''
    def parent(self, index):
        if index <= self.d:
            return 0
        else:
            return float("inf")

    '''
        retourne la valeur du tas et
        conserve la propriété de tas max (extraire-max-tas())
    '''
    def extract_heap_max(self):
        return None

    '''
        insere nouvel élément dans le tas (inserer-tas-max())
    '''
    def insert_heap_max(self):
        return None

    '''
        augmente valeur d'un noeud (augmenter-clé-tas)
    '''
    def increase_heap_key(self):
        return None

zeHeap = DeeHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7], 4)

print(zeHeap.heap)

zeHeap.build_heap()

print(zeHeap.heap)