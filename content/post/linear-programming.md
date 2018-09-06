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

- Scheduling problems;
- Resourcing problems;
- Assignment problems;
- Balance your meals to fit your macro nutrient goals;
- Sudoku.

## Example problem

To make things more concrete, I will present an example and solve it. Let's
suppose that a certain farmer wants to know which cereal to cultivate in his
farm. Let's suppose that the farmer can grow only 2 kinds of cereals, *corn* and
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

In the case of the proposed problem we have two variables, acres of *corn* and
*beans* that will be cultivated. For brevity, let's call *corn* $x$ and *beans*
$y$.


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

- The amount of money obtained for each acre of *corn* (named $x$) grown: $(150
  \times 8 \times x)$
- The amount of money obtained for each acre of *beans* (named $y$) grown: $(120
  \times 10 \times y)$

Then we subtract the costs of cultivating those crops, considering that each
work hour costs $200$ dollars:

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
> determine the bottleneck of your function. In case of all restrictions being
> reached it means that there was no bottleneck and all resources were
> utilized.

In the example problem we have some restrictions, it will be listed bellow:

- 100 acres available, it means $x+y \leq 100$
- The market demand for *corn* $8x \leq 480$
- The market demand for *beans* $10y \leq 800$
- The labour limitation defined by $ 3x + 2y \leq 240$
- And finally, the non negativity rule, that give us $x \geq 0$ and $y \geq 0$

### 100 acres available

Since we are calculating with our variables $x$ and $y$ being the acres
cultivated, they directly represent it, so no transformation is needed.

### The market demand for *corn*

We are using acres as our base value, the demand of *corn* is represented as the
amount of $x$ times how many sacks of *corn* each acre produces: $8x \leq 480$

### The market demand for *beans*

We are using acres as our base value, the demand of *beans* is represented as the
amount of $y$ times how many sacks of *beans* each acre produces: $10y \leq 800$

### The labour limitation

The same logic applies here, since we are using acres as our base value, we
multiply the labor needed for each acre of each cereal, it means that *corn*
needs $3$ hours of labor, and *beans* need $2$ hours.

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
won't be able to use all land that the farmer have, since the bottleneck in
this case will be the labor available.

Here is what the graph should look like after it is plotted.

- Colored in **orange** the 100 acres available, it means $x+y \leq 100$
- Colored in **red** The labour limitation defined by $ 3x + 2y \leq 240$
- Colored in **purple** the market demand for *corn* $8x \leq 480$
- Colored in **blue** the market demand for *beans* $10y \leq 800$

<iframe src="https://www.desmos.com/calculator/qb0rwtlecb?embed" width="500px" height="500px" style="border: 1px solid #ccc" frameborder=0></iframe>

### Intersection points

After plotting the restriction functions we have what is called **feasible
region**, a region of the graph that give possible solutions for our problem
based on the restrictions only. The second step is to determine which point in
this region maximizes or minimizes the result for the objective function $Z$.

The essence of this method is to create a visual analysis of those points of
intersection which are called **corner points**. If the problem has a solution,
this solution will be one of those corner points.

In the example we have **5 intersection points**, they will be presented based
on which restriction they intersect or 0, to make things easier to reference
later, we will name those points with letters.

- A) 0 and **demand for beans**;
- B) **demand for beans** and **available area**;
- C) **available area** and **available labor**;
- D) **available labor** and **demand for corn**
- E) **demand for corn** and 0;

Next step is to compile a table with all points and their values or $x$ and $y$.
But to be able to work with that we need to solve the equations to know their
values at their intersection point.

Points **A** and **E** won't require any special effort since they have a know
value in one of their axis.

#### Point B

Point **B** is the intersection between the demand of beans $y=80$ and the
available area $x+y \leq 100$. So we just solve the system

$$
  x + y = 100
$$

Replacing $y$ with it's value.

$$
  x + 80 = 100
$$

And

$$
  x = 100 - 80
$$

It gives us the point $x=20$ and $y=80$ $(20,80)$.

#### Point C

Point **C** is the intersection between the available labor $3x+2y \leq 240$ and
the available area $x+y \leq 100$. So we just solve the system

