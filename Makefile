
docker-build:
	docker build -t j0nn/pelican .
	#mkdir website/content
	#mkdir website/output
docker-kill:
	docker stop pelican
	docker rm pelican

docker-run:
	docker run --name="pelican" --network="proxy" -d -v $(CURDIR)/website:/srv/pelican-website -l traefik.frontend.rule=Host:j0nn.com,www.j0nn.com -l "traefik.frontend.redirect.regex=^https?://www.j0nn.com/(.*)" -l "traefik.frontend.redirect.replacement=https://j0nn.com/$${1}" -l traefik.port=80 -l traefik.docker.network=proxy -l traefik.enable=true j0nn/pelican

docker-bash:
	docker run --name="pelican" -i -t -v $(CURDIR)/website:/srv/pelican-website --network="proxy" -l traefik.domain="j0nn.com" -l traefik.frontend.rule="Host:j0nn.com,www.j0nn.com" -l traefik.docker.network=proxy j0nn/pelican /bin/bash
 

