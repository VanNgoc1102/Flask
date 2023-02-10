## Run dockerfile: 
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


## Run docker

```
docker-compose -f docker/docker-compose.yml build

docker-compose -f docker/docker-compose.yml up -d
```