FROM python:alpine3.8 

RUN apk add --no-cache --update make \
	bash && \ 
    pip install --upgrade pelican Markdown ghp-import shovel

WORKDIR /srv/pelican-website

CMD PORT=80 make devserver
