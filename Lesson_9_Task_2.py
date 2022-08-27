"""
Задача 2. Закодируйте любую строку по алгоритму Хаффмана.
"""
from binarytree import tree, Node

#функция создания дерева
def huffman_dict_new(string):
    chars = sorted(list(set(string)))
    nodes = tree(string)
    nodes_dict = {n['name']: n for n in nodes}

    if len(chars) == 1:
        return {chars[0]: '0'}

    ch_dict = {c: '' for c in chars}

    for c in chars:
        child_name = c
        child = nodes_dict[child_name]
        parent_name = child['parent']

        while parent_name:
            parent = nodes_dict[parent_name]
            if child_name == parent['left']:
                ch_dict[c] = '1' + ch_dict[c]
            elif child_name == parent['right']:
                ch_dict[c] = '0' + ch_dict[c]

            child_name = parent_name
            child = nodes_dict[child_name]
            parent_name = child['parent']

    return ch_dict

#закодируем строку
from collections import Counter, namedtuple


class Node(namedtuple("Node", ["left", "right"])):
    def walk(self,code, acc):
        self.left.walk(code, acc + '0')
        self.right.walk(code, acc + '1')

class Leaf(namedtuple("Leaf", ["char"])):
    def walk(self,code, acc):
        code[self.char] = acc

def haffman_encode(s):
    s_cnt = Counter(s)
    frq_chr = [(frq, Leaf(chr)) for chr, frq in sorted(s_cnt.items(), key=lambda t: t[1])]
    while len(frq_chr) > 2:
        first = frq_chr.pop(0)
        frq1, left = first[0], first[1]
        second = frq_chr.pop(0)
        frq2, right = second[0], second[1]
        if frq1 + frq2 > max([el[0] for el in frq_chr]):
            frq_chr.append((frq1 + frq2, Node(left, right)))
        else:
            idx = [frq_chr.index(el) for el in frq_chr if el[0] == frq1 + frq2][0]
            frq_chr.insert(idx, (frq1 + frq2, Node(left, right)))

    first = frq_chr.pop(0)
    frq1, left = first[0], first[1]
    second = frq_chr.pop(0)
    frq2, right = second[0], second[1]

    frq_chr.append((frq1 + frq2, Node(left, right)))
    [(_freq, root)] = frq_chr

    code = {}
    root.walk(code,'')
    return code

s = input('Введите строку для кодирования методом Хаффмана: ')
code = haffman_encode(s)
print(f'Символ--код:\n{code}')
print()
print(f'Исходная строка:\n{s}')
s_encode = ''.join(code[i] for i in s)
print(f'Закодированная строка:\n{s_encode}')

'''
Пример работы:

Введите строку для кодирования методом Хаффмана: я тебя люблю
Символ--код:
{'т': '000', 'е': '001', 'я': '01', 'л': '100', 'ю': '101', ' ': '110', 'б': '111'}

Исходная строка:
я тебя люблю
Закодированная строка:
0111000000111101110100101111100101
'''