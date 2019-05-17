

from functools import reduce
import math


def flatten(list):
    return flattenHelper(list, [])

def flattenHelper(list,copyList):
    for i in list:
        if type(i).__name__ == 'list':
            flattenHelper(i, copyList)
        else:
            copyList.append(i)
    return copyList

list1 = [ [1, 2, [3, 4] ], [5, 6], 7]
l1 = flatten(list1)
print(l1)






def reverse(list):
    return reverseHelper(list, [],len(list)-1)

def reverseHelper(list1, copyList,int):
    if int < 0:
        return copyList
    else:
        test = list1[int]
        if type(test).__name__ == 'list':
            reversedList = reverse(list1[int])
            copyList.append(reversedList) #Try calling reverse on a smaller array
            int -= 1
            return reverseHelper(list1, copyList, int)
        else:
            copyList.append(list1[int])
            int -= 1
            return reverseHelper(list1, copyList, int)

list1 = [[1, 2], [3, [4, 5]], 6]
l1 = reverse(list1)
print(l1)


def compress(list):
    return compressHelper(list,[],0)

def compressHelper(list, copyList, int):
    if int >= len(list):
        return copyList
    else:
        if list[int] not in copyList:
            copyList.append(list[int])
            int += 1
            return compressHelper(list,copyList, int)
        else:
            int += 1
            return compressHelper(list, copyList, int)

list1 = [1,1,4,5,5,6,4,3,0,2,3,4,5,3,9,8,7,6,5,4,3,2,1,9,8,7,6,5,4,3,2,1]
l1 = compress(list1)
print(l1)



def capitalized(items:list) -> list:
    return list(filter(lambda x: x.startswith('A')or x.startswith('B') or x.startswith('C') or
                                 x.startswith('D') or x.startswith('E') or x.startswith('F') or
                                 x.startswith('G') or x.startswith('H') or x.startswith('I') or
                                 x.startswith('J') or x.startswith('K') or x.startswith('L') or
                                 x.startswith('M') or x.startswith('N') or x.startswith('O') or
                                 x.startswith('P') or x.startswith('Q') or x.startswith('R') or
                                 x.startswith('S') or x.startswith('T') or x.startswith('U') or
                                 x.startswith('V') or x.startswith('W') or x.startswith('X') or
                                 x.startswith('Y') or x.startswith('Z'), items))

capitalized_items = ['Apples', 'bananas', 'Cherries', 'Donkey', 'elephant','fox', 'Zuchinni']
capitalized_items = capitalized(capitalized_items)
print(capitalized_items)


def longest(strings: list, from_start=True) :
    #return reverse(sorted(strings,key=len)
    #strings.sort(key=lambda x: len(x))
    if from_start == False:
        return reverse(sorted(strings, key=lambda x: (len(x))))[0]
    else:
        return list(filter(lambda y: len(reverse(sorted(strings, key=lambda x: (len(x))))[0]) == len (y), strings))[0]


longest_items= ["a","bb","cccccc","d","ee", "ff","123456","666666"]
longest_items = longest(longest_items, False)
print(longest_items)


def composition(f: 'function', g: 'function') -> 'function':
    return lambda x: f(g(x))

def n_compose(*functions):
    return reduce(composition, functions)

def add(x,*args, **kwargs):
    x += 1
    return  x

def sqrt1(x,*args, **kwargs):
    math.sqrt(x)
    return x
def subtract(x, *args, **kwargs):
    x -= 10
    return x

funct =n_compose (add,sqrt1, subtract)
print(funct(15))

funct =  composition(add, subtract)
print(funct(10))