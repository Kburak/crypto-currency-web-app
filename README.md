
# crypto-currency-web-app

  A simple web app with Django to be able to check current news and prices for Crypto market. It uses the CryptoCompare.com's API.

  To get your own API Key, simply go into the website and create one. You can paste api_key variable which you can see an area 'Your API Key'.

## Install guide

##### Clone the repo

```bash
$ git clone https://github.com/Kburak/crypto-currency-web-app.git
$ cd crypto-currency-web-app
```

##### Create the virtualenv and activate it
```bash
$ python3 -m venv venv
$ . venv/bin/activate
```

##### Or on Windows cmd::
```bash
    $ py -3 -m venv venv
    $ venv\Scripts\activate.bat
```

##### Install dependencies
```bash
$ pip install -r requirements.txt
```

##### Run the app
```bash
$ python manage.py runserver
```
