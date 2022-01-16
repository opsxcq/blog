+++
title = "Running Cron tasks on docker - The correct way"
author = ["OPSXCQ"]
date = 2018-09-06
draft = false
+++

While is perfectly possible to use _cron_ inside a container, I strongly
advise you to don't do it. Some of the most important points on why is a
**bad practice to run cron inside a container**:

<!--more-->


## Your tasks need to be ephemeral as your containers {#your-tasks-need-to-be-ephemeral-as-your-containers}

We live in the immutable infrastructure era, there is no need to worry about
cleaning up everything before or after your tasks run. Make your scheduled tasks
ephemeral as your containers, if something goes wrong, you can inspect the
precise state that the container was left. Even with Tasker supporting reusing
the container(`reuse: true`) this is not recommended.

Let your tasks be ephemeral as possible, you can always count on a clean
environment for every execution.


## Maintain custom images is time consuming {#maintain-custom-images-is-time-consuming}

This is the main point of using Tasker, imagine that you have 3 tasks to run,
one in Python, one in Javascript (nodejs) and the other is a backup tasks that
need the MongoDB command line tools. Using _cron_ would be needed to build 3
images, one for each task, adding the cron daemon to the base image, then
configuring your task and adding your scripts. After it is done, you need to
publish it, because your servers will need to pull this image to be able to run
it, so another step is giving access to it.

With Tasker, you simply use the images that are already available, no more extra
work required.


## No alerts when tasks fail {#no-alerts-when-tasks-fail}

Cron doesn't provide anything out of the box to alert about your tasks execution
status. Tasker in the other hand come with batteries included and ships alerting
out of the box, [here the official docs](https://github.com/opsxcq/tasker#notifications).


## Is hard to keep everything _as code_ {#is-hard-to-keep-everything-as-code}

Considering the first scenario, with 3 tasks each one with a image for each. If
you keep the good practices, you will create a git repository for each one, with
their own build. It means that you have 3 additional repositories to keep track
of.

With Tasker you can simply have one configuration file and replace all those
repositories with one repository.


## Introduction to Tasker {#introduction-to-tasker}

`Tasker` is a task scheduler and runner, it works by creating containers on demand
to run your task.

Let's use a practical example, considering the `docker-compose.yml` file bellow:

```yaml
version: "3"

services:
    tasker:
        image: strm/tasker
        volumes:
            - "/var/run/docker.sock:/var/run/docker.sock"
        environment:
              configuration: |
                  schedule:
                      - every: minute
                        task: hello
                  tasks:
                      docker:
                          - name: hello
                            image: debian:jessie
                            script:
                                - echo Hello world from Tasker
```

`Tasker` can be configured in several ways, one way is setting the environment
variable `configuration` and set it to your yml configuration. As you can notice,
it goes really well with the docker-compose file.

Let's break down the configuration to explain what is going on. We can break it
in two main sections, `schedule` and \`tasks\*\*.

**Schedules** are the triggers to our tasks, they are defined as an array of
`schedule`. These schedules are defined by two main properties, when they will
trigger the task, and what tasks they will trigger.

Another good point of Tasker is that you don't have to memorize some abstract
_cron_ syntax, it uses a more human language, like in this example `every: minute`,
it means every 1 minute this task will run. Test it, change to `every: 10 minutes`
and observe the results. You can also set it as a default _cron_ syntax.

More about scheduling can be found on the [official docs](https://github.com/opsxcq/tasker#scheduler)

The second element of the configuration (and the most important) are the **tasks**,
tasks defined under the `docker` property represent a **docker container
definitions**, they reflect the container that will be created when triggered and
will execute your commands. You can use any docker image to run your commands
into.

Here a more elaborate example to illustrate how you can use several images on
the same configuration

```yaml
version: "3"

services:
    tasker:
        image: strm/tasker
        volumes:
            - "/var/run/docker.sock:/var/run/docker.sock"
        environment:
            configuration: |
                logging:
                    level:
                        ROOT: WARN
                        org.springframework.web: WARN
                        sh.strm: DEBUG
                schedule:
                    - every: minute
                      task: hello
                    - every: minute
                      task: helloFromPython
                    - every: minute
                      task: helloFromNode
                tasks:
                    docker:
                        - name: hello
                          image: debian:jessie
                          script:
                              - echo Hello world from Tasker
                        - name: helloFromPython
                          image: python:3-slim
                          script:
                              - python -c 'print("Hello world from python")'
                        - name: helloFromNode
                          image: node:8
                          script:
                              - node -e 'console.log("Hello from node")'
```

Note that in this example, we have only one source file, but if you had to
replicate it using _cron_ you would had to create 3 images, one for each base
image + the cron daemon, and, or map your scripts to it, or copy it on the
build. After a while the maintenance required to keep everything updated will
consume a significant amount of time. This is one of the main scenarios where
Tasker simplifies a lot the work required.

Basically everything that you need to configure in a container, from **networking**,
**volumes**, and everything else can be done using this configuration section, for
more info [see the official docs](https://github.com/opsxcq/tasker#docker-tasks).


## References {#references}

-   [Tasker repository](https://github.com/opsxcq/tasker)
