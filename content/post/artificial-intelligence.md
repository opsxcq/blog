+++
date = "2018-09-12T00:00:00Z"
title = "Artificial Intelligence"
tags = ["artificial intelligence"]
draft = true
+++

# What is Artificial Intelligence ?

This is a hard question to ask, because not even among the experts there is a
complete agreement about what defines something as a real **artificial
intelligence.**

So it can be split between *acting* and *"thinking"*, and again between
*humanly* and *rationally*. Before you state that humans are rational, please
look carefully to this GIF

![humans](/img/ia-people-not-smart-01.gif)

So the combination of those aspects generate this four approaches generates:

 - Acting humanly
 - Thinking humanly
 - Thinking rationally
 - Acting rationally

## Acting humanly

By Kurzweil (1990)

> The art of creating machines that perform functions that require intelligence
> when performed by people.

By Rich and Knight (1991)

> The study of how to make computers do things at which, at the moment, people
> are better.

Can be considered the characteristic of a computer being able to act and pass as
a human being among others. The concept that a machine can fool a human into
thinking that it is really a human. As proposed by **Turing** in 1950, the
[**Turing test**](https://en.wikipedia.org/wiki/Turing_test) is a way to perform
this kind of assertion, if a machine can fool a group of humans into thinking
that they are talking with a human, so this machine can be considered to act in
a similar way to humans.

For the purpose of *intelligence* only, no physical interaction is needed, but
for the **total Turing test** it is, so it can include a video or a physical
construction (a robot basically) to interact with a group of humans. The actual
technology is too primitive to such test be necessary, but when it happens, you
can imagine a scene just like this from the **Blade Runner** movie:

![turing](/img/ia-turing-test-01.gif)

The whole movie is good mental exercise of what a real IA would look like and
all its dilemmas, they just renamed the Turing test to **Voigt-Kampff** test,
but the essence of the test stills the same.


## Thinking humanly

By Haugeland (1985)

> The exciting new effort to make computers think... machines with minds, in
> the full and literal sense.

By Hellman (1978)

> [The automation of] activities that we associate with human thinking,
> activities such as decision-making, problem solving, learning ...


## Thinking rationally

By Charniak and McDermott (1985)

> The study of mental faculties through the use of computational models.

By Winston (1992)

> The study of the computations that make it possible to perceive, reason, and
> act.

## Acting rationally

By Poole (1998)

> Computational Intelligence is the study of the design of intelligent agents.

By Nilsson (1998)

> AI... is concerned with intelligent behavior in artifacts.

# Artificial intelligent concepts and foundation

## Intelligent Agents

An agent is an autonomous entity which observes the **environment** and act
according with it. The perception of the environment comes from their
**sensors** and their interactions over the environment is made using
**actuators**. So basically **sensors are the agent sources of input** and
**actuators are their output**. Sometimes autonomous agents are called
**abstract intelligent agents (AIA)**.

Example of sensors:

 - Camera
 - Microphone
 - Files
 - `stdin`
 
Example of actuators:

 - Speakers
 - Engines
 - `stdout`

It is really similar to the concept of input and output in any software, if you
consider that stdin and stdout can be used as a sensor and actuator respectively
you may notice that it is far different from something like the replicants in
the Blade Runner movie, but if you take chat bots like
[ELIZA](https://en.wikipedia.org/wiki/ELIZA) as example, it make sense.

In between of the *input* and *output* of any computer program there is the
*processing* stage, so as you can expect, the same stage exists in the
implementation of autonomous agents. But one aspect differs them from the normal
computer programs, the agents must **adapt to environment changes**, it can be
interpreted as the machine learning to handle these changes, or just in a
reactive way change its behavior to fir the current situation (like the
difficulty level in a game).

The classic way to express the agent behavior is:

$f = P^{\star} \mapsto A$

Which means, given a sequence of perceptions that an agent can perceive
$P\raise0.5ex\hbox{*}$ , it is mapped to an action $A$.

By sequence of perceptions is meant the whole history of perceptions of that
agent. Which means the actual action may or may not depend on the whole sequence
of perceptions that this agent have perceived.

To illustrate this scenario we will study the classic example of the vacuum cleaner.


### Vacuum Cleaner example

Imagine a very limited world, composed only by two rooms and one agent, the
*vacuum cleaner**.

![vacuum01](/img/ia-vacuum-cleaner-01.png)

Inside this very limited environment we have the following actions that can be
executed by the agent:

 - Move left
 - Move right
 - Clean
 - Do nothing
 
And we have the perceptions:

 - Current room (A or B)
 - Room state (Clean or Dirty)
 
Given the above scenario, some expected actions based on the perceptions would be:

 - Perception (**Room=B** and **State=Dirty**), expected action **Clean**.
 - Perception (**Room=B** and **State=Clean**), expected action **Move to Room A**.
 - Perception (**Room=A** and **State=Dirty**), expected action **Clean**.
 - Perception (**Room=A** and **State=Clean**), expected action **Move to Room B**.

We will look further to expand the intelligence of this agent later in this post.

### Rational Agents

What means being rational ? What makes one person choices good or bad ? What
makes one person smart or dumb ? That can be quite relative based on several
aspects if we consider a complex scenario, like for example, autonomous cars.

Taking autonomous cars as example, not only the choices made have to be
considered, but the ethics of it, check [the Moral
Machines](http://moralmachine.mit.edu/) website to be exposed to some moral
dilemmas that AI can bring to people who create them. Like when the paramedics
choose which emergency they will respond first, there is no such thing as
respond everyone, the resources are limited and priorities must take place to
think rationally on emergency situations, to illustrate this example consider
the [Emergency Service response
codes](https://en.wikipedia.org/wiki/Emergency_service_response_codes). Back
again about autonomous cars, consider the image bellow, which one would you
rather to kill ?

![ethics](/img/ia-ethics-01.png)

In the picture, if you choose to change the car direction, all passengers will
die, if you don't, it will kill 3 homeless men and a woman.

This kind of dilemma start a whole debate about how much a life worth, and which
lives matter most. Rational agents usually don't require some thought decisions
like those exposed above, but always keep in mind the ethics and
responsibilities when designing agents.

### Determining the agent performance

Rationally thinking, what makes a choice good, not so good, neutral, bad, or
terrible is called `fitness function`. The fitness function will determine
whether or not your agent is doing a good job.

This function simplifies the real world to a simple score, that shows the
performance of your agent based on the problem that it is intended to solve. In
a small scenario like the vacuum cleaner robot is easy to create such function,
we can summarize it in a statement like *keep it clean with the least effort*.

For an artificial intelligence like those presented in the movies, it can be far
more complex, we can talk about happiness as being a fitness function, others
can use a more collectivist point of view and consider how much someone benefits
those around it as the fitness function. So the selfish robot would kill for an
ice cream, while the collectivist one would throw itself in the front of a bus
to stop so a random kid won't be late for school. Both approaches sound really
stupid if you look at them in this naive way, this is why the fitness function
is so complex for real world scenarios.

The main point of the fitness function is **to reflect the desired result** in
the agent behavior.

### Types Of Agents

Even agents sharing the same sensors and actuators can act very differently,
based on how they were implemented, according to Norvig and Russell these agents
can be categorized into five groups:

 - Simple Reflex Agents
 - Model Based Reflex Agents
 - Goal-based agents
 - Utility-based agents
 - Learning agents

Autonomous agents can also present characteristics from one or more of these
categories, like for example, be model-utility agents.

### Simple Reflex Agents 

![reactive](/img/ia-agent-reactive.png)

The most basic type of agent that can be implemented, it simply reacts to its
perceptions. Also called reactive agents because of the way that they operate,
just reacting to external events. Simple reflex agents acts only based on the
current perception, ignoring the whole perception history.

If the vacuum cleaner robot were implemented using this agent model a
pseudo-code will look like:

```python
def agent(world):
  if world.isDirty():
    clean()
  if world.currentRoom == 'A':
    moveToRoomB()
  else:
    moveToRoomA()
```

The problem with this approach is that don't take a lot to figure out that if
the whole environment is clean, the robot will be running from room A to B and
then from B to A forever.

> Simple reflex agents are suitable for environments where the processing power
> is really limited and just reacting to simple perceptions is enough

### Model Based Reflex Agents

![reactive](/img/ia-agent-reactive-model.png)

Model based reflex agents can keep track of the past perceptions using an
internal *model*. So future actions are the result of the current perception and
all the previous ones.

### Goal-based agents

![reactive](/img/ia-agent-goal.png)

Goal based agents, as the name suggests, are based on goals. These goals are the
target for their actions, it means, given a set of perceptions, choose the
action that will be better to archive the goal.

> Goal agents don't distinguish between goal states and non-goal states, there
> is no between.

### Utility-based agents

![reactive](/img/ia-agent-utility.png)

These agents are more complex and elaborated, can be described as an advanced
goal based agent. In utility based agents is possible to define how much you
want some desired goal, so the agent can choose the best action for that
situation. An utility based agent chooses the action that maximizes the expected
utility of their action.

Example, imagine a game like Mortal Kombat, where you want to create an agent to
fight against other players. While not being hit by the opponent is good, kill
the opponent is better and make you winner of the fight (objective state). Given
this scenario, considering that the opponent is near you, what is the optimal
move ? An utility based agent would calculate it based on several aspects.

 - If your energy level is low, and the opponent is higher, **Block**
 - If your energy level is high, and the opponent is low, **Attack**
 
This is obviously a simplification of the current scenario, but the idea is,
given that the end goal (win the fight) can be archived only if you don't lose
the fight, if your energy bar is low, better to protect yourself than risking
being hit while attacking the opponent. But the opposite is also true, while
avoiding damage is a goal, it can be sacrificed by risking being hit if you have
chances of winning the fight by hitting the opponent.

### Learning agents

![reactive](/img/ia-agent-learning.png)

As the name suggests, the learning agents can adapt to the environment where
they are. Based on perceptions they change their critic of the world and their
actions. The **critic is the crucial ingredient creating a learning agent**
because it gives the required feedback to the process.

Imagine a poker game, where initially you don't know the other players, but as
the game goes, you know that a certain player always bluff. If that player is
playing against a learning agent, at first the agent will believe in the bluff,
but after some games it will *learn* who bluff and will change its strategies to
defeat the other player (goal).

Other scenario are the adaptive adversarial NPCs in games, their objective is
not defeat the player, but give the desired level of difficulty
(Easy/Regular/Hard). So, if a given player keep dying, they change their
strategy to keep the game interesting, while these characters fight the
protagonist, is not the game goal (in this case) to make the player lose all the
time, using the *easy* mode as an example, if the player keep dying, the
internal mechanics change to a point where the enemies become weak in both
energy level and skills.

# Search methods

# Search methods based on heuristics

# Machine Learning and Neural Networks

# References

Russell Book

- [AI: A Modern Approach](http://aima.cs.berkeley.edu/)
- [EDX Course](https://www.edx.org/course/artificial-intelligence-ai-columbiax-csmm-101x-0)
