# Simple manage dataset geokoboard with python
this repo about simple way to manange dataset in geckoboard with python include
- test connection & auth
- create dataset
- add new data
- update data
- delete data

## install required
requests package for use request to http server
```
sudo pip install requests
```

python-dotenv package for get configuration data from  `.env` file
```
sudo pip install python-dotenv
```

## API Key in geockboard
Geckoboard need authorize by API key. you can find api key in menu account in top right corner.

## Setup configuration file
copy .env.example file and rename it to .env file 
```
cp .env.example > .env
```
Then replace your api key
```
apikey=<you-api-key->
```
## Documentation
for more information. you can have a look.
- [Manage Geckoboard Dataset with python](https://www.linkedin.com/pulse/manage-geckoboard-dataset-python-narongsak-keawmanee)
- [Geokoboard API reference](https://developer.geckoboard.com/api-reference/)

