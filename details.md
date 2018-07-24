# Details 

## Is it necessary to ignore ```.gitignore``` file itself?
Have be curious about this problem for a long time, in my opinion, ```.gitignore``` file may contain some files which I use just for myself and anyone else will not use it, so it should be visible to myself only.
but at the other hand, if some other developer maintain a repository with me at the same time, then some generated files should be ignored and it should be known to everyone participated in developing. But what if some files are only needed to be ignored ny myself? I found GitHub's help page gives a good solution as below

> If you don't want to create a .gitignore file to share with others, you can create rules that are not committed with the  repository. You can use this technique for locally-generated files that you don't expect other users to generate, such as 
> files created by your editor.
> 
> Use your favorite text editor to open the file called .git/info/exclude within the root of your Git repository. Any rule you add here will not be checked in, and will only ignore files for your local repository.
> 
> 1. In Terminal, navigate to the location of your Git repository.
> 2. Using your favorite text editor, open the file .git/info/exclude.

the above link also hold the view that ```.gitignore``` file is needed to be contained in a repository ~. Problem solved~


## Good workflow for open-source project on GitHub
confused about how to continuely contribute to a project which is maintained by many developers and make my fork's commits more easily to manage at the same time, I read about kubernetes's contributing guide and think it makes a good example about showing the developers how to contribute in a good way.  
[GitHub workflow guide for contributors](https://github.com/kubernetes/community/blob/master/contributors/guide/github-workflow.md)  
other parts of this guide are also worth reading for those who maintains a large project and for those who want to make their projects better in some conventions. Vscode's contribution guides are also worth reading,e.g. [its coding conventions](https://github.com/Microsoft/vscode/wiki/Coding-Guidelines)

## how to give good branch names?
got the problem from kubernetes's contributing guide about 'developing on a branch'. And I think [this question]() discussed on stackoverflow gives good answer.  
For short, the conventions are below(examples omitted here)

> Branch naming conventions
> 1. Use grouping tokens (words) at the beginning of your branch names.
> 2. Define and use short lead tokens to differentiate branches in a way that is meaningful to your workflow.
> 3. Use slashes to separate parts of your branch names.
> 4. Do not use bare numbers as leading parts.
> 5. Avoid long descriptive names for long-lived branches.



## good conventions for comments on source code?
List some good rules which I got from Rob Pike's _Practise of programming_ below

1. ```Comments shouldn't report self-evident information```

2. ```Comment functions and global data```

3. ```Don't comment bad code, rewrite it. Comment anything unusual or potentially con- fusing, but when the comment outweighs the code, the code probably needs fixing. This example uses a long, muddled comment and a conditionally-compiled debugging print statement to explain a single statement: 
? ```

4. ```Don't contradict the code. Most comments agree with the code when they are writ- ten, but as bugs are fixed and the program evolves, the comments are often left in their original form, resulting in disagreement with the code. This is the likely expla- nation for the inconsistency in the example that opens this chapter.```

5. ```Clarify, don't confuse. Comments are supposed to help readers over the hard parts, not create more obstacles```

and for the second item, I have read some code which use tools to generate documentation about its key method usages and meanings. This seems to solved the fourth item at the same time and I think it's a quite good practise for writing code.

In other scenarios it may be better to write as fewer comments as possible, since good code should explain itself clear by variable names, directory names, file names, etc.

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


P.S. at the end of the article, the author referred  Larry Wall's words and suggested that ```as a person, relating to other people, the three virtues we should aspire to are: diligence, patience, and humility```. These virtues may be the more important things that should be kept in mind when writing documentations.   
To see a good example of good documentation, I think [documentation of Rust](https://www.rust-lang.org/en-US/documentation.html
) and [documentation of Go](https://golang.org/doc/
) will be awesome enough. 

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

## How to understand the basic use of a framework or library quickly?
###  accordig to your goal -- you just want to use this library/framework
1. first look at the brief introduction of this library, pay attention to why the author create this library / framework? (Have anyone ever written something similar? What are the differences between this library / framework and the libraries / frameworks alike to it? Or, the author just wrote it out for practising? As a result, everyone found it useful and start to use it? )
2. see others' comments on the libraries / frameworks you are going to use, and focus on the diferences. Choose the one that fits you in your condition.
3. Read the documentation. Pay attention to the parts talking about the author's intended use for the library / framework. What are main partitions in funtion? Waht are the main interfaces use convention? Think about the problems you are going to tackle and how to can combine them with the library / framework.
4. Read the ```Best Practise``` part if the author wrote it.
5. Take a look at the author's testcases, paying special attention to the parts of the boundary value.

### accordig to your goal -- you want to implement similar requirements / you want to rewrite the library / framework
1. According to the testcase, take a look at how the interfaces is called in different procedures and find the corresponding file to be used step by step. Focus on the main modules been used and take a look up the details you care about.
2. Take a look at the issue area or the discussion area to see what people often ridicule,their common questions and the author's answers to the questions.

## Is it necessary to wrap your code after the left brace?
I tend to not do that, so the left side of each line must be the right brace. **It can prevent me from getting dazzled in reading code with many braces.**  
there are still a lot of opinions that support to wrap the code after the left brace, because it is symmetrical,e.g. Microsoft's C++ specification recommends to wrap. . . In short, it is good to be consistent in code style.
Post some of the most famous styles here:

K&R: Not to wrap

google C++：[Not to wrap](http://zh-google-styleguide.readthedocs.io/en/latest/google-cpp-styleguide/formatting/)

oracle Java：[Not to wrap](http://www.oracle.com/technetwork/java/javase/documentation/codeconventions-142311.html#449)

## Summarize my shortcut in mastering the basic use of various languages ​​ 
(just basic use, to learn a language well, you need to pay a lot of efforts)  
Emmm... learning languages in different programming styles really opened my eyes. I have to say it is so important to choose the proper language for your current work. And it is unreliable to believe your dearest language can do everything well. There is also no need to believe in the philosophy of the design of some languages. It is always important to put the usgae scenario first.
C++ is powerful, but with too many features, it's hard for a low level programmer to master all the best practises and write good codes. However when using language with fewer features that fit the work well, it will be somewhat more easy for the programmer to do a good work.   
Why do best practice matter? Because the implementations supporting a language are always complicated, if we need to learn about their details to write robust code, it would be too inefficient. Learn about the language's best practise help you get to know the author's opinion about the designs of the language more quickly.     
I summarize the following steps to quickly master the basic use of a programming language.  

1. focus on the problem you are going to tackle and observe what language is used by the most people in the field, it may also suit you well. Or you are familiar with a language which though not usually used in this field but you are familiar with it enough and believe it can help you get the work done, you may also choose it. Be careful about the condition where a lot of people who are not familiar with the language need to maintain your project after you leave.

2. learn about the language's basic data types and structs and compare their use to which you had learned before, for example, use data types and structs in C to help your learn is a good way. C provides us many interface enabling us to mainpulate the computer resources directly. Also the basic use of C is easy to manipulate, and you can learn it very fast.(being proficient in C and implementing complex functionalities well are hard though).   
You can also think about how to implement these data types or structs yourself in C and figure out possible costs of them. Think about some scenarios where you can use these data and how you can optimize your program's performance by choosing proper data types to reduce data copy and make use of the continuity of storage.  
Think about the differences between the language and some one you have learned well. Think about where their better scenario is respectively and whether there are some risks you may ignore in common use.   
3. find a project implemented in the language which makes good use of the language. With Good programming conventions used, the project should be better worth reading. Think about how you will implement the requirements and make comparisons to the author's implementations. Find the underlying reasons of the differences and thier tradeoffs respectively.  
4. Read about the ```best practise``` or ```effective xxx``` in the language's documentation or its community. And find some examples in practise.  
5. Use editors/IDE and tools recommended by most users or the documentation.  
6. With debugging, no need to learn various debugging tools from my perspective of view, just use ```print``` function and those integrated well with IDE. Doing some experiments to verify your assumption may be faster than watching many variables and guessing about the reasons in solving the problems.  
7. Some more mysterious behaviours of your program may be solved by just thinking about how the program is running in very detailed level and you may look to some popular communities for help.

**With all the above talked about, actually I want to say, Go is so awesome a language!!!! Cause all the above I've been talking about is what golang's official documentation is trying to teach its users~~~** And [Rob Pike](https://github.com/robpike) is very active in [Go's issue area on GitHub](https://github.com/golang/go/issues). So excited to hear the great master talking about the great language ~ More motivation for learning ~ [Rob Pike's personal website](http://herpolhode.com/rob/) also holds many of his posts which are worth reading.

