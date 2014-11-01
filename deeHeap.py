__author__ = 'Remy Mourard'


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
        on considère que le parent du sommet est le sommet lui même
    '''
    def parent(self, index):
        if index <= self.d:
            parent = 0
        else:
            if index % self.d != 0:
                parent = index // self.d
            else:
                parent = (index // self.d) - 1

        return parent

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
            self.heap.pop(self.length - 1)  # on pop le dernier élément qu'on a mis en haut du tas
            self.length -= 1  # on diminue taille de 1
            self.heap_max(0)

            return max_val

    '''
        augmente valeur d'un noeud (augmenter-clé-tas)
    '''
    def increase_heap_key(self, index, new_val):
        if self.heap[index] > new_val or index > self.length-1:  #
            return None
        else:
            self.heap[index] = new_val
            while index >= 1 and self.heap[self.parent(index)] < self.heap[index]:  # tant que le parent a une valeur inférieure
                self.heap[index], self.heap[self.parent(index)] = self.heap[self.parent(index)], self.heap[index]  # , on permutte
                index = self.parent(index)

    '''
        insere nouvel élément dans le tas (inserer-tas-max())
    '''
    def insert_heap_max(self, value):
        self.length += 1
        self.heap.append(float("-inf"))
        self.increase_heap_key(self.length-1, value)

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

        for i in range(0, zeHeap.length):
            ret_str += "index parent de " + str(self.heap[i]) + " : " + str(self.parent(i)) + "\n"

        return ret_str

    '''
        impression etat
    '''
    def afficher(self):
        print(self)

# tas brut - non construit
zeHeap = DeeHeap([4, 1, 3, 2, 16, 9, 10, 5, 13, 14, 8, 15, 17], 3)
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

# augmente clé élément existant
print("augmentation clé :")
print("heap[4] = 1 --> 11")
zeHeap.increase_heap_key(4, 11)
zeHeap.afficher()

# insère nouvel élément dans le tas
print("insertion nouvel élément dans le tas de valeur 7")
zeHeap.insert_heap_max(7)
zeHeap.afficher()

print("insertion nouvel élément dans le tas de valeur 16")
zeHeap.insert_heap_max(16)
zeHeap.afficher()