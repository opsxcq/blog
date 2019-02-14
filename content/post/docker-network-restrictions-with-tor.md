---
title: "Docker network restrictions with Tor"
date: 02-14-19
draft: false
tags: ["docker", "devops", "tor", "anonimity"]
---

Image the following usecase, you have an application and want to for its
traffict through Tor, exclusively. If if is running on your computer like a
normal application, it is simple, just add some iptables rules. But in the
container world things are different, specially if you want to escalate it
through several machines.

Here will be explored an usecase of an isolated container that can only
communicate with a *proxy* container that has access to the Tor network. Suppose
that you don't trust that you application will keep the proxy configurations or
properly use it and you want to be sure that nothing wrong happen to your
privacy.

## Create the networks

The very first step is to create the networks used for this example. Let's give
them some self-explanatory names.

``` shellsession
docker network create internet
docker network create --internal restricted
```

As you can see, the *restricted* network is created with the `--internal` flag,
which means that it doesn't have any external access.

## Create the proxy container

Two containers will be created for this test, the first one is the *proxy*
server that will run Tor as a proxy.

``` shellsession
docker run --rm -it --name proxy --network internet -e PROXY_PORT=9050 strm/tor
```

In another terminal run

``` shellsession
docker run --rm -it --name client --network restricted strm/task-base
```

And finally attach the proxy container to the restricted network.

``` shellsession
docker network connect restricted proxy
```

## Testing

To be sure that the setup is properly working, the image used as the client
image already has `curl` installed, so is possible to run the following command.

```shell
root@a7534de5d6be:/data# curl -x socks5h://proxy:9050 google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

The next step is to be sure that the opposite also happens, that the *client*
container can't access the internet without the proxy. So you can use *ping*,
*curl* and other tools to test it.

# References

- [Tor image](https://github.com/opsxcq/docker-tor)
