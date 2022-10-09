from collections import OrderedDict
from timeit import timeit


def create_dict(n):
    simple_dict = {}
    for i in range(n):
        key = f'el_{i}'
        value = f'val_{i}'
        simple_dict[key] = value
    return simple_dict

def create_orderdict(n):
    ord_dict = OrderedDict()
    for i in range(n):
        key = f'el_{i}'
        value = f'val_{i}'
        ord_dict[key] = value
    return ord_dict

def del_elem_dict(mydict):
    for i in range(len(mydict)):
        mydict.popitem()

def del_elem_orddict(myorddict):
    for i in range(len(myorddict)):
        myorddict.popitem()

def get_el_dict(mydict):
    for i in mydict:
        tmp = mydict[i]

def get_el_orddict(myorddict):
    for i in myorddict:
        tmp = myorddict[i]

my_dict = create_dict(1000)
my_orddict = create_orderdict(1000)

print(f"Create dict: {timeit(stmt='create_dict(n)', setup='n=1000', globals=globals(), number=1000)}")
print(f"Create order dict: {timeit(stmt='create_orderdict(n)', setup='n=1000', globals=globals(), number=1000)}")
print(f"Del elem from dict: {timeit(stmt='del_elem_dict(mydict)', setup='mydict=my_dict', globals=globals(), number=1000)}")
print(f"Del elem from orderdict:{timeit(stmt='del_elem_orddict(myorddict)', setup='myorddict=my_orddict', globals=globals(), number=1000)}")
print(f"Get elem from dict: {timeit(stmt='get_el_dict(mydict)', setup='mydict=my_dict', globals=globals(), number=1000)}")
print(f"Get elem from orderdict: {timeit(stmt='get_el_orddict(myorddict)', setup='myorddict=my_orddict', globals=globals(), number=1000)}")

"""
Create dict: 0.21734940500027733
Create order dict: 0.2116831879975507
Del elem from dict: 0.0001759670049068518
Del elem from orderdict:0.0002252589983982034
Get elem from dict: 5.2431001677177846e-05
Get elem from orderdict: 6.266499985940754e-05
Вывод: заметных преимуществ использования упорядоченного словаря по сравнению с обычным словарем не замечено.
Нет смысла использовать OrderedDict в Python 3.6 и более поздних версиях
"""
