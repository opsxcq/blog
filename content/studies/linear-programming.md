+++
title = "Linear Programming"
author = ["OPSXCQ"]
date = 2018-08-09
draft = false
+++

**Linear programming** is a mathematical method to achieve the best result for a
given problem. This problem is expressed through a mathematical model which
represents the real world problem. Also called **linear optimization** because of
it's essence to optimize a [_linear objective function_](https://en.wikipedia.org/wiki/Loss_function).

In other words, linear programming aim to find the optimal input value for the
function, value which will also be the optimal solution for the problem. Usually
linear optimization is a good method to solve [assignment problems](https://en.wikipedia.org/wiki/Assignment_problem) which are a
fundamental kind of [combinatorial optimization problems](https://en.wikipedia.org/wiki/Combinatorial_optimization). Assignment (or
allocation) problems are basically the kind of problem that asks for the
allocation of scarce resources. Some examples:

-   Scheduling problems;
-   Resourcing problems;
-   Assignment problems;
-   Balance your meals to fit your macro nutrient goals;
-   Sudoku.

While the first example is focused on explaining the concepts, the second
example will be solved using a more straight forward solution without giving
redundant explanations.


## Example problem 1 {#example-problem-1}

To make things more concrete, I will present an example and solve it. Let's
suppose that a certain farmer wants to know which cereal to cultivate in his
farm. Let's suppose that the farmer can grow only 2 kinds of cereals, _corn_ and
_beans_. And the farmers main objective is the maximum profit. The farm has 100
acres, each acre of _corn_ result in 8 sacks while each acre of _beans_ result in 10
sacks. For planting of each acre of _corn_ it is needed 3 hours of work, while for
each acre of _beans_ 2 hours of work are needed. The farmer has 240 hours of work
available but it costs 200$ for every hour. The maximum demand is limited by the
market at a maximum of _480 sacks of corn_ sold by 150$ each and _800 sacks of
beans_ sold by 120$ each. Which cereal should the farmer grow to have the maximum
profit ?


### Problem modeling {#problem-modeling}

To model the problem, we need to extract the 3 main characteristics of the
problem, determine the variables, determine it's restrictions and calculate the
objective function.


#### Variables {#variables}

Variables are everything that you can work on the problem, they are the moving
parts and the input of the _objective function_.

In the case of the proposed problem we have two variables, acres of _corn_ and
_beans_ that will be cultivated. For brevity, let's call _corn_ \\(x\\) and _beans_ \\(y\\).


#### Objective function {#objective-function}

It shows our target function to archive, it can be a **maximization** or
**minimization** of the result of the function \\(Z\\), or in very rare cases, the
objective is to approximate \\(Z\\) to a certain value. The objective function is
created to reflect the impact of the variables on the outcome. In other words,
based on the variable values, it output has to represent the outcome in the real
world.

For the objective function of the example case above, the main objective is
**maximum profit**, it means to maximize the output of the function that given the
amount of _corn_ and _beans_ calculate the profit. We can define what profit is by
the \\(Profit = Sell Price - Costs\\).

So:

\\[ Z(x,y) = (150 \times 8 \times x) + (120 \times 10 \times y) - (200 \times 3 \times x) - (200 \times 2 \times y) \\]

Let's break it down in some chunks and analyse it:

-   The amount of money obtained for each acre of _corn_ (named \\(x\\)) grown: \\((150 \times 8 \times x)\\)
-   The amount of money obtained for each acre of _beans_ (named \\(y\\)) grown: \\((120 \times 10 \times y)\\)

Then we subtract the costs of cultivating those crops, considering that each
work hour costs \\(200\\) dollars:

-   The cost of cultivating one acre of _corn_ \\((200 \times 3 \times x)\\)
-   The cost of cultivating one acre of _beans_ \\((200 \times 2 \times y)\\)

We can optimize it by writing:

\\[ Z(x,y) = (1200 \times x) + (1200 \times y) - (600 \times x) - (400
\times y) \\]

And again:

\\[ Z(x,y) = (600 \times x) + (800 \times y)\\]


#### Restrictions {#restrictions}

Restrictions are any restriction that we need to apply to our variables. The
amount of resources, time, effort, etc... One common restriction considering
cases where we are applying linear programming to production is the **non
negativity** rule, it means, you can't produce -1 cars, all numbers of cars
produced must be positive or no car produced at all (zero cars).

> The maximization or minimization of the function \\(Z\\) will always end up with on
> restriction limiting it's result. So you can analyse that restriction and
> determine the bottleneck of your function. In case of all restrictions being
> reached it means that there was no bottleneck and all resources were utilized.

In the example problem we have some restrictions, it will be listed bellow:

-   100 acres available, it means \\(x+y \leq 100\\)
-   The market demand for _corn_ \\(8x \leq 480\\)
-   The market demand for _beans_ \\(10y \leq 800\\)
-   The labour limitation defined by $ 3x + 2y &le; 240$
-   And finally, the non negativity rule, that give us \\(x \geq 0\\) and \\(y \geq 0\\)


#### 100 acres available {#100-acres-available}

Since we are calculating with our variables \\(x\\) and \\(y\\) being the acres
cultivated, they directly represent it, so no transformation is needed.


#### The market demand for _corn_ {#the-market-demand-for-corn}

We are using acres as our base value, the demand of _corn_ is represented as the
amount of \\(x\\) times how many sacks of _corn_ each acre produces: \\(8x \leq 480\\)


#### The market demand for _beans_ {#the-market-demand-for-beans}

We are using acres as our base value, the demand of _beans_ is represented as the
amount of \\(y\\) times how many sacks of _beans_ each acre produces: \\(10y \leq 800\\)


#### The labour limitation {#the-labour-limitation}

The same logic applies here, since we are using acres as our base value, we
multiply the labor needed for each acre of each cereal, it means that _corn_ needs
\\(3\\) hours of labor, and _beans_ need \\(2\\) hours.


## Solving by hand with graphical method {#solving-by-hand-with-graphical-method}

We will apply the graphical solution here where the limitations are plotted so
is possible to determine the solution visually. Bellow is the result of the
above restrictions plotted in a graph.


#### Plot the graph {#plot-the-graph}

For all restrictions listed above, we will create a table with two lines, one
for the restriction result for the smallest value of \\(x\\) and the maximization of
the value \\(y\\), and the other for the opposite. As you can see, if there is only
one variable in the restriction the table is not needed, since we are looking
for the maximization of the use, it will result only on a straight line in the
graph. In the example case the limitations of the market can be seen in the
graph as perpendicular lines across their axis.

Since we are trying to maximize the resource usage, we remove the \\(\leq\\) and
replace it with an equal symbol.

For the labour time restriction \\(3x + 2y = 240\\)

| X  | Y   |
|----|-----|
| 0  | 120 |
| 80 | 0   |

It means that for this restriction you will draw a line from the point \\((0,120)\\)
to the point \\((80,0)\\). The are bellow the line, which for all elements there
this function is true, is called **feasible region**.

The second restriction is pretty straight forward, we will analyse the total
available area for the crops, which is given by the \\(x+y = 100\\).

| X   | Y   |
|-----|-----|
| 0   | 100 |
| 100 | 0   |

It means that you will draw a line from the point \\((0,100)\\) to the point
\\((100,0)\\).

The market demand for production of _corn_ \\(8x = 480\\), that gives us \\(x=60\\). The
market demand for production of _beans_ \\(10x = 800\\), that gives us \\(y=80\\). Both
will be represented by a straight line each on the given point.

With those restrictions calculated we can have some idea of the dimension of the
graph that we are going to plot. Since our max value for \\(y\\) is 120 (labour
restriction) and for \\(x\\) is 100 (total available area). Also adding a little bit
of interpretation to this graph, we can tell that if we only grow corn crops, we
won't be able to use all land that the farmer have, since the bottleneck in this
case will be the labor available.

Here is what the graph should look like after it is plotted.

-   Colored in **orange** the 100 acres available, it means \\(x+y \leq 100\\)
-   Colored in **red** The labour limitation defined by $ 3x + 2y &le; 240$
-   Colored in **purple** the market demand for _corn_ \\(8x \leq 480\\)
-   Colored in **blue** the market demand for _beans_ \\(10y \leq 800\\)

    <iframe src="https://www.desmos.com/calculator/qb0rwtlecb?embed" width="500px" height="500px" style="border: 1px solid #ccc" frameborder=0></iframe>


#### Intersection points {#intersection-points}

After plotting the restriction functions we have what is called **feasible region**,
a region of the graph that give possible solutions for our problem based on the
restrictions only. The second step is to determine which point in this region
maximizes or minimizes the result for the objective function \\(Z\\).

The essence of this method is to create a visual analysis of those points of
intersection which are called **corner points**. If the problem has a solution, this
solution will be one of those corner points.

In the example we have **5 intersection points**, they will be presented based on
which restriction they intersect or 0, to make things easier to reference later,
we will name those points with letters.

-   A) 0 and **demand for beans**;
-   B) **demand for beans** and **available area**;
-   C) **available area** and **available labor**;
-   D) **available labor** and **demand for corn**
-   E) **demand for corn** and 0;

