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