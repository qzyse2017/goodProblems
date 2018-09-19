# Virtualization
_problems about using and developing with virtualization_

## What is the authoritative list of Docker Run exit codes?
REF:
[answer from stackoverflow](https://stackoverflow.com/questions/31297616/what-is-the-authoritative-list-of-docker-run-exit-codes)  
[PR from GitHub](https://github.com/docker/docker/pull/14012)  
[Exit status from docker's doc](https://docs.docker.com/engine/reference/run/#exit-status)  
[Exit Codes With Special Meanings](http://tldp.org/LDP/abs/html/exitcodes.html)  
The following are from docker's documentation
> When docker run exits with a non-zero code, the exit codes follow the chroot standard, see below:  
> 
> 125 if the error is with Docker daemon itself
> 
> $ docker run --foo busybox; echo $?  
> `#` flag provided but not defined: --foo  
>   See 'docker run --help'.  
>   125  
> 126 if the contained command cannot be invoked  
> 
> $ docker run busybox /etc; echo $?    
> `#` docker: Error response from daemon: Container command '/etc' could not be invoked.  
>   126  
> 127 if the contained command cannot be found  
>   
> $  docker run busybox foo; echo $?    
> `#` docker: Error response from daemon: Container command 'foo' not found or does not exist.  
>   127  
> Exit code of contained command otherwise  
> 
> $ docker run busybox /bin/sh -c 'exit 3'; echo $?  
> `#` 3

and the following stackoverflow
> 128 + n Fatal error signal n:
> 
> 130 = (128+2) Container terminated by Control-C
> 
> 137 = (128+9) Container received a SIGKILL
> 
> 143 = (128+15) Container received a SIGTERM


## Dockerfile vs docker-compose, which is better?

>The docker cli is used when managing individual containers on a docker engine. It is the client command line to access the docker daemon api.

>The docker-compose cli can be used to manage a multi-container application. It also moves many of the options you would enter on the docker run cli into the docker-compose.yml file for easier reuse. It works as a front end "script" on top of the same docker api used by docker, **so you can do everything docker-compose does with docker commands and a lot of shell scripting. See this documentation on docker-compose for more details.**



REF:

https://stackoverflow.com/questions/29480099/docker-compose-vs-dockerfile-which-is-better
https://stackoverflow.com/questions/37966552/what-is-the-difference-between-docker-and-docker-compose
