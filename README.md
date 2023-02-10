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
```
## Url

```
localhost:5000/get_info
localhost:5000/process
localhost:5000/write_info
localhost:5000/sync_data

```