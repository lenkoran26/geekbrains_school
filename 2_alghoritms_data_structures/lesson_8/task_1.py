import heapq
from collections import Counter, namedtuple

class Node():
    def __init__(self, left, right):
        self.Node = namedtuple("Node", ["left", "right"])
        self.Node.left = left
        self.Node.right = right

    def walk(self, codes, code):
        self.Node.left.walk(codes, code + "0")
        self.Node.right.walk(codes, code + "1")

class Leaf():
    def __init__(self, char):
        self.Leaf = namedtuple("Leaf", ["char"])
        self.Leaf.char = char

    def walk(self, codes, code):
        codes[self.Leaf.char] = code or "0"

def huf_encode(s):
    heap_list = []
    for ch, freq in Counter(s).items():
        heap_list.append((freq, len(heap_list), Leaf(ch)))
    heapq.heapify(heap_list)
    count = len(heap_list)

    while len(heap_list) > 1:
        freq1, _count1, left = heapq.heappop(heap_list)
        freq2, _count2, right = heapq.heappop(heap_list)
        heapq.heappush(heap_list, (freq1 + freq2, count, Node(left, right)))
        count += 1
    code = {}
    if heap_list:
        [(_freq, _count, root)] = heap_list
        root.walk(code, "")
    return code

def huf_decode(enc_text, code):
    text = []
    enc_char = ""
    for char in enc_text:
        enc_char += char
        for dec_char in code:
            if code.get(dec_char) == enc_char:
                text.append(dec_char)
                enc_char = ""
                break
    return "".join(text)

text = 'abaadgggdaaacvbbb'
print(f'Исходный текст:\n{text} ')

code = huf_encode(text)
encoded = "".join(code[char] for char in text)
print('Кодовая таблица:')

for char in sorted(code):
    print(f'{char}: {code[char]}')

print(f'Кодированный текст:\n{encoded} ')
print(f'Результат декодирования:\n{huf_decode(encoded, code)}')
assert huf_decode(encoded, code) == text

"""
Исходный текст:
abaadgggdaaacvbbb 
Кодовая таблица:
a: 11
b: 01
c: 1010
d: 100
g: 00
v: 1011
Кодированный текст:
1101111110000000010011111110101011010101 
Результат декодирования:
abaadgggdaaacvbbb
"""