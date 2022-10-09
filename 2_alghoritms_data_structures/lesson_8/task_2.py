import random

class Node:

    def __init__(self, key):
        self.key = key
        self.right = None
        self.left = None

    def insert(self, key):
        if self.key == key:             #если узел уже существует
            return
        elif self.key < key:            #если новый узел > существующего, добавить в правую часть дерева
            if self.right is None:
                self.right = Node(key)  #рекурсивно доходим до крайнего узла в правой части дерева
            else:
                self.right.insert(key)
        else:
            if self.left is None:       #если новый узелy < существующего узла, добавить в левую часть дерева
                self.left = Node(key)
            else:
                self.left.insert(key)   #рекурсивно доходим до крайнего узла в левой части дерева

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # для листа
        if (self.right is None) and (self.left is None):
            line = f'{self.key}'
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # только левый узел
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = f'{self.key}'
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # только правый узел
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = f'{self.key}'
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # два узла
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = f'{self.key}'
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

my_tree = Node(50)
for _ in range(50):
    my_tree.insert(random.randint(0, 100))
my_tree.display()

"""
              ________________50_______________________                      
              /                                         \                     
     ________26_______               __________________79_                    
    /                 \             /                     \                   
   10_______       __37___         55_________           80_________          
  /         \     /       \       /           \                     \         
 _5    ____25    34_     40___   51        __63_             ______89___      
/     /         /   \   /     \           /     \           /           \     
0    11___     32  36  39    47          59_   67_         82_         91___  
 \        \                 /           /   \     \           \       /     \ 
 4       17                43          58  62    74___       83_     90    100
        /                             /               \         \         /   
       14                            57              78        87_       92   
                                                    /             \           
                                                   77            88           
Данное дерево удовлетворяет условия двоичного дерева поиска:
1. Вся левая часть от корня дерева меньше корневого узла,
    вся правая часть от корня дерева больше корневого узла
2. Левый потомок каждого узла меньше этого узла,
    правый потомок каждого узла больше этого узла
"""