$$
3x+2y = 240
$$

$$
x+y = 100
$$

We need to isolate one factor, so let's isolate $y$ in the second equation.

$$
x+y = 100 (\times -2)
$$

And making one big equation we will have

$$
3x +2y -2x -2y = 240 - 200
$$


$$
x = 40
$$

Now that we have the $x$ value, we just need to replace it in any of this two
equations and we will have the $y$ value for that point.

$$
40+y=100
$$

$$
y=60
$$

It gives us the point $x=40$ and $y=60$ $(40,60)$.


#### Point D


Point **D** is the intersection between the available labor $3x+2y \leq 240$ and
the demand for corn $x=60$. So we just solve the system by replacing $x$

$$
 180 + 2y = 240
$$

$$
 2y = 240 - 180
$$

$$
 y = 30
$$

It gives us the point $y=30$ and $x=60$ $(60,30)$.

#### Corner points table

Now that all points are calculated, just replace the $x$ and $y$ symbols by
their values on the table bellow and calculate the objective function with it.
It will give the output for those variables, and using this output if our
objective is to maximize the result of the function, we will take the biggest
value on the table as the optimal value, if the objective is to minimize, we
take the smallest, simple as that.

Given the objective function

$$ Z(x,y) = (600 \times x) + (800 \times y)$$

| Point |  x |  y | Objective Function |
|-------|----|----|--------------------|
| A     |  0 | 80 |              64000 |
| B     | 20 | 80 |              76000 |
| C     | 40 | 60 |              72000 |
| D     | 60 | 30 |              60000 |
| E     | 60 |  0 |              36000 |

## Conclusion

Based on the table in the last section we can determine that the **optimal** area
for the maximization of the profit is **20 acres of corn** and **80 acres of beans**,
which will give a **profit of 76000$**.

This is enough, but we can look further and determine the bottlenecks, in other
words, what is limiting the maximization of the objective function. In this
example, this is a point of the analysis that gives the answer about what should
be worked on to improve the profit.

### Bottleneck analysis

To determine which restrictions are limiting the objective function, just
analyse the values of $x$ and $y$, if restrictions match the value it means that
this restriction is limiting the best outcome.

Applying our example

#### Available area

All available area was used, since
$$
20+80 = 100
$$

#### Demand for corn

The market demand for corn was not met, it means that if more corn was produced,
it would be sold.

$$
8 \times 20 \leq 480
$$

#### Demand for beans

The market demand for beans was met, it means that even if more beans were
produced, they won't be sold and won't generate any profit.

$$10 \times 80 = 800$$

#### Labor limitation

Still 20 hours of labor remaining after all the production, it can be determined
by:

$$
3 \times 20 + 2 \times 80 \leq 240
$$

$$
220 \leq 240
$$


## Solving with python

For solving this problem with python we are going to use **PuLP**. To setup PuLP
on Debian is easy, just `pip3 install pulp` and that is it.

### Modeling the problem

For modeling this problem using PuLP basically we will need to import PuLP and
create a problem:

```python
import pulp
problem = pulp.LpProblem("Farmer", pulp.LpMaximize)
```

Then we can add our variables to the problem, note that the restrictions based
on variable values are mapped here, so the non negativity rule and all others
based on the range of values should be applied at this point.

- The minimum bound of a variable is defined by the **lowBound** parameter.
- The maximum bound of a variable is defined by the **upBound** parameter.

Continuing our example, to create the $x$ and $y$ variables

```python
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')
```

Now we define our objective function, we can write it as plain python code and
just `+=` it into the `problem` variable like this:

```python
problem += 600 * x + 800 * y, "Z"
```

Now we do the same to all our restrictions, we can just `+=` them into the
problem.

```python
problem += x + y <= 100
problem += 8 * x <= 480
problem += 10 * y <= 800
problem += 3 * x + 2 * y <= 240
```

To print the actual state of the problem, just type the variable name in the
python console:

```
>>> problem
Farmer:
MAXIMIZE
600*x + 800*y + 0
SUBJECT TO
_C1: x + y <= 100

_C2: 8 x <= 480

_C3: 10 y <= 800

_C4: 3 x + 2 y <= 240

VARIABLES
x Continuous
y Continuous
```

