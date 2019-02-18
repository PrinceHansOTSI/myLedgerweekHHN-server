# myLedgerweekHHN-server

## Quick Start
### Dependencies
- Flask
- Docker

```sh
// build and run docker container
$ docker build . -t hhnapp_db:latest
$ docker run --rm -d -v $(pwd)/certs:/var/lib/mysql -p 127.0.0.1:3306:3306 hhnapp_db
// setup flask env
$ export FLASK_APP=server.py
$ flask run
```

If you want to use mySQL-cli in the docker container...
```sh
$ mysql -h 127.0.0.1 -u root -p HHNAPP
```