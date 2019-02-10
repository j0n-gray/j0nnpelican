Title: Dockerizing Pelican 
Date: 2018-10-22 18:00
tags: linux, DevOps

I took some inspiration from an existing Pelican docker image, except I found that
the Dockerfile was a bit too bulky for my liking - I would also need to modify the Makefile to get the 
docker container be recognised and used by traefik as the reverse proxy.

For the Dockerfile I have tried to trim the image down as much as possible by using
Python's alpine image. This leaves us with a compact Dockerfile of minimal size:

```
FROM python:alpine3.8

RUN apk add --no-cache --update make \
        bash && \
    pip install --upgrade pelican Markdown ghp-import shovel

WORKDIR /srv/pelican-website

CMD PORT=80 make devserver

```
Using a MakeFile, we can add some aliases to make building and running
the container easy. For example:


```
docker-build:
        docker build -t j0nn/pelican .
docker-kill:
        docker stop pelican
        docker rm pelican

```

And to get this running with traefik we add an additional "docker-run" argument to the Makefile:

```
docker-run:
docker run --name="pelican" --network="network" -d -v $(CURDIR)/website:/srv/pelican-website -l traefik.frontend.rule=Host:hostname.com,www.hostname.com -l traefik.port=80 -l traefik.docker.network=network -l traefik.enable=true j0nn/pelican

```
we have successfully dockerized pelican!

### sources / further reading:

1. [jderuere/pelican](https://github.com/jderuere/docker-pelican)
2. [Docker Python Image](https://hub.docker.com/_/python/)
3. [Traefik documentation](https://docs.traefik.io/)
























































