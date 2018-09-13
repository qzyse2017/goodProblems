# golang

_with my beautiful golang_

## tools
- all tools recommended by its official documentation
- tools which integrated in [vscode-go](https://github.com/Microsoft/vscode-go) plugin.
- package management: [govendor](https://github.com/kardianos/govendor)

## Difference between slice and array
SEE https://blog.golang.org/go-slices-usage-and-internals, do not going to repeat its contents here, the blog can be rather detailed.

## Two dimensional array representation and its memeory use in golang

There are usually two ways to express multidimensional arrays in golang, one is to use **array**, the other to use **slice of slice**.

1. In the link above, the author proof that array will use less memory size(just the same as **table_rows** `*` **table_columns** ) while slice, because of its struct header, tands to make use more memory.

2. Another difference which matters is that when initializing, array's length should be constant while slice's need not to be.

3. >With arrays of arrays, the inner arrays are, by construction, always the same length; however with slices of slices (or arrays of slices), the inner lengths may vary dynamically. Moreover, the inner slices must be initialized individually. 

4. may also use **arrays of slices**

>Like arrays, slices are indexable and have a length. The length of a slice s can be discovered by the built-in function len; unlike with arrays it may change during execution. The elements can be addressed by integer indices 0 through len(s)-1. The slice index of a given element may be less than the index of the same element in the underlying array. 

>A slice, once initialized, is always associated with an underlying array that holds its elements. A slice therefore shares storage with its array and with other slices of the same array; by contrast, distinct arrays always represent distinct storage. 

>The array underlying a slice may extend past the end of the slice. The capacity is a measure of that extent: it is the sum of the length of the slice and the length of the array beyond the slice; a slice of length up to that capacity can be created by slicing a new one from the original slice. The capacity of a slice a can be discovered using the built-in function cap(a). 

REF

https://stackoverflow.com/a/39561477/7122122

https://golang.org/ref/spec#ArrayLength