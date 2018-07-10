# Details 

## how to write good documentation  
REF:  
- [A beginner's guide to writing documentation](https://github.com/writethedocs/www/blob/master/docs/guide/writing/beginners-guide-to-docs.rst)
- [write better docs](https://opensource.com/business/15/5/write-better-docs)  

Having gained a lot from good documentation and struggled a lot with that not so friendly, I've been curious for a long time about how to write good documentation.   
I found the two article referred above answers the problem well, especially the second one.  
The parts about ```What should you be writing?``` in the second article is very meaningful. I think it tells the key points to distinguish between friendly and obscure documentations.
In short, good documentation should contain the following parts:  
- Scope: decide what topics you are  willing to cover
- Types of docs
  - start here:```the place where you tell users what they need to know before they even get started```
  - reference guide:```This is where terms are defined, functions' input and output are explained```
  - tutorials:show how each steps should be taken
  - learning/understanding:```Often linked to from the tutorials, the learning/understanding documents dig deeper. They investigate the why and the how of a particular thing. Why was a certain decision made? How was it implemented in the code? What does the future look like for this thing? How can you help create that future?```  
  this part is better done as blog posts
  - cookbook/recipe: 
    - ```provide cut-and-paste best-practice solutions to common problems```
    - ```They should be accompanied by an explanation```, but keeping your code correctly is crucial, people tends to cut and paste your code without reading the explanation carefully.
    - all examples should be tested first
    - ```promote the best practice``` ```never tell them how not to do it```
  - error measage:it should be more detailed and help the user easily find the solution.  


P.S. at the article, the author referred  Larry Wall's words and suggested that ```as a person, relating to other people, the three virtues we should aspire to are: diligence, patience, and humility```. These virtues may be the more important things that should be kept in mind when writing documentations. 




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
  