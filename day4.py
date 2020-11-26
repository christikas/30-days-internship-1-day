Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 23:03:10) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> l=[23,56,89,45,23]
>>> print(l)
[23, 56, 89, 45, 23]
>>> l.append(54)
>>> print(l)
[23, 56, 89, 45, 23, 54]
>>> del l[0:1]
>>> print(l)
[56, 89, 45, 23, 54]
>>> a=min(l)
>>> print(a)
23
>>> b=max(l)
>>> print(b)
89
>>> t=(3,5,2,6,7)
>>> print(t)
(3, 5, 2, 6, 7)
>>> t=t[::-1]
>>> print(t)
(7, 6, 2, 5, 3)
>>> atuple=(4,5,6,3,7)
>>> alist=list(atuple)
>>> print(alist)
[4, 5, 6, 3, 7]
>>> 