# git

_collect something helps to better user git_

## how to How to clone a single branch in git?
see [how to How to clone a single branch in git? -- stackoverflow](https://stackoverflow.com/questions/1778088/how-to-clone-a-single-branch-in-git)  
use  
```
# clone only the remote primary HEAD (default: origin/master)
git clone --single-branch

# as in:
git clone <url> --branch <branch> --single-branch [<folder>]
```  
here the ```<url>``` is the url for the origin repo and ```branch``` arg stands for the branch name in remote repo and ```single-branch``` is for your local directory.