Next step is to compile a table with all points and their values or \\(x\\) and \\(y\\).
But to be able to work with that we need to solve the equations to know their
values at their intersection point.

Points **A** and **E** won't require any special effort since they have a know value in
one of their axis.

<!--list-separator-->

-  Point B

    Point **B** is the intersection between the demand of beans \\(y=80\\) and the available
    area \\(x+y \leq 100\\). So we just solve the system

    \\[ x + y = 100 \\]

    Replacing \\(y\\) with it's value.

    \\[ x + 80 = 100 \\]

    And

    \\[ x = 100 - 80 \\]

    It gives us the point \\(x=20\\) and \\(y=80\\) \\((20,80)\\).

<!--list-separator-->

-  Point C

    Point **C** is the intersection between the available labor \\(3x+2y \leq 240\\) and the
    available area \\(x+y \leq 100\\). So we just solve the system

    \\[ 3x+2y = 240 \\]

    \\[ x+y = 100 \\]

    We need to isolate one factor, so let's isolate \\(y\\) in the second
    equation.

    \\[ x+y = 100 (\times -2) \\]

    And making one big equation we will have

    \\[ 3x +2y -2x -2y = 240 - 200 \\]

    \\[ x = 40 \\]

    Now that we have the \\(x\\) value, we just need to replace it in any of
    this two equations and we will have the \\(y\\) value for that point.

    \\[ 40+y=100 \\]

    \\[ y=60 \\]

    It gives us the point \\(x=40\\) and \\(y=60\\) \\((40,60)\\).

