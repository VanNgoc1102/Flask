## Use

```
copy api_key.json and credentials.json to /src/credentials/
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
```


## Run docker-compose

```
docker-compose -f docker/docker-compose.yml build

docker-compose -f docker/docker-compose.yml up -d

docker-compose -f docker/docker-compose.yml down

```

## Url

```
localhost:80/get_info
localhost:80/process
localhost:80/write_info
localhost:80/sync_data
```