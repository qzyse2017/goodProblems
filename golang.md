# golang

_with my beautiful golang_

## tools
- all tools recommended by its official documentation
- tools which integrated in [vscode-go](https://github.com/Microsoft/vscode-go) plugin.
- package management: [govendor](https://github.com/kardianos/govendor)

## how to check if a file exists in go
Well, it all started from that I found there are two functions in package os which seems to have similar functionality of checking error reported so I search the two functions, and got this [answer](https://stackoverflow.com/a/49892959/7122122)

>So basically if `os.Stat` if this function doesn't give any error that means the file is existing if it does you need to check what kind of error it is, here comes the use of these two function `os.IsNotExist` and `os.IsExist`.
This can be understood as the Stat of the file throwing error because it doesn't exists or is it throwing error because it exist and there is some problem with it.

>The parameter that these functions take is of type error, although you might be able to pass nil to it but it wouldn't make sense.

>This also points to the fact that `IsExist` is not same as `!IsNotExist`, they are way two different things.
So now if you want to know if a given file exist in go, I would prefer the best way is:
```go
if _, err := os.Stat(path/to/file); !os.IsNotExist(err){
   //TODO
} 
```

description and example from golang [docs](https://golang.org/pkg/os/#IsExist)

>func IsExist

>func IsExist(err error) bool
>IsExist returns a boolean indicating whether the error is known to report that a file or directory already exists. 
>It is satisfied by ErrExist as well as some syscall errors. 

>func IsNotExist 

>func IsNotExist(err error) bool
>IsNotExist returns a boolean indicating whether the error is known to report that a file or directory does not exist. It is satisfied by ErrNotExist as well as some syscall errors. 

So the difference is that you **use some other functions which will return an error to you the error could be two type, it may mean that some file or directory has existed and the creation of them is failed and you need to do some handling, to verify this error, you use os.IsExist; and in another condition, it may mean that you want to open a file or directory which does not eixst and you need os.IsNotExist to verify the error is true or false.**


REF 

https://golang.org/pkg/os/#IsExist

https://stackoverflow.com/questions/12518876/how-to-check-if-a-file-exists-in-go/22467409#22467409

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

## What is a good best practice with Go workspaces?

Recommned the answer from [Matt](https://stackoverflow.com/a/20725538/7122122):
>I used to use multiple GOPATHs -- dozens, in fact. Switching between projects and maintaining the dependencies was a lot harder, because pulling in a useful update in one workspace required that I do it in the others, and sometimes I'd forget, and scratch my head, wondering why that dependency works in one project but not another. Fiasco.

>I now have just one GOPATH and I actually put all my dev projects - Go or not - within it. With one central workspace, I can still keep each project in its own git repository (src/<whatever>) and use git branching to manage dependencies when necessary (in practice, very seldom).

>My recommendation: use just one workspace, or maybe two (like if you need to keep, for example, work and personal code more separate, though the recommended package path naming convention should do that for you).

And the same convention is recommended in [golang.org](https://golang.org/doc/code.html#GOPATH). 

>The GOPATH environment variable specifies the location of your workspace. It defaults to a directory named go inside your home directory, so $HOME/go on Unix, $home/go on Plan 9, and %USERPROFILE%\go (usually C:\Users\YourName\go) on Windows. 

>If you would like to work in a different location, you will need to set GOPATH to the path to that directory. (Another common setup is to set GOPATH=$HOME.) Note that GOPATH must not be the same path as your Go installation. 

>The command go env GOPATH prints the effective current GOPATH; it prints the default location if the environment variable is unset. 

>For convenience, add the workspace's bin subdirectory to your PATH: 

``$ export PATH=$PATH:$(go env GOPATH)/bin``

>The scripts in the rest of this document use $GOPATH instead of $(go env GOPATH) for brevity. To make the scripts run as written if you have not set GOPATH, you can substitute $HOME/go in those commands or else run: 
``$ export GOPATH=$(go env GOPATH)``

>To learn more about the GOPATH environment variable, see 'go help gopath'. To use a custom workspace location, set the GOPATH environment variable.  

REF

https://stackoverflow.com/questions/20722502/whats-a-good-best-practice-with-go-workspaces

https://golang.org/doc/code.html#GOPATH