<!--list-separator-->

-  Point D

    Point **D** is the intersection between the available labor \\(3x+2y \leq 240\\) and the
    demand for corn \\(x=60\\). So we just solve the system by replacing \\(x\\)

    \\[ 180 + 2y = 240 \\]

    \\[ 2y = 240 - 180 \\]

    \\[ y = 30 \\]

    It gives us the point \\(y=30\\) and \\(x=60\\) \\((60,30)\\).

<!--list-separator-->

-  Corner points table

    Now that all points are calculated, just replace the \\(x\\) and \\(y\\) symbols by
    their values on the table bellow and calculate the objective function with it.
    It will give the output for those variables, and using this output if our
    objective is to maximize the result of the function, we will take the biggest
    value on the table as the optimal value, if the objective is to minimize, we
    take the smallest, simple as that.

    Given the objective function

    \\[ Z(x,y) = (600 \times x) + (800 \times y)\\]

    | Point | x  | y  | Objective Function |
    |-------|----|----|--------------------|
    | A     | 0  | 80 | 64000              |
    | B     | 20 | 80 | 76000              |
    | C     | 40 | 60 | 72000              |
    | D     | 60 | 30 | 60000              |
    | E     | 60 | 0  | 36000              |


### Conclusion {#conclusion}

Based on the table in the last section we can determine that the **optimal** area
for the maximization of the profit is **20 acres of corn** and **80 acres of beans**,
which will give a **profit of 76000$**.

This is enough, but we can look further and determine the bottlenecks, in other
words, what is limiting the maximization of the objective function. In this
example, this is a point of the analysis that gives the answer about what should
be worked on to improve the profit.


#### Bottleneck analysis {#bottleneck-analysis}

To determine which restrictions are limiting the objective function, just
analyse the values of \\(x\\) and \\(y\\), if restrictions match the value it means that
this restriction is limiting the best outcome.

Applying our example

<!--list-separator-->

-  Available area

    All available area was used, since \\[ 20+80 = 100 \\]

<!--list-separator-->

-  Demand for corn

    The market demand for corn was not met, it means that if more corn was produced,
    it would be sold.

    \\[ 8 \times 20 \leq 480 \\]

<!--list-separator-->

-  Demand for beans

    The market demand for beans was met, it means that even if more beans were
    produced, they won't be sold and won't generate any profit.

    \\[10 \times 80 = 800\\]

<!--list-separator-->

-  Labor limitation

    Still 20 hours of labor remaining after all the production, it can be determined
    by:

    \\[ 3 \times 20 + 2 \times 80 \leq 240 \\]

    \\[ 220 \leq 240 \\]


## Solving example 1 with python {#solving-example-1-with-python}

For solving this problem with python we are going to use `PuLP`. To setup `PuLP` on
Debian is easy, just `pip3 install pulp` and that is it. If you are using `Poetry`,
just run `poetry add pulp`, or if you are using the `Poetry` setup in this
repository, it is already installed.


### Modeling the problem {#modeling-the-problem}

For modeling this problem using `PuLP` basically we will need to import it and
create a problem:

```python
import pulp
problem = pulp.LpProblem("Farmer", pulp.LpMaximize)
```

Then we can add our variables to the problem, note that the restrictions based
on variable values are mapped here, so the non negativity rule and all others
based on the range of values should be applied at this point.

-   The minimum bound of a variable is defined by the `lowBound` parameter.
-   The maximum bound of a variable is defined by the `upBound` parameter.

Continuing our example, to create the \\(x\\) and \\(y\\) variables

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

