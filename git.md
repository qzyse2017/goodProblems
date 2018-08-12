# git

_collect something helps to better use git_

## Use git rebase to keep the commits log clean
Make good use of `rebase` can make the commits log clean  
Use `rebase` to merge to branches can avoid a commit of 'Merge ...' 
Use `rebase` on a single rebase can merge many commits to a single one and can remove the commits you do not want to include.(use `squash` and `pick`)  
REF:  
[help doc from github](https://help.github.com/articles/about-git-rebase/)
[docs from git-scm](https://git-scm.com/book/en/v2/Git-Branching-Rebasing)


## sync a fork on GitHub
REF:  
[sync a fork -- GitHub help](https://help.github.com/articles/syncing-a-fork/)  
In short, it is  
```shell
$ git fetch upstream
$ git checkout master
$ git merge upstream/master

```

## use about git hooks?
REF:  
[solution from StackOverflow](https://stackoverflow.com/questions/13076584/500-error-while-creating-a-pull-request)  
[git push instructions from manuals](https://git-scm.com/docs/git-push)  
[git hooks' instructions from manuals](https://git-scm.com/docs/githooks)  
[skip git hooks -- stackoverflow](https://stackoverflow.com/questions/7230820/skip-git-commit-hooks)  

Overcame a 500Error while creating a new pull request and I tried the first method above but it seemed not to work for me and I read a message under the answer which explains that it seems to have been fixed by github's staff.   
And I happened to discover that I used ```git push -f ${your_remote_name} myfeature --no-verify``` instead of that without ```--no-verify```. But it also seemed not to be the reason, for the files in ```hooks``` directory all ends with ```.sample``` in their names so it should not for any of the work here to work.   
I listed a sample here, I thought it rather fun to use it to help the work done better somewhere in the future.

```shell
#!/bin/sh

# An example hook script to verify what is about to be pushed.  Called by "git
# push" after it has checked the remote status, but before anything has been
# pushed.  If this script exits with a non-zero status nothing will be pushed.
#
# This hook is called with the following parameters:
#
# $1 -- Name of the remote to which the push is being done
# $2 -- URL to which the push is being done
#
# If pushing without using a named remote those arguments will be equal.
#
# Information about the commits which are being pushed is supplied as lines to
# the standard input in the form:
#
#   <local ref> <local sha1> <remote ref> <remote sha1>
#
# This sample shows how to prevent push of commits where the log message starts
# with "WIP" (work in progress).

remote="$1"
url="$2"

z40=0000000000000000000000000000000000000000

while read local_ref local_sha remote_ref remote_sha
do
	if [ "$local_sha" = $z40 ]
	then
		# Handle delete
		:
	else
		if [ "$remote_sha" = $z40 ]
		then
			# New branch, examine all commits
			range="$local_sha"
		else
			# Update to existing branch, examine new commits
			range="$remote_sha..$local_sha"
		fi

		# Check for WIP commit
		commit=`git rev-list -n 1 --grep '^WIP' "$range"`
		if [ -n "$commit" ]
		then
			echo >&2 "Found WIP commit in $local_ref, not pushing"
			exit 1
		fi
	fi
done

exit 0

```

at last I created a successful pull request and I thougt the reason may just be those of GitHub.

Got to know some about how to use git hooks and it seems rather fun!!! 


## how to manage large binary files with git?
REF [managing-large-binary-files-with-git -- stackoverflow](https://stackoverflow.com/questions/540535/managing-large-binary-files-with-git)  
I think git-lfs and building binaries as submodule are good and easy solutions.


## how to view all git activity for a repo?  
REF [is-there-a-git-activity-log -- stackoverflow](https://stackoverflow.com/questions/12820167/is-there-a-git-activity-log)  
use ```git reflog```  
tried it, but seemed to only show activity for the local parts.

## how to How to clone a single branch in git?
REF [how to How to clone a single branch in git? -- stackoverflow](https://stackoverflow.com/questions/1778088/how-to-clone-a-single-branch-in-git)  
use  
```
# clone only the remote primary HEAD (default: origin/master)
git clone --single-branch

# as in:
git clone <url> --branch <branch> --single-branch [<folder>]
```  
here the ```<url>``` is the url for the origin repo and ```branch``` arg stands for the branch name in remote repo and ```single-branch``` is for your local directory.

## Is it necessary to ignore ```.gitignore``` file itself?
Have been curious about this problem for a long time, in my opinion, ```.gitignore``` file may contain some files which I use just for myself and anyone else will not use it, so it should be visible to myself only.
but at the other hand, if some other developer maintain a repository with me at the same time, then some generated files should be ignored and it should be known to everyone participated in developing. But what if some files are only needed to be ignored by myself? I found [GitHub's help page](https://help.github.com/articles/ignoring-files/#explicit-repository-excludes) gives a good solution as below

> If you don't want to create a .gitignore file to share with others, you can create rules that are not committed with the  repository. You can use this technique for locally-generated files that you don't expect other users to generate, such as 
> files created by your editor.
> 
> Use your favorite text editor to open the file called .git/info/exclude within the root of your Git repository. Any rule you add here will not be checked in, and will only ignore files for your local repository.
> 
> 1. In Terminal, navigate to the location of your Git repository.
> 2. Using your favorite text editor, open the file .git/info/exclude.

the above link also hold the view that ```.gitignore``` file is needed to be contained in a repository ~. Problem solved~



## how to give good branch names?
got the problem from kubernetes's contributing guide about 'developing on a branch'. And I think [this question](https://stackoverflow.com/questions/273695/git-branch-naming-best-practices) discussed on stackoverflow gives good answer.  
For short, the conventions are below(examples omitted here)

> Branch naming conventions
> 1. Use grouping tokens (words) at the beginning of your branch names.
> 2. Define and use short lead tokens to differentiate branches in a way that is meaningful to your workflow.
> 3. Use slashes to separate parts of your branch names.
> 4. Do not use bare numbers as leading parts.
> 5. Avoid long descriptive names for long-lived branches.


## How to write good git commit messages
I've been confused about how to write git commit messages properly for a long time, and I think this [blog](https://chris.beams.io/posts/git-commit/) can answer the problem well.  
strongly recommened reading the [blog](https://chris.beams.io/posts/git-commit/) yourself, the author refers some good examples of git commit messages in link forms.  
In this blog, the author explains why good git commit messages matters and lists seven rules of great git commit messages as follows:  
```
Keep in mind: This has all been said before.
1. Separate subject from body with a blank line
2. Limit the subject line to 50 characters
3. Capitalize the subject line
4. Do not end the subject line with a period
5. Use the imperative mood in the subject line
6. Wrap the body at 72 characters
7. Use the body to explain what and why vs. how
```
he elaborates the rules afterwards. And here are some points I usually took no notice of in the past.  
1. use a blank lines to sperate the subject and the body and you can use ```git log --pretty=oneline``` to see your message subject only later.
2. use git commit messages with bodies only when they are necessary.  
3. don't commit too many changes at once. Use atomic commits.

and the author recommend [Pro Git](https://git-scm.com/book/en/v2) at the last of the article.

ADD some good REF:  
[1] [learn from how Linus wrote commits](https://github.com/torvalds/linux/commits/master)  
[2] [some very simple rules for good commits](https://github.com/thoughtbot/dotfiles/blob/master/gitmessage)


## Good workflow for open-source project on GitHub
confused about how to continuely contribute to a project which is maintained by many developers and make my fork's commits more easily to manage at the same time, I read about kubernetes's contributing guide and think it makes a good example about showing the developers how to contribute in a good way.  
[GitHub workflow guide for contributors](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md)  
other parts of this guide are also worth reading for those who maintains a large project and for those who want to make their projects better in some conventions. Vscode's contribution guides are also worth reading,e.g. [its coding conventions](https://github.com/Microsoft/vscode/wiki/Coding-Guidelines)



