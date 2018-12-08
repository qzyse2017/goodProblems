# Java

collect problems I encounter while using Java

## When to use abstract class and when interface?

Encountered this problem while extracting some java interfaces from some existing code in my work. 

And I had seen some examples which may use abstract class or interface as the "interface" used by the higher level to call.

Found some links below in the REF

**From the answer on stackoverflow**

>Now you may be wondering why not declare an abstract class as an interface, and have the Dog and Cow implement the interface. Sure you could - but you'd also need to implement the eat and sleep methods. By using abstract classes, you can inherit the implementation of other (non-abstract) methods. You can't do that with interfaces - an interface cannot provide any method implementations.

**The second link shows some more detailed differences.**

I listed here mainly some points which are mentioned in the other links I saw.

>Interfaces have all methods inherently public and abstract. You can not override this behavior by trying to reduce accessibility of methods. You can not even declare the static methods. Only public and abstract.

>On the other side, abstract classes are flexible in declaring the methods. You can define abstract methods with protected accessibility also. Additionally, you can define static methods as well, provided they are not abstract. Non-abstract static methods are allowed.

**Always remember that choice between the interface or abstract class is not either/or scenario, where choosing anyone without proper analysis would yield the same results.** A choice must be made very intelligently after understanding the problem at hand. Let us try to put some intelligence here.

>**Partial behavior with abstract classes**

>Abstract classes let you define some behaviors; it makes them excellent candidates inside of application frameworks.

>Lets take example of HttpServlet. It is the main class you must inherit if you are developing a web application using Servlets technology. As we know, each servlet has a definite life cycle phases, i.e. initialization, service, and destruction. What if each servlet we create, we have to write the same piece of code regarding initialization and destruction again and again. Surely, it will be a big pain.

>**Contract only interfaces**

>An interface only provide contracts and it is the responsibility of implementing classes to implement each and every single contract provided to it.An interface is the best fit for cases where you want to define only the characteristics of class, and you want to force all implementing entities to implement those characteristics.

>I would like to take an example of Map interface in the collections framework. It provides only rules, how a map should behave in practice. e.g. it should store the key-value pair, the value should be accessible using keys etc. These rules are in form of abstract methods in the interface.

>Also, interfaces can be used in defining the separation of responsibilities. For example, HashMap implements 3 interfaces: Map, Serializable and Cloneable. Each interface defines separate responsibilities and thus an implementing class choose what it want to implement, and so will provide that much limited functionality.

>With Java 8, now you can define methods in interfaces. These are called default methods. Default methods enable you to add new functionality to the interfaces of your libraries and ensure binary compatibility with code written for older versions of those interfaces.

>If you see we are now able to provide a partial implementation with interfaces as well, just like abstract classes. So essentially the line between interfaces and abstract classes has become very thin. They provide almost the same capabilities now.
Now, only one big difference remains that you cannot extend multiple classes whereas you can implement multiple interfaces. Apart from this difference, you can achieve any possible functionality from interfaces which abstract classes can make possible, and vice-versa is also true.

Other topics in the left side bar about OOPs are also worth reading! They may be excellent problems if you learn any other OOP languages.

**And the fisrt answer from quora provides some thinking on OOP design principles, but I do not think it declares some useful rules you can use in your work.**

The following provides some rules useful, listed them here

From [Alex-S-Constâncio](https://www.quora.com/profile/Alex-S-Constâncio)

>The most important thing you should understand is that classes carry behavior (code) and interfaces does not (they don’t have code). So, an abstract class can provide code that will be easily reused in descending classes.
You will use abstract classes when you want to create a family of classes that share some general behavior, complemented with some specific behavior provided by descending classes.

>You will use interfaces when you want to be certain that given methods do exist, not regarding which class family is providing them.

And from [Siddiq Ahmed Syed](https://www.quora.com/profile/Siddiq-Ahmed-Syed)

>Interface can be considered as a contract. They tell what needed to be achieved but not how to achieve it. The benefit of interface is that a class can implement many interfaces (mocks multiple inheritance). The drawback is that interface cannot contain any code

>The benefit of Abstract class is that it gives you an ability to provide a structure. The drawback is that a class can extend only one abstract class.

>Rule of thumb is to use interface when you are not sure about the implementation and when there is possibility that you class will extend other classes. Use abstract class when you want to provide partial implementation and wanted the inheriting class to provide the remaining implementation.

From [Greg Joshua](https://www.quora.com/profile/Greg-Joshua)

>If you want the user have greater freedom over their class definition while making sure that they adhere to a core group of functions then implement an interface. If you have a narrow scope but you would like to permit some flexibility then use an abstract class.

>If you have a class that implements multiple interfaces then objects of that class can be stored as types of any interface it implements. Subclasses of an abstract class can have their instances saved as the abstract class type. There is no definitive case to use one instead of the other but they lend themselves better to different situations. This is where design patterns come into play.

REF:

- [How and when to use an abstract class](https://stackoverflow.com/questions/6007089/how-and-when-to-use-an-abstract-class)

- [Interface vs. Abstract Class in Java](https://howtodoinjava.com/oops/exploring-interfaces-and-abstract-classes-in-java/)

- [How do I use abstract classes and interface in Java, and when to use them?](https://www.quora.com/How-do-I-use-abstract-classes-and-interface-in-Java-and-when-to-use-them)


## Implement abstract factory pattern in Java