```text
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


### Solving the problem {#solving-the-problem}

After the problem is modelled we can run it to make PuLP find a solution for us
by calling the `solve()` method in the problem object.

```python
problem.solve()
```

And check the status of the solution passing the `problem.status` variable to the
`PuLP` array that contains all the status codes:

```python
pulp.LpStatus[problem.status]
```

As you can check in this problem, the output was `Optimal`, which means that it
found the optimal solution. Depending on the problem status, several outputs can
be shown:

-   **Not Solved**: The problem status when it is created, before calling
    `problem.solve()` method.
-   **Optimal**: The optimal solution has been found.
-   **Infeasible**: There are no feasible solutions, maybe a contradiction in the
    problem definition, or a range of variables that can't exist like define two
    restrictions, one being \\(x \leq 10\\) and the other \\(x \geq 20\\)
-   **Unbounded**: There are no upper or lower bound to the variables, so the solution
    tend to the positive or negative infinite.
-   **Undefined**: Maybe there is an optimal solution but it may not have been found.


### Getting the solution {#getting-the-solution}

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

As you can check, we modelled the _corn_ as being the \\(x\\) variable, and the
optimal solution given by `PuLP` matches the optimal solution that we found by
hand. The same occurs to the _beans_ that we modelled as \\(y\\) variable.

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

As you can check, the very same solution that we found by hand. Here is the
complete source code:

```python
import pulp
problem = pulp.LpProblem("Farmer", pulp.LpMaximize)
x = pulp.LpVariable('x', lowBound=0, cat='Continuous')
y = pulp.LpVariable('y', lowBound=0, cat='Continuous')
problem += 600 * x + 800 * y, "Z"
problem += x + y <= 100
problem += 8 * x <= 480
problem += 10 * y <= 800
problem += 3 * x + 2 * y <= 240
problem.solve()

