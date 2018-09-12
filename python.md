# Python

## What is double colon in Python when subscripting sequences?

e.g. ```a[::-1]```

some most common use 

```
For example, you can now easily extract the elements of a list that have even indexes:
>>>
>>> L = range(10)
>>> L[::2]
[0, 2, 4, 6, 8]

Negative values also work to make a copy of the same list in reverse order:
>>> L[::-1]
[9, 8, 7, 6, 5, 4, 3, 2, 1, 0]

This also works for tuples, arrays, and strings:
>>> s='abcd'
>>> s[::2]
'ac'
>>> s[::-1]
'dcba'
```

in the docs for python, it reads, this feature is requested by developers of Numerical Python, I just saw the use in some code, the author use it to reverse an array, however i do not think it good to do this if it just need to reverse the array without some more extensible demands, it should just be clearer to use ```array.reverse()``` 

There lists some more use of the feature in the doc at the end of the ref.

REF

https://docs.python.org/3/whatsnew/2.3.html#extended-slices

https://stackoverflow.com/a/3453103/7122122

https://docs.python.org/3/whatsnew/2.3.html#extended-slices

https://docs.python.org/3/library/array.html?highlight=rray#array.array.reverse

https://stackoverflow.com/questions/20839219/how-to-reverse-the-array-in-python

