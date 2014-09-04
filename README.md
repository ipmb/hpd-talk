Getting started:

Install Docker.
*Note: If you're on OS X, use `docker-osx` instead of `boot2docker` because https://github.com/boot2docker/boot2docker-cli/issues/202.*


```
pip install fig
fig -f fig/{runserver,uwsgi,varnish}.yml up
# First time
fig -f fig/{runserver,uwsgi,varnish}.yml run web ./bin/manage.py migrate --noinput
fig -f fig/{runserver,uwsgi,varnish}.yml run web ./bin/manage.py fill_db
```

Servers are exposed on port 8080
