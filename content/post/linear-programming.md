---
title: "Linear Programming"
date: 2018-07-29T00:00:00Z
draft: true 
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

And again:

$$ Z(x,y) = (600 \times x) + (800 \times y)$$

### Restrictions

Restrictions are any restriction that we need to apply to our variables. The
amount of resources, time, effort, etc... One common restriction considering
cases where we are applying linear programming to production is the **non
negativity** rule, it means, you can't produce -1 cars, all numbers of cars
produced must be positive or no car produced at all (zero cars).

> The maximization or minimization of the function $Z$ will always end up with
> on restriction limiting it's result. So you can analyse that restriction and
> determine the bottle neck of your function. In case of all restrictions being
> reached it means that there was no bottle neck and all resources were
> utilized.

In the example problem we have some restrictions, it will be listed bellow:

- 100 acres available, it means $x+y \leq 100$
- The market demand for *corn* $8x \leq 480$
- The market demand for *beans* $10y \leq 800$
- The labour limitation defined by $ 3x + 2y \leq 240$
- And finally, the non negativity rule, that give us $x \geq 0$ and $y \geq 0$

## Solving by hand

We will apply the graphical solution here where the limitations are plotted so
is possible to determine the solution visually. Bellow is the result of the
above restrictions plotted in a graph.

### Plot the graph

For all restrictions listed above, we will create a table with two lines, one
for the restriction result for the smallest value of $x$ and the maximization of
the value $y$, and the other for the opposite. As you can see, if there is only
one variable in the restriction the table is not needed, since we are looking
for the maximization of the use, it will result only on a straight line in the
graph. In the example case the limitations of the market can be seen in the
graph as perpendicular lines across their axis.

Since we are trying to maximize the resource usage, we remove the $\leq$ and
replace it with an equal symbol.

For the labour time restriction $3x + 2y = 240$

|  X |   Y |
|----|-----|
|  0 | 120 |
| 80 |   0 |

It means that for this restriction you will draw a line from the point $(0,120)$
to the point $(80,0)$. The are bellow the line, which for all elements there
this function is true, is called **feasible region**.

The second restriction is pretty straight forward, we will analyse the total available area for the crops, which is given by the $x+y = 100$.

|   X |   Y |
|-----|-----|
|   0 | 100 |
| 100 |   0 |

It means that you will draw a line from the point $(0,100)$ to the point
$(100,0)$.

The market demand for production of *corn* $8x = 480$, that gives us $x=60$. The
market demand for production of *beans* $10x = 800$, that gives us $y=80$. Both
will be represented by a straight line each on the given point.

With those restrictions calculated we can have some idea of the dimension of the
graph that we are going to plot. Since our max value for $y$ is 120 (labour
restriction) and for $x$ is 100 (total available area). Also adding a little bit
of interpretation to this graph, we can tell that if we only grow corn crops, we
won't be able to use all land that the farmer have, since the bottle neck in
this case will be the labor available.

Here is what the graph should look like after it is plotted.

- Colored in **orange** the 100 acres available, it means $x+y \leq 100$
- Colored in **stronger red** The labour limitation defined by $ 3x + 2y \leq 240$
- Colored in **red** the market demand for *corn* $8x \leq 480$
- Colored in **blue** the market demand for *beans* $10y \leq 800$

<iframe src="https://www.desmos.com/calculator/qb0rwtlecb?embed" width="500px" height="500px" style="border: 1px solid #ccc" frameborder=0></iframe>

### Intersection points

After plotting the restriction functions we have what is called **feasible
region**, a region of the graph that give possible solutions for our problem
based on the restrictions only. The second step is to determine which point in
this region maximizes the result for the objective function $Z$.


## Solving with python

## References

 - [Feasible Region](https://en.wikipedia.org/wiki/Feasible_region)

## Books

<style>
img[alt="cover"]{
  max-width: 12rem;
}
</style>

![cover](/books/covers/george-b-dantzig-linear-programming.jpg)

## References


