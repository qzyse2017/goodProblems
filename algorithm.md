# Algorithm 

## Dynamic programming versus divide-and-conquer

Well, both of the links are from the same author but I thought he could be a person skilled enough in algorithoms to answer these question.

I came across this problem while doing practise on leetcode and I viewed some discussion under a problem which I thought had nothing to do with dynamic programming, but users in the discussion area all used `dp` as their array name(well, maybe some of they just referenced the name from others). 

In fact, I thought that problem just has a little relation with memoization.

want to record the problem:```Compare dynamic programming and divide-and-conquer``` and make it clear when I should use dp and when dc, it can also help myself get some more deeper impreesion on these confusing concepts.(Added memoization here since it is also confusing)

Just like the author had got confused

>it feels for me like we may lose valuable detail that might help to catch the difference faster. And these detail tells us that each technique serves best for different types of problems.

### Similarity

From [https://github.com/trekhleb](trekhleb)
>they both work by recursively breaking down a problem into two or more sub-problems of the same or related type, until these become simple enough to be solved directly. The solutions to the sub-problems are then combined to give a solution to the original problem.

### Difference

>dynamic programming approach may be applied to the problem only if the problem has certain restrictions or prerequisites. And after that dynamic programming extends divide and conquer approach with memoization or tabulation technique.

Just anagolous to what I have got after reading CLRS again. 

From CLRS, "Dynamic Programming"

>Dynamic programming, like the divide-and-conquer method, solves problems by combining the solutions to subproblems. (“Programming” in this context refers to a tabular method, not to writing computer code.) As we saw in Chapters 2
and 4, divide-and-conquer algorithms partition the problem into disjoint subproblems, solve the subproblems recursively, and then combine their solutions to solve
the original problem. In contrast, dynamic programming applies when the subproblems **overlap**—that is, when subproblems **share subsubproblems**. In this context,
a divide-and-conquer algorithm does more work than necessary, repeatedly solving the common subsubproblems. A dynamic-programming algorithm solves each subsubproblem just once and then saves its answer in a table, thereby avoiding the work of recomputing the answer every time it solves each subsubproblem. 

>We typically apply dynamic programming to optimization problems. Such problems can have many possible solutions. Each solution has a value, and we wish to find a solution with the optimal (minimum or maximum) value. We call such a
solution an optimal solution to the problem, as opposed to the optimal solution, since there may be several solutions that achieve the optimal value.

>When developing a dynamic-programming algorithm, we follow a sequence of
four steps:
1. Characterize the structure of an optimal solution.
2. Recursively define the value of an optimal solution.
3. Compute the value of an optimal solution, typically in a bottom-up fashion.
4. Construct an optimal solution from computed information.

>Steps 1–3 form the basis of a dynamic-programming solution to a problem. If we
need only the value of an optimal solution, and not the solution itself, then we
can omit step 4. When we do perform step 4, we sometimes maintain additional
information during step 3 so that we can easily construct an optimal solution.

And I do not agree with the author `trekhleb` on the points that ``Once these two conditions are met we can say that this divide and conquer problem may be solved using dynamic programming approach.``, here he what he refer as `these two conditions` are `Optimal substructure` and `Overlapping sub-problems`, I think optimal substructure is not a must for dynamic programming to be used, it just usually used to solve optimal problems, but it can also adapted to solve those with just same subproblems.

Also not think the author's example is a good example, binary search can not be divided into divide-and-conquer category, since it do not need to search every element in the array, so it need not to combine what you got in  every sub-section array, and it is against the basic steps of divide-and-conquer. 

As in CLRS

>Divide-and-Conquer

>In Section 2.3.1, we saw how merge sort serves as an example of the divide-andconquer paradigm. Recall that in divide-and-conquer, we solve a problem recursively,
applying three steps at each level of the recursion:

>1. Divide the problem into a number of subproblems that are smaller instances of the same problem.
2. Conquer the subproblems by solving them recursively. If the subproblem sizes are small enough, however, just solve the subproblems in a straightforward manner.
3. Combine the solutions to the subproblems into the solution for the original problem 

### Memoization
Memoization is just common technique to make some algorithm run fast, in my opinion.

 without memoization, they can also run, but will do some redundant work, and I do not think this concept is bind to DP, since, just take Fibonacci sequence as an example, if you are required to return answers of many different index, you may just cache them, and Fibonacci seuqence, in theory, do not need to be calculated in DP, though, you can use DP.(IN fact, there are many interesting ways to calculate Fibonacci number and many of them are rather fast!)

REF

Introduction to algorithms

https://stackoverflow.com/a/50872936/10213822

https://dev.to/trekhleb/dynamic-programming-vs-divide-and-conquer-218i