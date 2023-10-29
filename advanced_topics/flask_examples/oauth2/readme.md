## Oauth2 example 
This is a simple example of oauth2 with flask, server and client. This follows the code flow of oauth2.

There are two docker images, one for the server and one for the client. The server is a flask app that exposes an endpoint to request authorization. The client is a flask app that exposes an endpoint to request the authorization code and another endpoint to request the access token.


### Dependencies

docker
docker-compose

### How to run

```bash
docker-compose up
```

or if docker compose was installed as plugin of docker

```bash 
docker compose up
```

optionally you can add the --build flag to force the build of the images

```bash
docker-compose up --build
```

### How to test

You can use postman or web browser

URL: http://localhost:8080/request_authorization

### How to stop

```bash
docker-compose down
```