### Solving the problem

After the problem is modelled we can run it to make PuLP find a solution for us
by calling the `solve()` method in the problem object.

```python
problem.solve()
```

And check the status of the solution passing the `problem.status` variable to
the PuLP array that contains all the status codes:

```python
pulp.LpStatus[problem.status]
```

As you can check in this problem, the output was `Optimal`, which means that it
found the optimal solution. Depending on the problem status, several outputs can
be shown:

- **Not Solved**: The problem status when it is created, before calling
  `problem.solve()` method.
- **Optimal**: The optimal solution has been found.
- **Infeasible**: There are no feasible solutions, maybe a contradiction in the
  problem definition, or a range of variables that can't exist like define two
  restrictions, one being $x \leq 10$ and the other $x \geq 20$
- **Unbounded**: There are no upper or lower bound to the variables, so the
  solution tend to the positive or negative infinite.
- **Undefined**: Maybe there is an optimal solution but it may not have been
  found.
  
### Getting the solution

To get the values for the solution of the problem, you can access both variables
directly or you can access them using the problem variable. With the problem
variable will look like this:

```python
[(v.name, v.value()) for v in problem.variables()]
```

And it will show an array of tuples with the variables names and values

```python
[('x', 20.0), ('y', 80.0)]
```

As you can check, we modelled the *corn* as being the $x$ variable, and the
optimal solution given by PuLP matches the optimal solution that we found by
hand. The same occurs to the *beans* that we modelled as $y$ variable.

You can also access directly the variables `x` and `y`.

```python
>>> y.value()
80.0
>>> x.value()
20.0
```

The very last thing is to know our profit, it can be accessed using the
`pulp.value(objective)` method, the objective variable that it expects is the
`problem.objective` value. An example:

```python
>>> pulp.value(problem.objective)
76000.0
```

As you can check, the very same solution that we found by hand.

# Another example

Problem of **minimization**

Metal plate cutting for war tanks building.

Uncut metal plates have 50cm.

They can be cut in 3 ways, 15cm, 17.5cm and 20cm. 

The max spare cut plate is 10 units of each size. 

## Variables

- Amount of metal plates that will be cut according with each specification:
  $x_i$ with $i$ being a number from 1 to 6.

## Objective function

$Z = 5 \times x_1 + 2.5 \times x_2 + 0 \times x_3 + 0 \times x_4 + 12.5 \times x_5 + 10 \times x_6$

## Restrictions

The demands of plates.

- Min on 15cm plates: $3 \times x_1 + 2 \times x_2 + 1 \times x_3 \geq 32$
- Max on 15cm plates: $3 \times x_1 + 2 \times x_2 + 1 \times x_3 \leq 42$
- Min on 17.5cm plates: $1 \times x_2 + 2 \times x_3 + 1 \times x_5 \geq 17$
- Max on 17.5cm plates: $1 \times x_2 + 2 \times x_3 + 1 \times x_5 \leq 27$
- Min on 20cm plates: $1 \times x_4 + 1 \times x_5 + 2 \times x_6 \geq 21$
- Max on 20cm plates: $1 \times x_4 + 1 \times x_5 + 2 \times x_6 \leq 31$

And finally the **non negativity** rule: $x_i \geq 0$

# Forewords

This is just an introduction to solving these kind of problems using the graphic
method. If you are interested into getting more info, there are several books
out there about it.

[If you think that you can help make this post better, send me a
PR](https://github.com/opsxcq/blog/blob/master/content/post/linear-programming.md)

## References

 - [Feasible Region](https://en.wikipedia.org/wiki/Feasible_region)
 - [PuLP Homepage](https://pythonhosted.org/PuLP/)
 - [PuLP Repository](https://github.com/coin-or/pulp)
 - [Simplex Algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)

## Books

If you want to read a book about it, I recommend this one by Dantzig, who is one
of the most important contributor of the field.

<style>
img[alt="cover"]{
  max-width: 12rem;
}
</style>

![cover](/books/covers/george-b-dantzig-linear-programming.jpg)
