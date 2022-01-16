+++
title = "Restricting Docker container networking to Tor only"
author = ["OPSXCQ"]
date = 2019-02-14
draft = false
+++

Image the following use case, you have an application running which you strictly
want to force its traffic to go through the **TOR** network. In normal case
scenarios, you can implement at your network firewall level a restriction to
such traffic, a more simplistic approach would be locally to add an `iptables`
rule, but in the container world everything is different.

<!--more-->

Here will be explored an use case of an isolated container that can only
communicate with a _proxy_ container that has access to the Tor network. Suppose
that you don't trust that you application will keep the proxy configurations or
properly use it and you want to be sure that nothing wrong happen to your
privacy.


## Create the networks {#create-the-networks}

The very first step is to create the networks used for this example. Let's give
them some self-explanatory names.

```bash
docker network create internet
docker network create --internal restricted
```

As you can see, the _restricted_ network is created with the `--internal` flag,
which means that it doesn't have any external access.


## Create the proxy container {#create-the-proxy-container}

Two containers will be created for this test, the first one is the _proxy_ server
that will run Tor as a proxy.

```bash
docker run --rm -it --name proxy --network internet -e PROXY_PORT=9050 strm/tor
```

In another terminal run

```bash
docker run --rm -it --name client --network restricted strm/task-base
```

And finally attach the proxy container to the restricted network.

```bash
docker network connect restricted proxy
```


## Testing {#testing}

To be sure that the setup is properly working, the image used as the client
image already has `curl` installed, so is possible to run the following command.

```bash
root@a7534de5d6be:/data# curl -x socks5h://proxy:9050 google.com
<HTML><HEAD><meta http-equiv="content-type" content="text/html;charset=utf-8">
<TITLE>301 Moved</TITLE></HEAD><BODY>
<H1>301 Moved</H1>
The document has moved
<A HREF="http://www.google.com/">here</A>.
</BODY></HTML>
```

The next step is to be sure that the opposite also happens, that the _client_
container can't access the internet without the proxy. So you can use _ping_, _curl_
and other tools to test it.


## References {#references}

-   [Tor image](https://github.com/opsxcq/docker-tor)
