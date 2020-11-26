Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> dict1={'a':1,'b':2,'c':3}
>>> dict2={'d':4,'e':5,'f':6}
>>> d=dict1.copy()
>>> d.update(dict2)
>>> print(d)
{'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6}
>>> del d['c']
>>> print(d)
{'a': 1, 'b': 2, 'd': 4, 'e': 5, 'f': 6}
>>> keys=['a','b','c']
>>> values=[1,3,5]
>>> dictionary=dict(zip(keys,values))
>>> print(dictionary)
{'a': 1, 'b': 3, 'c': 5}
>>> s=set([5,6,9,8,6])
>>> print(len(s))
4
>>> a={3,7,9,6}
>>> b={5,7,4,9}
>>> print("original set")
original set
>>> print(a)
{9, 3, 6, 7}
>>> print(b)
{9, 4, 5, 7}
>>> a.difference_update(b)
>>> print(a)
{3, 6}
>>> a={3,7,9,6}
>>> b={5,7,4,9}
>>> print(a-b)
{3, 6}
>>> 