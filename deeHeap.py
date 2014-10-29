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
        formule
    '''
    def parent(self, index):
        if index <= 0 or index-self.d <= 0:
            return 0
        else:
            x = index % self.d


    '''
        retourne la valeur du tas et
        conserve la propriété de tas max (extraire-max-tas())
    '''
    def extract_heap_max(self):
        if self.length < 0:
            return None
        else:
            max_val = self.heap[0]
            self.heap[0] = self.heap[self.length - 1]  # on met une valeur basse en haut du tas
            self.length -= 1  # on diminue taille de 1
            self.heap.pop(self.length - 1)  # et on pop le dernier élément qu'on a mis en haut du tas
            self.heap_max(0)

            return max_val

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

    '''
        afficher le tableau directement
        en faisant des print() sur objet tas
    '''
    def __str__(self):
        ret_str = "longueur du tas : " + str(self.length)
        ret_str += "\ntas-d : " + str(self.d)
        ret_str += "\n["
        for i in range(0, self.length, 1):
            ret_str += str(self.heap[i]) + ", "

        ret_str = ret_str.rstrip(', ') + "]\n"
        return ret_str

    '''
        impression etat
    '''
    def afficher(self):
        print(self)

# tas brut - non construit
zeHeap = DeeHeap([4, 1, 3, 2, 16, 9, 10, 14, 8, 7], 3)
print("tas non construit :")
zeHeap.afficher()

# construction du tas
zeHeap.build_heap()
print("tas construit :")
zeHeap.afficher()

# extraction tas max
print("extraction max :")
maxVal = zeHeap.extract_heap_max()
print(maxVal)
zeHeap.afficher()

# insere nouvel élément
print("parent de 1 : " + str(zeHeap.parent(1)))
print("parent de 2 : " + str(zeHeap.parent(2)))
print("parent de 3 : " + str(zeHeap.parent(3)))
print("parent de 4 : " + str(zeHeap.parent(4)))
print("parent de 5 : " + str(zeHeap.parent(5)))
print("parent de 6 : " + str(zeHeap.parent(6)))
print("parent de 7 : " + str(zeHeap.parent(7)))
print("parent de 8 : " + str(zeHeap.parent(8)))