print("Problem status: " + pulp.LpStatus[problem.status])
print("Optimal corn amount to grow: "+str(x.value()))
print("Optimal beans amount to grow: "+str(y.value()))
print("By growing them the profit will be: "+str(pulp.value(problem.objective)))
```


## Solving the example 1 by hand with tableau simplex method {#solving-the-example-1-by-hand-with-tableau-simplex-method}

To make it possible to solve a linear programming problem using the tableau
simplex method, the first thing to be done is to rearrange the problem into the
**standard form**.


### Modeling example 1 in the standard form {#modeling-example-1-in-the-standard-form}

In the standard form **restriction equations** can't be written as inequalities, for
example \\(x <= 10\\) is an inequality, and should be written as \\(x = 10\\). To make
this transformation valid, we have to add another variable to the equation, this
will be our **slack variable** \\(fn\\), so the equation will be rewritten as \\(x + f1 =
10\\).

If it is an \\(\leq\\) restriction, the \\(fn\\) variable is **added** to the equation, the
opposite is also true, if the restriction is a \\(\geq\\) restriction, the \\(fn\\)
variable is **subtracted** from the equation.


#### In case of a subtraction {#in-case-of-a-subtraction}

For every slack variable that is subtracted, an artificial variable should be
added \\(a\\) this variable is used to give an initial solution to the problem.
Also, an artificial objective function \\(W\\) should be added, which initially is
represented as:

\\(W= a\_1 + a\_2 + a\_3 + ... + a\_n\\)

But before writing the \\(W\\) function we have to rewrite it as an expression using
the problem variables instead of the artificial variables.

For example consider 3 restrictions:

-   \\(3x + 1y - f1 + a1 = 12\\)
-   \\(3x + 4y - f2 + a2 = 30\\)
-   \\(2x + 7y - f3 + a3 = 28\\)

We isolate the artificial variable \\(a\\) as:

-   \\(a1 = 12 - 3x - 1y + f1\\)
-   \\(a2 = 30 - 3x - 4y + f2\\)
-   \\(a3 = 28 - 2x - 7y + f3\\)

Then the initial \\(W = a1 + a2 + a3\\) that will be rewritten as:

\\(W = (12 - 3x -1y + f1)+(30 - 3x -4y +f2)+(28 -2x -7y +f3)\\)

\\(W = 70 -8x -12y + f1 + f2 + f3\\) \\(W + 8x + 12y -f1 -f2 -f3 = 70\\)

Then the \\(W\\) objective function is used in the first phase of this resolution
instead of the original objective function \\(Z\\).


#### Continuing {#continuing}

All values presented in the right side of the equal sign must be constant, it
include the objective function \\(Z\\). So any term in any equation in the right
side that isn't constant should be transfered to the left side of the equation.

The restrictions can be translated into the following equations:

-   \\(x + y + f1 = 100\\)
-   \\(3x + 2y + f2 = 240\\)
-   \\(y + f4 = 80\\)
-   \\(x + f3 = 60\\)
-   \\(x,y,f1,f2,f3,f4 \geq 0\\)

With the objective function being translated into:

\\(Z - 600x - 800y = 0\\)


### Table modeling {#table-modeling}

The tableau simplex method is based on tables, where each table represents a
possible solution to the problem, it doesn't mean that every table found is an
optimal solution for the problem, but _is a solution_. This table is called **basic
feasible solution (BFS)**.

For every table we will have variables with _positive values_ called **basic
variables** and _null_ variables (with their value being \\(0\\)) denominated **non-basic
variables**. **The number of basic variables in a problem is equivalent to the
number of restrictions**.

For every equation, the value in the **right side of the equal sign is called
Right Hand value**.

For every restriction, there will be a line in the table and after it another
line for the objective function \\(Z\\). The values of the **non-basic** variables will
be added accordingly with their respective values in the restriction that they
represent.

For this example, the first table will look like:

| Basic Variable | x    | y    | f1 | f2 | f3 | f4 | Right Hand |
|----------------|------|------|----|----|----|----|------------|
| \\(f1\\)       | 1    | 1    | 1  | 0  | 0  | 0  | 100        |
| \\(f2\\)       | 3    | 2    | 0  | 1  | 0  | 0  | 240        |
| \\(f3\\)       | 1    | 0    | 0  | 0  | 1  | 0  | 60         |
| \\(f4\\)       | 0    | 1    | 0  | 0  | 0  | 1  | 80         |
| \\(Z\\)        | -600 | -800 | 0  | 0  | 0  | 0  | 0          |


### Table solving {#table-solving}

The initial table state is the initial problem state, where no action has been
taken, even solution will result in a new table after the calculations have
done. To determine if the current table is an optimal solution there are two
rules:

-   No **right hand** value can be negative.
-   In the case of a **maximization problem**, no value in the objective \\(Z\\) line can
    be negative. In the opposite case, a **minimization problem** the opposite is also
    true, we have an optimal solution if we only have any \\(n \leq 0\\) values.

The very first step to solve the table is to pick a **pivot column**, a column which
will be the base for the calculation of the next table. So we choose the column
(variable) that has more impact (has the smallest value) on the \\(Z\\) function, in
this case the \\(y\\) column where the impact is \\(-800\\).

The second step is to choose the **pivot line** which means **which restriction will
be exhausted**. So, for every value in the column, it will be checked against
every restriction to determine which one will result in more performance for the
\\(Z\\) function.

Using our example problem:

-   Line 1, \\(100 / 1 = 100\\)
-   Line 2, \\(240 / 2 = 120\\)
-   Line 3, will generate a division by zero in the \\(y\\) column, it means that this
    line and column combination won't affect the current situation.
-   Line 4, \\(80 / 1 = 80\\)

Next step is define the **pivotal line**, this line means the best current move to
explore so we can archive the desired goal for our objective function \\(Z\\). The
line is chosen based on the smallest value on the list above, in this case, the
line 4 with the value \\(80\\).

| Basic Variable | x    | y    | f1 | f2 | f3 | f4 | Right Hand |
|----------------|------|------|----|----|----|----|------------|
| \\(f1\\)       | 1    | 1    | 1  | 0  | 0  | 0  | 100        |
| \\(f2\\)       | 3    | 2    | 0  | 1  | 0  | 0  | 240        |
| \\(f3\\)       | 1    | 0    | 0  | 0  | 1  | 0  | 60         |
| \\(f4\\)       | 0    | 1    | 0  | 0  | 0  | 1  | 80         |
| \\(Z\\)        | -600 | -800 | 0  | 0  | 0  | 0  | 0          |

After that, the next step is to **divide** the whole pivot line by the value on the
**pivot column**. And calculate the new values for the other lines by subtracting
the chosen variable, in this case \\(y\\) by the value that we set in the pivot
line, as following:

The new line 4 will be defined by \\(NewLine4 = Line4 / y\\), since \\(y\\) is 1, no
changes will happen.

Where \\(y=1\\), meaning the value in the intersection between the **pivot line and
column**. In the bellow examples, the \\(y\\) value mean the \\(y\\) value on the line of
the respective line being calculated and \\(NewLine4\\) is the value for that column
in the pivot line (Line 4).

-   Line 1, \\(NewLine1 = Line1 - y \times NewLine4\\)
-   Line 2, \\(NewLine2 = Line2 - y \times NewLine4\\)
-   Line 3, \\(NewLine3 = Line3 - y \times NewLine4\\)
-   Line \\(Z\\), \\(NewLineZ = LineZ - y \times NewLine4\\)

Making it more visual

| Basic Variable | x                            | y                            | f1                     | f2                        | f3                        | f4                        | Right Hand                 |
|----------------|------------------------------|------------------------------|------------------------|---------------------------|---------------------------|---------------------------|----------------------------|
| \\(f1\\)       | \\(1 - 1 \times 0\\)         | \\(1 - 1 \times 1\\)         | \\(1 - 1 \times 0\\)   | \\(0 - 1 \times 0\\)      | \\(0 - 1 \times 0\\)      | \\(0 - 1 \times 1\\)      | \\(100 - 1 \times 80\\)    |
| \\(f2\\)       | \\(3 - 2 \times 0\\)         | \\(2 - 2 \times 1\\)         | \\(0 - 2 \times 0\\)   | \\(1 - 2 \times 0\\)      | \\(0 - 2 \times 0\\)      | \\(0 - 2 \times 1\\)      | \\(240 - 2 \times 80\\)    |
| \\(f3\\)       | \\(1 - 0 \times 0\\)         | \\(0 - 0 \times 1\\)         | \\(0 - 0 \times 0\\)   | \\(0 - 0 \times 0\\)      | \\(1 - 0 \times 0\\)      | \\(0 - 0 \times 1\\)      | \\(60 - 0 \times 100\\)    |
| \\(y\\)        | 0                            | 1                            | 0                      | 0                         | 0                         | 1                         | \\(80\\)                   |
| \\(Z\\)        | \\(-600 - (-800 \times 0)\\) | \\(-800 - (-800 \times 1)\\) | \\(0 - 800 \times 0\\) | \\(0 - (-800 \times 0)\\) | \\(0 - (-800 \times 0)\\) | \\(0 - (-800 \times 1)\\) | \\(0 - (-800 \times 80)\\) |

Since the \\(y=1\\) this example isn't that illustrative as the next ones will be it
can seem a little confusing. Also we set the variable in the column as the
variable (Basic Variable) in the first column. This will be the resulting table:

| Basic Variable | x    | y | f1 | f2 | f3 | f4  | Right Hand |
|----------------|------|---|----|----|----|-----|------------|
| \\(f1\\)       | 1    | 0 | 1  | 0  | 0  | 0   | 20         |
| \\(f2\\)       | 3    | 0 | 0  | 1  | 0  | 0   | 80         |
| \\(f3\\)       | 1    | 0 | 0  | 0  | 1  | 0   | 60         |
| \\(y\\)        | 0    | 1 | 0  | 0  | 0  | 1   | 80         |
| \\(Z\\)        | -600 | 0 | 0  | 0  | 0  | 800 | 64000      |

> If still any negative value in the \\(Z\\) line, it means that we don't
> have the optimal solution yet.

The next column will be the \\(x\\) column, since is the only one left, and the
column will be calculated based on:

-   Line 1: \\(20 / 1 = 20\\)
-   Line 2: $80 / 3 = 26.66...$
-   Line 3: \\(60 / 1 = 60\\)

The smallest value belongs to the line 2, so this will be our pivot line. Since
again the value of \\(x\\) in the pivot line and column is one, the line 2 will be
kept the same.

| Basic Variable | x | y | f1  | f2 | f3 | f4  | Right Hand |
|----------------|---|---|-----|----|----|-----|------------|
| \\(x\\)        | 1 | 0 | 1   | 0  | 0  | 0   | 20         |
| \\(f2\\)       | 0 | 0 | 0   | 1  | 0  | 0   | 20         |
| \\(f3\\)       | 0 | 0 | 0   | 0  | 1  | 0   | 40         |
| \\(y\\)        | 0 | 1 | 0   | 0  | 0  | 1   | 80         |
| \\(Z\\)        | 0 | 0 | 600 | 0  | 0  | 800 | 64000      |

There are no more negative values in the \\(Z\\) line, so we archived the optimal
solution. The final result will be the variable noted in the first column (Basic
variable) with the value at the Right Hand, it will give \\(x=20\\) and \\(y=80\\).


## Example 2 {#example-2}

Since linear programming advances were due to the war, this example focus on the
following problem. Imagine that there is a tank production factory, where to
produce the tanks they need to cut some metal plates. Those plates come in 50cm
sheets, and can be cut in three ways, a 15cm cut, a 17.5cm cut and a 20cm cut.
The max allowed for any plates to be stored is 10 units per cut, it means that
if you can't produce 10 units of any measure above the required amount.

To finish the current tank is needed 32 plates of 15cm, 17 plates of 17.5cm and
21 plates of 20cm. How to cut the metal plates to minimize the loss and how many
metal plates will be needed ?


### Modeling the problem {#modeling-the-problem}

The current problem is a **minimization** problem. An uncut metal plate have 50cm
and can be cut in 3 ways, 15cm, 17.5cm and 20cm. So the first step is to
determine the combination of possibilities and their respective losses.


#### Variables {#variables}

This problem have only one variable, the amount of metal sheets cut under each
size. But how to determine the possibilities ?

<!--list-separator-->

-  Determine the possible arranges for the variables

    To determine the possibilities a simple combinatorial algorithm can answer how
    many different combinations and their respective losses.

    ```python
      def combination(available, cuts):
          solutions = []
          for cut in cuts:
              if available >= cut:
                  next = combination(available - cut, cuts)
                  if len(next) == 0:
                      solutions.append([cut])
                  else:
                      for possibilities in next:
                          possibilities.append(cut)
                          solutions.append(possibilities)
          return solutions

      combinations=list(set(map(tuple, map(sorted, combination(50, [15, 17.5, 20])))))
      for combination in combinations:
          print(str(combination) + " with loss of " + str(50-sum(combination)))
    ```

    It will output the combination of cuts that can be done for each 50cm metal
    plate as well how much metal will be lost with each combination.

    ```python
    (15, 15, 17.5) with loss of 2.5
    (20, 20) with loss of 10
    (15, 15, 15) with loss of 5
    (15, 15, 20) with loss of 0
    (17.5, 20) with loss of 12.5
    (15, 17.5, 17.5) with loss of 0.0
    ```

    That can be translated into the list bellow:

    -   \\(x\_1 = 15, 15, 15, Loss = 5\\)
    -   \\(x\_2 = 15, 15, 17.5, Loss = 2.5\\)
    -   \\(x\_3 = 15, 17.5, 17.5, Loss = 0.0\\)
    -   \\(x\_4 = 15, 15, 20, Loss = 0\\)
    -   \\(x\_5 = 17.5, 20, Loss = 12.5\\)
    -   \\(x\_6 = 20, 20, Loss = 10\\)


#### Restrictions {#restrictions}

-   The max spare cut plate is 10 units of each size.
-   minimum of 32 plates of 15cm
-   minimum of 17 plates of 17.5cm
-   minimum of 21 plates of 20cm

That using the variables above can be translated into:

-   Min on 15cm plates: \\(3 \times x\_1 + 2 \times x\_2 + 1 \times x\_3 \geq
      32\\)
-   Max on 15cm plates: \\(3 \times x\_1 + 2 \times x\_2 + 1 \times x\_3 \leq
      42\\)
-   Min on 17.5cm plates: \\(1 \times x\_2 + 2 \times x\_3 + 1 \times x\_5 \geq
      17\\)
-   Max on 17.5cm plates: \\(1 \times x\_2 + 2 \times x\_3 + 1 \times x\_5 \leq
      27\\)
-   Min on 20cm plates: \\(1 \times x\_4 + 1 \times x\_5 + 2 \times x\_6 \geq
      21\\)
-   Max on 20cm plates: \\(1 \times x\_4 + 1 \times x\_5 + 2 \times x\_6 \leq
      31\\)

And finally the **non negativity** rule: \\(x\_i \geq 0\\)


### Objective function {#objective-function}

Since the problem is based on the **minimization** of loss, the output value of \\(Z\\)
function is based on the loss of each cut.

\\(Z = 5 \times x\_1 + 2.5 \times x\_2 + 0 \times x\_3 + 0 \times x\_4 + 12.5
\times x\_5 + 10 \times x\_6\\)

For keep the explanation clear and straight to the point, all above formulas
weren't optimized in any way.

```python
import pulp
problem = pulp.LpProblem("Tank", pulp.LpMinimize)
```

Then we create the \\(x\\) variables as integers (`cat=Integer`).

```python
x_1 = pulp.LpVariable('x_1', lowBound=0, cat='Integer')
x_2 = pulp.LpVariable('x_2', lowBound=0, cat='Integer')
x_3 = pulp.LpVariable('x_3', lowBound=0, cat='Integer')
x_4 = pulp.LpVariable('x_4', lowBound=0, cat='Integer')
x_5 = pulp.LpVariable('x_5', lowBound=0, cat='Integer')
x_6 = pulp.LpVariable('x_6', lowBound=0, cat='Integer')
```

Next step is just transcribe the \\(Z\\) function and the restrictions as python
code:

```python
problem += (5 * x_1) + (2.5 * x_2) + (0 * x_3) + (0 * x_4) + (12.5 * x_5) + (10 * x_6), "Z"
problem += (3 * x_1) + (2 * x_2) + x_3 >= 32
problem += (3 * x_1) + (2 * x_2) + x_3 <= 42
problem += x_2 + (2 * x_3) + x_5 >= 17
problem += x_2 + (2 * x_3) + x_5 <= 27
problem += x_4 + x_5 + (2 * x_6) >= 21
problem += x_4 + x_5 + (2 * x_6) <= 21
```

Then just solve it calling `problem.solve()` function and print the results.

```python
problem.solve()

