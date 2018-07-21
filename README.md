# goodProblems

collecting intereting prolems I overcome every day.  
the content of every file is indicated in its name, and at the start of each file, there is a simple introduction.

## SEE posts according to TIME
SEE [`newoposts.md`](newPosts.md), I use [`genPosts.py`](genPosts.py) to generate this file automatically by git logs.  
to use the scripts to help generate your contents, you need to format your commit message into ```Insert `<your-content-digest-here>` `<insert-location-here-no-md-suffix>` ```  
it is recommended you do the commit every time you insert a new item and specify your location of insertion by its file name. When you need to renew the content, run ```python genPosts.py``` ,the new posts will be updated in ```newPosts.md``` .