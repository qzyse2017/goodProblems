# goodProblems

collecting intereting prolems I overcome every day.  
the content of every file is indicated in its name, and at the start of each file, there is a simple introduction.

## SEE posts according to TIME
SEE [`newoposts.md`](newPosts.md), I use [`genPosts.py`](genPosts.py) to generate this file automatically by git logs.  
to use the scripts to help generate your contents, you need to format your commit message into ```Insert `<your-content-digest-here>` `<insert-location-here-no-md-suffix>` ```  
it is recommended you do the commit every time you insert a new item and specify your location of insertion by its file name. When you need to renew the content, run ```python genPosts.py``` ,the new posts will be updated in ```newPosts.md``` .

Also, for the title location to be inserted correctly in the ```newPosts.md```, it is recommended you use ```copy-paste``` while writing the content digest in commit message to make sure it is same as the title in the correspoding documentation and the view you see will be directly located to the correspoding title when you click the link. Special characters should be taken care of(I have not tested them all). 

Not all title locations in my commits will work well(most of them will probably work), I do not follow the convention talked above in all my documentation here(e.g. ```tricksAndWindows.md```).


## TODO
-[ ] Remove special characters in content title locator and it should work correctly for locating, do it before next generating for contents