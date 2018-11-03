#!/usr/bin/env python3

from random import randint
from time import sleep
import matplotlib.pyplot as plt


class World:

    def __init__(self, size):
        self.size = size
        self.x = 0
        self.y = 0
        r = range(size)
        self.grid = [[self.randomIsDirty() for x in r] for y in r]
        self.dirtyCount = sum(sum(e) for e in self.grid)

    def updatePosition(self, x, y):
        self.x = x
        self.y = y

    def canGoUp(self):
        return self.x != 0

    def canGoDown(self):
        return self.x < self.size - 1

    def canGoLeft(self):
        return self.y != 0

    def canGoRight(self):
        return self.y < self.size - 1

    def randomIsDirty(self):
        return 0 if randint(0, 9) < 9 else 1

    def isClean(self, x, y):
        return self.grid[x][y] == 0

    def isEverythingClean(self):
        return self.dirtyCount == 0

    def clean(self, x, y):
        self.grid[x][y] = 0
        self.dirtyCount = self.dirtyCount - 1

    def render(self):
        print(self)

    def __repr__(self):
        data = ""
        for x, line in enumerate(self.grid):
            data = data + "|"
            for y, c in enumerate(line):
                if self.x == x and self.y == y:
                    data = data + "  [" + str(c) + "]"
                else:
                    data = data + "   " + str(c) + " "
            data = data + " |\n"
        return data


class GraphicalWorld(World):

    def __init__(self, size):
        super().__init__(size)

    def render(self):
        matrix = [l[:] for l in self.grid]
        matrix[self.x][self.y] = 2
        plt.imshow(matrix)
        plt.show(block=False)
        plt.pause(0.005)
        plt.clf()
        super().render()


class Cleaner:

    def __init__(self, world):
        self.world = world
        self.actionCount = 0
        self.x = 0
        self.y = 0

    def action(self):
        agentAction = self.percept(self.world, self.x, self.y)
        if agentAction:
            agentAction()
            self.world.updatePosition(self.x, self.y)
            self.actionCount = self.actionCount + 1
        return agentAction

    def isDone(self):
        return True

    def canClean(self):
        return not self.world.isClean(self.x, self.y)

    def actionMoveUp(self):
        self.x = self.x - 1

    def actionMoveDown(self):
        self.x = self.x + 1

    def actionMoveLeft(self):
        self.y = self.y - 1

    def actionMoveRight(self):
        self.y = self.y + 1

    def actionClean(self):
        self.world.clean(self.x, self.y)

    def actionNothing(self):
        pass


class ReactiveCleaner(Cleaner):

    def __init__(self, world):
        self.down = True
        super().__init__(world)

    def percept(self, world, x, y):
        if self.canClean():
            return self.actionClean
        if self.down:
            if world.canGoDown():
                return self.actionMoveDown
            self.down = False
        else:
            if world.canGoUp():
                return self.actionMoveUp
            self.down = True
        if world.canGoRight():
            return self.actionMoveRight
        return self.actionNothing

    def isDone(self):
        if self.canClean():
            return False
        if self.world.canGoRight():
            return False
        if self.down:
            return not self.world.canGoDown()
        else:
            return not self.world.canGoUp()
        return False


class UtilityCleaner(Cleaner):

    def __init__(self, world):
        self.actions = []
        super().__init__(world)

    def percept(self, world, x, y):
        if len(self.actions) > 0:
            return self.actions.pop(-1)

        if self.canClean():
            return self.actionClean

        e = enumerate
        g = self.world.grid
        dirty = [self.getMoveActions(self.x, self.y, x, y) for x,l in e(g) for y,c in e(l) if c == 1]
        if dirty:
            self.actions.extend(min(dirty, key=len))
            return self.actions.pop(-1)

        return self.actionNothing

    def getMoveActions(self, cx, cy, x, y):
        if cx > x:
            return [self.actionMoveUp] + self.getMoveActions(cx - 1, cy, x, y)
        if cx < x:
            return [self.actionMoveDown] + self.getMoveActions(cx + 1, cy, x, y)

        if cy > y:
            return [self.actionMoveLeft] + self.getMoveActions(cx, cy - 1, x, y)
        if cy < y:
            return [self.actionMoveRight] + self.getMoveActions(cx, cy + 1, x, y)

        return []

    def isDone(self):
        return self.world.isEverythingClean()


if __name__ == "__main__":
    world = GraphicalWorld(50)
    #agent = ReactiveCleaner(world)
    agent = UtilityCleaner(world)
    world.render()
    sleep(6)
    while not agent.isDone():
        print(agent.action())
        world.render()
    sleep(5)
