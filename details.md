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

oracle的Java：[Not to wrap](http://www.oracle.com/technetwork/java/javase/documentation/codeconventions-142311.html#449)

## json文件最后的","是否有必要
感觉[这里](https://www.zhihu.com/question/265283301/answer/292662958)这条回答比较有道理，总结下要点就是，加不加逗号其实对于parser的实现没有很多影响，但是加逗号，并且记录分行写的时候，新增一条item可以少产生两行diff，并且防止某些时候少加逗号使得依靠json生成的某些数据产生连接在一起的错误。

## 总结下自己用偷懒的方式学习各种语言的经验
自问自答：
emmm，很多语言了解下真的是开阔眼界啊，不得不说，每一门语言都是由很合适自己的场景的，所以千万不要说“xxx是最好的语言”，语言设计的哲学也是不需要盲目追逐的，同样是要跟应用场景联系在一起，C++功能是强大，但是总觉得写法太多，而且因为功能太多，很多时候很难学会最佳实践，像我大golang，对准小领域，设计正交化，功能减少，大道至简，反而更容易学会最佳实践。  
为什么上面一直再强调最佳实践呢，因为最近发现语言本身的特性和底层实现都是很复杂的，每一门语言都靠采坑去学是非常没效率的，这时候好好读好最佳实践就可以很快避免很多坑，同时写出比较稳健的代码了。  
所以总结下偷懒方式学习新语言的套路：  
1. 对准要解决问题的领域，看看大家普遍再用什么语言，或者找一个你稍微了解的，并且觉得这个语言虽然在这个领域上用的人少，但是你觉得它有潜力，你要当开山的那个人。然后注意一些项目相关的东西，比如和你一起干活的人多吗，以后项目需要被维护的频率和时间；干活的人多和项目需要长期经常维护的，如果不是你在维护，那么最好都用常见的，会这门语言的人数多的语言。  
2. 学习该语言的基本数据类型，特别注意要和你以前已经有过的经验进行比较学习，就找C进行对比就是很好的尝试。因为C是最接近机器并且容易读懂的代码，和学习C的过程中使用计算机资源的经历进行对比可以容易联想到一些可能的数据结构底层实现的大概思路，以及可能的开销，在必要的时候，对关键数据结构做对比，减少数据拷贝，利用数据存储的连续性可以很大程度上优化程序性能。同时，注意找一门自己了解深入，并且和该语言使用领域以及特性接近的语言，进行对比，加深理解，搞清楚新学的语言的创新和便捷的地方在哪里，什么场景下不合适使用，安全性方面可能有哪些坑。
3. 接下来就是找一个成熟点的项目，看一看自己刚才读的文档里面的东西怎样使用在真实环境中，读的时候注意思考，自己要实现这个功能，会怎么写，和作者不一样的地方可以深入思考下，作者的写法或许就是一种更好的实践。
4. 接下来就是在文档/社区里面找一些关于最佳实践的文章读一读了。读过之后，可以再找一些实例看看。
5. 最后工具方面，开始干大项目前先上线查查大家都用什么编辑器，工具链，可以提高效率。
6. debug方面，无论何时何地，我都推荐，print大法，通用性好，用好了可以有奇效，除了速度慢一点，但是我并不觉得直接跑断点看变量值不算是蛮力debug，我更推崇“演绎推理-实验验证”的办法，快很多。
7. 最后的最后，我想说，多线程，并行的东西这类，坑都多。。。很多神奇的bug，遇到看似没道理的bug时候多往这里想想，有奇效。。。


