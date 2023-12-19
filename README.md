## Use
```
have api_key.json and credentials.json => /src/credentials/
```
## Test

```
docker exec -it flask_app  pwd
docker exec -it flask_app bash
```

## Run dockerfile

```
docker build -t pythonflask .
docker run -d -p 80:5000 --name flask pythonflask
docker rm -f flask
```

## Install new package

```
pip install pipenv
pipenv install package_name
docker system prune
docker system df


```

## Run docker-compose

```
docker-compose -f docker/docker-compose.yml build

docker-compose -f docker/docker-compose.yml up -d

docker-compose -f docker/docker-compose.yml up --build -d

docker exec -t flask_app python3 -m src.app

docker-compose -f docker/docker-compose.yml down

```

## Insomnia

```
localhost:80/get_info
Auth => API Key Auth 
                    => KEY: X-Api-Key
                       VALUE: ...............

localhost:80/process
localhost:80/write_info
localhost:80/sync_data
```