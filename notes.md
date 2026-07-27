# Notes Data Structures and algorithsm


# Goals

Boot_Dev

 - Learn to think algorithmically. Break problems down into easier-to-solve parts.
 - Le arn to think about how to organize data for more efficient access. Break problems down into data models that make sense.
 - Learn and practice performance optimization. Make your code run faster and more efficiently, even with more data.

Mine:

    Learn in a way I can also teach it not only work with it. This step is crucial for my understanding of any topic. I'll no longer work with mediocrity nor will I force perfection, I'm here to learn, I'm a student, even when being a teacher becomes a responsinility, I'll still be a student. 

May this be good for me.
Soli Deo Gloria(SDG)

# Data Structures & Algorithm

Data structures are organizational tools that allow for more advanced algorithms.

Examples of data structures are:
 - List
 - Dictionaries
 - Sets

One of the big questions about these is, "When should I use one or another?"

An algorithm is a set of instructions that can be carried out to solve a problem. 

**Dont focus on memorizing this algorithms or data structures. Focus on undestanding how DSA works at the moment. You should understand what your code is doing and why.**


# What is an Algorithm?

In the context of computer science, an algorithm is a finite sequence of well-defined, computer-implementable instructions. In short, an algorithm is:

- Defined: there is a specific sequence of steps that performs a task
 - Unambiguous: there is a "correct" and "incorrect" interpretation of the steps
 - Implementable: it can be executed using software and hardware


Algorithms is not "code" per se, it is usually written in pseudocode because algorithm is a higher-level description of a solution to a problem. 
So, it does not care about the language or how or where is implemented. 
Pseudocode is just plain English that describes the steps of the algorithm. 

Visual Example:

![alt text](image.png) 

# Chapter 2: Math

## Exponentials

Basically in Python we can use the notation ** for exponentials"

eg.
    5^2 == 5**2(in python)

### Exponents grow

Exponents grow very large veri quickly.

eg.
    10^2 = 100
    10^4 = 10,000
### Non-Linear Growth

Exponents are important to understand when it cokmes to the execution speed of an algorithm. 

If the number of operations grows quickily as the amount of the input data increases, the algorithm will become slower and slower.

eg.

![alt text](image-1.png)

![alt text](image-2.png)

The doubling formula, 2*x results in linear or straight growth

The quadratic formula, x^2, keeps growing faster and faster.

Generally we try to avoid writing code that causes the usage of a resource to grow quadratically (with an exponent).

Sometimes that's a lot of computations (CPU utilization / slowness).
Sometimes that's a lot of memory usage (RAM utilization)
Sometimes that's a large storage requirement (disk space)
A notable exception is in cryptography and security: we want to force attackers to waste resources trying to get at our information

So we want the code to execute faster, and since we have the ability to decide that(According to how we construct our code, ergo we can also decide for a process to take a looooong time to process(like in the case of contrasting a hacker) )

## Logarithms 

A logarithm is the inverse of an oponent

eg.
    Exponent : 2^2 = 4
    Log(2)= log_2 4 = 2 || log_2 16 = 4

"log_2(16)" can be read as "log base 2 of 16", and means "the number of times 2 must be multiplied by itself to equal 16".

Brief eg. 

![alt text](image-3.png)


On python there is no direct operator to calculate log, but we can import the **math** library and use the math.log() function


    import math
    print(f"Logarithm base 2 of 16 is: {math.log(16, 2)}")
    # Logarithm base 2 of 16 is: 4.0
  
As opposed to exponents log grows **very very slow**.

Here is an example of the grox between a dobling formula and logarithm formula:

![alt text](image-4.png)



An example comparing linear, quadratic and log formulas, the differences are astronomical:

![alt text](image-5.png)

As you can see from the input colimn to the quadratic, the highest number is 10^6 or higher, when log, is just 20


## Factorials

The factorial of a positive integer os the product of all positive integer less than and equal to n not equal to 0.

eg.
    5! = 5*4*3*2*1 = 120
Factorials grows even faster than exponentiation.

Comparison table:

![alt text](image-6.png)





Graph comparing x!, 2^x, 2*x

![alt text](image-7.png)

As you cann see x! at first grows slower than 2^x, but then it grows much faster

For a numerical idea:
![alt text](image-8.png)

Increasing the value by 10 increased the result by 10^18

## Exponential decay

In physics an exponential decay is a process where a quantity decreases over time at a rate proportional to its current value. 



## Logarithmic Scale

In some cases, data can span several orders of magnitude, making it difficult to visualize on a linear scale. A logarithmic scale can help by compressing the data so that it's easier to understand.

For example, at LockedIn we have influencers with follower counts ranging from 1 to 1,000,000,000. If we want to plot the follower count of each influencer on a graph, it would be difficult to see the differences between the smaller follower counts. We can use a logarithmic scale to compress the data so that it's easier to visualize.

## Mean and Median

