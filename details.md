# Details 

## how to insert a newline in markdown
1. insert two blank spaces and press the Enter key after that  
2. pressing the Enter key twice can also make a new line  


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
  