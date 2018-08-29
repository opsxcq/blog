---
title: "Linear Programming"
date: 2018-07-29T00:00:00Z
draft: false 
tags: ["math", "python"]
---

**Linear programming** is a mathematical method to achieve the best result for a
given problem. This problem is expressed through a mathematical model which
represents the real world problem. Also called **linear optimization** because
of it's essence to optimize a [*linear objective
function*](https://en.wikipedia.org/wiki/Loss_function).

In other words, linear programming aim to find the optimal input value for the
function, value which will also be the optimal solution for the problem. Usually
linear optimization is a good method to solve [assignment
problems](https://en.wikipedia.org/wiki/Assignment_problem) which are a
fundamental kind of [**combinatorial optimization**
problems](https://en.wikipedia.org/wiki/Combinatorial_optimization). Assignment
(or allocation) problems are basically the kind of problem that asks for the
allocation of scarce resources. Some examples:

- Determine which items to produce in a factory;

$$
\frac{1}{(\sqrt{\phi \sqrt{5}}-\phi) e^{\frac25 \pi}} =
     1+\frac{e^{-2\pi}} {1+\frac{e^{-4\pi}} {1+\frac{e^{-6\pi}}
      {1+\frac{e^{-8\pi}} {1+\ldots} } } }
$$

$$
X=Y
$$


## Example problem

To make things more concrete, lets try to use an example and solve it. Let's
suppose that a certain farmer wants to know which cereal to cultivate in his
farm. Let's suppose that the farmer can grow 2 kinds of cereals, *corn* and
*beans*. And the farmers main objective is the maximum profit. The farm has 100
acres, each acre of *corn* result in 8 sacks while each acre of *beans* result
in 10 sacks. For planting of each acre of *corn* it is needed 3 hours of work,
while for each acre of *beans* 2 hours of work are needed. The farmer has 240
hours of work available but it costs 200$ for every hour. The maximum demand is
limited by the market at a maximum of *480 sacks of corn* sold by 150$ each and
*800 sacks of beans* sold by 120$ each. Which cereal should the farmer grow to
have the maximum profit ?


## Problem modeling

To model the problem, we need to extract the 3 main characteristics of the
problem, determine the variables, determine it's restrictions and calculate the
objective function.

### Variables

Variables are everything that you can work on the problem, they are the moving
parts and the input of the *objective function*.

In the case of the proposed problem we have two variables, the amount of *corn*
and *beans*. For brevity, let's call *corn* $x$ and *beans* $y$.


### Objective function

It shows our target function to archive, it can be a **maximization** or
**minimization** of the result of the function $Z$, or in very rare cases, the
objective is to approximate $Z$ to a certain value. The objective function is
created to reflect the impact of the variables on the outcome. In other words,
based on the variable values, it output has to represent the outcome in the real
world.

For the objective function of the example case above, the main objective is
**maximum profit**, it means to maximize the output of the function that given
the amount of *corn* and *beans* calculate the profit. We can define what profit
is by the $Profit = Sell Price - Costs$.

So:

$$ Z(x,y) = (150 \times 8 \times x) + (120 \times 10 \times y) - (200 \times 3
  \times x) - (200 \times 2 \times y) $$

Let's break it down in some chunks and analyse it:

- The amount of money for each acre of *corn* (named $x$) grown: $(150 \times 8 \times x)$
- The amount of money for each acre of *beans* (named $y$) grown:  $(120 \times 10 \times y)$

Then we subtract the costs of cultivating those crops:

- The cost of cultivating one acre of *corn* $(200 \times 3 \times x)$
- The cost of cultivating one acre of *beans*  $(200 \times 2 \times y)$

We can optimize it by writing:

$$ Z(x,y) = (1200 \times x) + (1200 \times y) - (600 \times x) - (400 \times y) $$

### Restrictions

Restrictions are any restriction that we need to apply to our variables. The
amount of resources, time, effort, etc... One common restriction considering
cases where we are applying linear programming to production is the **non
negativity** rule, it means, you can't produce -1 cars, all numbers of cars
produced must be positive or no car produced at all (zero cars).

## Solving by hand

## Solving with python

## References

## Books

<style>
img[alt="cover"]{
  max-width: 12rem;
}
</style>

![cover](/books/covers/george-b-dantzig-linear-programming.jpg)

## References