print("problem status: " + pulp.LpStatus[problem.status])
print("Optimal amount to cut into x_1 = [15,15,15]: "+str(x_1.value()))
print("Optimal amount to cut into x_2 = [15,15,17.5]: "+str(x_2.value()))
print("Optimal amount to cut into x_3 = [15,17.5,17.5]: "+str(x_3.value()))
print("Optimal amount to cut into x_4 = [15,15,20]: "+str(x_4.value()))
print("Optimal amount to cut into x_5 = [17.5,20]: "+str(x_5.value()))
print("Optimal amount to cut into x_6 = [20,20]: "+str(x_6.value()))
print("The total metal loss is: "+str(pulp.value(problem.objective)))

plate15 = (3 * x_1.value()) + (2 * x_2.value()) + x_3.value()
plate17 = x_2.value() + (2 * x_3.value()) + x_5.value()
plate20 = x_4.value() + x_5.value() + (2 * x_6.value())

print("Total of 15cm plates "+str(plate15))
print("Total of 17.5cm plates "+str(plate17))
print("Total of 20cm plates "+str(plate20))
```

Bellow the whole code:

```python
import pulp
problem = pulp.LpProblem("Tank", pulp.LpMinimize)
x_1 = pulp.LpVariable('x_1', lowBound=0, cat='Integer')
x_2 = pulp.LpVariable('x_2', lowBound=0, cat='Integer')
x_3 = pulp.LpVariable('x_3', lowBound=0, cat='Integer')
x_4 = pulp.LpVariable('x_4', lowBound=0, cat='Integer')
x_5 = pulp.LpVariable('x_5', lowBound=0, cat='Integer')
x_6 = pulp.LpVariable('x_6', lowBound=0, cat='Integer')
problem += (5 * x_1) + (2.5 * x_2) + (0 * x_3) + (0 * x_4) + (12.5 * x_5) + (10 * x_6), "Z"
problem += (3 * x_1) + (2 * x_2) + x_3 >= 32
problem += (3 * x_1) + (2 * x_2) + x_3 <= 42
problem += x_2 + (2 * x_3) + x_5 >= 17
problem += x_2 + (2 * x_3) + x_5 <= 27
problem += x_4 + x_5 + (2 * x_6) >= 21
problem += x_4 + x_5 + (2 * x_6) <= 21
problem.solve()

