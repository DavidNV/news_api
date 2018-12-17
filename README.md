# News API

This project will consume the [newapi](https://newsapi.org/) and will save locally the last one hundred(100) news in JSON format.

## Getting Started

Please wait for the docker image to be constructed

### Prerequisites

In order to run this project you'll need:

```
Docker version 18.06
```
```
docker-compose version 1.21.2
```
```
A valid *newsapi* API Key
```

### Installing

Once you have Docker and Compose use *sudo docker-compose build --build-arg inbound_api_key=[YOUR_API_KEY]*

```
If you made a mistake by using another docker command before, just use *source clean_environment.sh*
For now, please use this command as well if you add more dependencies to the requirements file.
```
```
For launching a bash container use: *sudo docker-compose run web bash*
For launching the server: *sudo docker-compose up*
```
```
If you want to populate the database with the last 100 new please *sudo docker-compose run web python3.7 seeds.py*
```


## Built With

* [NewsAPI](https://newsapi.org/) - The provider
* [Django](https://www.djangoproject.com/) - Framework
* [Python](https://www.python.org/) - Programming Language


## Authors

* **David Niño Valderrama** - *Initial work* - [DavidNV](https://github.com/DavidNV)

## License

TBD

## Acknowledgments

* To challange myself.
