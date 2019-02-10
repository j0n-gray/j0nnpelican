Title: My Traefik Configuration - Docker Reverse Proxy 
Date: 2019-01-09
tags: linux, DevOps

In this article I will run through my Traefik configuration, which currently handles routing and load-balancing (in future) to 22 docker containers (5+ wordpresses, prometheus and this blog).

My traefik setup consists of a .toml file and uses docker-compose. Firstly, looking at the docker-compose.yml

```
version: '2'

services:
  rnetwork:
    image: traefik:latest
    ports:
      - 80:80
      - 443:443
      - 8080:8080
    networks:
      - network
      - metric
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - /opt/traefik/traefik.toml:/traefik.toml
    container_name: traefik
    restart: always
networks:
  network:
    external: true
  prometheus:
    external:
     name: prometheus_backend
  bridge:
    external: true

```

so here we make a docker-compose which spins up traefik. the important thing to know is the networking aspect. traefik is mapped to an external network which you then add your other containers to. additionally we have another network configured which will be used for prometheus metrics. we have revealed 3 ports: 80, 8080 and 443. 8080 being the dashboard port. 

and the traefik.toml configuration:

```
defaultEntryPoints = ["http", "https"]
logLevel = "ERROR"

[api]
entryPoint = "traefik"
debug = true
dashboard = true
  [api.statistics]

[entryPoints]
  [entryPoints.traefik]
    address = ":8080"
  [entryPoints.traefik.auth.basic]
    users = ["bob:passwordbase64encoded."]
  [entryPoints.http]
    address = ":80"

[metrics]
  [metrics.prometheus]
    entryPoint = "traefik"
    buckets = [0.1,0.3,1.2,5.0]

[docker]
endpoint = "unix:///var/run/docker.sock"
domain = "j0nn.com"
watch = true
exposedbydefault = true
network = "network"

```

finally, let's look at an example containers docker-compose configuration. The example I took is thegoose.house, a gaming organization and community I manage the servers for 

```
   mysql: 
   labels:
    - traefik.enable=false
    volumes:
    - ./wordpressdbdump.sql:/docker-entrypoint-initdb.d/backup.sql.gz
    - db_data:/var/lib/mysql
    networks:
     - wordpress

   wordpress:
    image: wordpress
    restart: always
    environment:
    labels:
     - traefik.backend=wordpress
     - traefik.frontend.rule=Host:wordpresssite.org, www.wordpresssite.org
     - traefik.docker.network=network
     - traefik.port=80
     - traefik.enable=true
    volumes:
      - ./wordpress:/var/www/html
    networks:
      - network
      - wordpress
```


soon I will have a LetsEncrypt container working.


### sources / further reading:

1. [Traefik documentation](https://docs.traefik.io/basics/)
2. [Docker wordpress](https://hub.docker.com/_/wordpress/)
























