print("problem status: " + pulp.LpStatus[problem.status])
print("Optimal amount to cut into x_1 = [15,15,15]: "+str(x_1.value()))
print("Optimal amount to cut into x_2 = [15,15,17.5]: "+str(x_2.value()))
print("Optimal amount to cut into x_3 = [15,17.5,17.5]: "+str(x_3.value()))
print("Optimal amount to cut into x_4 = [15,15,20]: "+str(x_4.value()))
print("Optimal amount to cut into x_5 = [17.5,20]: "+str(x_5.value()))
print("Optimal amount to cut into x_6 = [20,20]: "+str(x_6.value()))
print("The total metal loss is: "+str(pulp.value(problem.objective)))

plate15 = (3 * x_1.value()) + (2 * x_2.value()) + x_3.value()
plate17 = x_2.value() + (2 * x_3.value()) + x_5.value()
plate20 = x_4.value() + x_5.value() + (2 * x_6.value())

print("Total of 15cm plates "+str(plate15))
print("Total of 17.5cm plates "+str(plate17))
print("Total of 20cm plates "+str(plate20))
```

It will output the result of the problem:

```text
problem status: Optimal
Optimal amount to cut into x_1 = [15,15,15]: 6.0
Optimal amount to cut into x_2 = [15,15,17.5]: 1.0
Optimal amount to cut into x_3 = [15,17.5,17.5]: 13.0
Optimal amount to cut into x_4 = [15,15,20]: 21.0
Optimal amount to cut into x_5 = [17.5,20]: 0.0
Optimal amount to cut into x_6 = [20,20]: 0.0
The total metal loss is: 32.5
Total of 15cm plates 33.0
Total of 17.5cm plates 27.0
Total of 20cm plates 21.0
```


## Conclusion {#conclusion}

This is just an introduction to solving these kind of problems. If you
are interested into getting more info, there are several books out there
about it.

[If you think that you can help make this post better, send me a PR](https://github.com/opsxcq/blog/blob/master/content/post/linear-programming.md)


## References {#references}

-   [Feasible Region](https://en.wikipedia.org/wiki/Feasible_region)
-   [PuLP Homepage](https://pythonhosted.org/PuLP/)
-   [PuLP Repository](https://github.com/coin-or/pulp)
-   [Simplex Algorithm](https://en.wikipedia.org/wiki/Simplex_algorithm)
-   [Tableau Simplex](http://math.uww.edu/~mcfarlat/s-prob.htm)
-   [The Simplex Method: Step by Step with Tableaus](https://en.proft.me/media/science/sm3_ams_jhu_edu.pdf)
-   [The Simplex Method in Tabular Form](https://www.utdallas.edu/~scniu/OPRE-6201/documents/LP06-Simplex-Tableau.pdf)
-   [Lecture on Simplex method](http://www.unc.edu/depts/stat-or/courses/provan/STOR614_web/lect03_simplex.pdf)
-   [PERT page wikipedia](https://en.wikipedia.org/wiki/Program_evaluation_and_review_technique)


## Bibliography {#bibliography}

For further reading on this topic the book _Linear programming and extensions_ by
George Dantzig is recommended.