Means and medians are two of the most common ways to "summarize" a group of numbers.


The mean (or "average") of a group of numbers is the sum divided by the count of those numbers.

For example, say we have the numbers 2, 5, 1, 6, 75:

2 + 5 + 1 + 6 + 75 = 89
89 / 5 = 17.8

The mean is 17.8.

The median of a group of numbers is the middle number after sorting them.


For example, say we have the numbers 2, 5, 1, 6, 75:

Sort the numbers: 1, 2, 5, 6, 75
The middle number is 5, so the median is 5.

# Chapter 3 : Big O Notation

Pronounced "Big Oh" not "Big Zero"

Big O Analysis is oneway to compare the practicality of algorithms by classifying their time complexity. 

Big O is a characterization of algorithms according to their worst-case growth rates

We write Big-O notation like this:
        O(formula)

Where formula describes how an algorithm's run time or space requirements grow as the input size grows.

    O(1) - constant
    O(log n) - logarithmic
    O(n) - linear
    O(n^2) - squared
    O(2^n) - exponential
    O(n!) - factorial


As the size of inputs grows, the algorithms become slower to complete (take longer to run). The rate at which they become slower is defined by their Big O category.

For example, O(n) algorithms slow down more slowly than O(n^2) algorithms.

The Worst Big-O Category?
    The algorithms that slow down the fastest in our chart are the factorial and exponential algorithms, or O(n!), and O(2^n).

## O(n) - Order “n”

O(n) is very common - When the number of steps in an algorithm grows at the same rate as its input size, it's classified as O(n)

For example, our find min algorithm from earlier is O(n):

Set min to positive infinity.
For each number in the list, compare it to min. If it is smaller, set min to that number.
min is now set to the smallest number in the list.
The input to the find min algorithm is a list of size n. Because we loop over each item in the input once, we add one step to our algorithm for each item in our list.

As we use find min with larger and larger inputs, the length of time it takes to execute the function grows at a steady linear pace. We can reasonably estimate the time it will take to run, based on a previous measurement. If we find that:

Input size	Time to run
find_min(10 items)	2 ms
Then we can estimate the following:

Input size	Time to run
find_min(100 items)	20 ms
find_min(1000 items)	200 ms
find_min(10000 items)	2000 ms

## O(n^2) - Order “N Squared”

O(n^2) grows in complexity much more rapidly. That said, for small and medium input sizes, these algorithms can still be very useful.

A common reason an algorithm falls into O(n^2) is by using a nested loop, where the number of iterations of each loop is equal to the number of items in the input:

for person_one in persons:
    for person_two in persons:
        # every combination of people
        # will go on a date... twice!
        go_on_date(person_one, person_two)

## O(nm)

O(nm) is very similar to O(n^2), but instead of a single input that we care about, there are two. If n and m increase at the same rate, then O(nm) is effectively the same as O(n^2). However, if n or m increases faster or slower, then it's useful to track their complexity separately.

## Constant dont matter

Big-O notation only describes the theoretical growth rate of algorithms. It doesn't deal with the actual time an algorithm takes to run on a given machine. As such, when doing Big O analysis, we don't let ourselves get bogged down in details.

So, in Big notations, we dont care about quantitative data but qualitative one. We dont care about 3s, 5s, or 10 min. But about which is faster and which one is slower. 

Ex.
    We can tell if a ferrari is faster than a porche.
    We dont care if Ferrari is 100 mph or 10 mph faster. 

So when working with constants, we just... ignores it. 

eg.
    O(n+3) -> O(n)
    O(2log(5n)) -> O(log(n))
## O(1)

O(1) means that no matter the size of the input, there is no growth in the runtime of the algorithm. This is also referred to as a "constant time" algorithm.

In Python, a dictionary offers the ability to look items up by key, which is an operation that is independent of the size of the dictionary:

# this is a constant time lookup
org = organizations[org_id]

Dictionary lookups are O(1). Which is one of the reasons dictionaries and dictionary-equivalents in other languages are used all over the place.

## Order Log N

O(log(n)) algorithms are only slightly slower than O(1), but much faster than O(n). They do grow according to the input size, n, but only according to the log of the input.

    Coparison O(log(n)) vs O(n)
![alt text](image-9.png)

### Binary Search

A binary search algorithm is a common example of an O(log(n)) algorithm. Binary searches work on a pre-sorted list of elements.

Pseudocode
    Given two inputs:

        A list of n elements sorted from least to greatest
    A target value:

Do the following:

    Set low = 0 and high = n - 1.
    While low <= high:
        Set median (the position of the middle element) to (low + high) // 2, which is the greatest integer less than or equal to (low + high) / 2
        If list[median] == target, return True
        Else if list[median] < target, set low to median + 1
    Otherwise set high to median - 1
Return False

At each iteration of loop, we halve the list. Which makes the algorithm O(log(n)). In other words, to add one more step to the runtime, we'd have to double the size of the input. Binary searches are fast.

