# C language

## Arrays of Length Zero?
See an example [here](http://www.vpri.org/pdf/tr2006003a_objmod.pdf), and its answer

See explanation from [gcc doc](https://gcc.gnu.org/onlinedocs/gcc-4.1.2/gcc/Zero-Length.html).

It is used to achieve variable array length.

>Zero-length arrays are allowed in GNU C. They are very useful as the last element of a structure which is really a header for a variable-length object: 
```C
struct line {
    int length;
    char contents[0];
};
   
struct line *thisline = (struct line *)
	malloc (sizeof (struct line) + this_length);
thisline->length = this_length;
```