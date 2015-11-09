# De Exchange Broker

An automated exchange broker, which will create and fill guaranteed quotes for clients.

A quote consists of [De Exchange Node](https://bitbucket.org/deginner/de-exchange-node) orders which the client needs to approve. Once the client approves the orders, and [De Shared Wallet](https://bitbucket.org/deginner/de-shared-wallet) indicate the quote is funded, the broker will fill the orders, fulfilling its quoted obligation to the user.

For detailed documentation of the API, see the [swagger docs](http://deginner.github.io/deexbroker-ui/).

## Install

By default it's expected that [secp256k1](https://github.com/bitcoin/secp256k1) is available, so install it before proceeding; make sure to run `./configure --enable-module-recovery`. If you're using some other library that provides the functionality necessary for this, check the __Using a custom library__ section of the bitjws README.

##### Building secp256k1

In case you need to install the `secp256k1` C library, the following sequence of commands is recommended. If you already have `secp256k1`, make sure it was compiled from the expected git commit or it might fail to work due to API incompatibilities.

```
git clone git://github.com/bitcoin/secp256k1.git libsecp256k1
cd libsecp256k1
git checkout d7eb1ae96dfe9d497a26b3e7ff8b6f58e61e400a
./autogen.sh
./configure --enable-module-recovery
make
```

##### Install De Exchange Broker

De Exchange Broker is pretty easy to install after secp256k1. Just `make install`. This will automatically create a `~/.deapp/broker` directory for logs and temporary files, and run `python setup.py install`.

## Usage

Start the server in debugging mode.

`python deexbroker/server.py`

Start `supervisord` to manage the gunicorn process. This is suitable for a production environment.

`supervisord`

## Automated Swagger Updates

To update the swagger spec's paths, flask-swagger provides a generator. This can be run with `make swagger`, but it is worth looking at what is happening.

`flaskswagger deexbroker.server:app --template deexbroker/static/swagger.json --out-dir deexbroker/static/`

This crawls the app's routes looking for flask-swagger docstrings. If so, it updates the template and outputs it. In this case, the spec is being edited in place. The net result is that the spec's paths will be updated based on the latest docstrings in your app.

The definitions in this example were also automatically generated, those using [alchemyjsonschema](https://github.com/podhmo/alchemyjsonschema). It's command schema extractor was run on both [sqlalchemy-login-models](https://github.com/deginner/sqlalchemy-login-models) and the SQLAlchemy model(s) in this repo. For example (where $DE_APP_HOME is the root of this repo):

`alchemyjsonschema sqlalchemy_login_models.model -s --out-dir $DE_APP_HOME/deexbroker/static`


## Configuration

This app expects a Python configuration file, which can be specified using the DE_EX_BROKER_CONFIG_FILE environmental variable.

`export DE_EX_BROKER_CONFIG_FILE = /path/to/cfg.py`

The format of the config file is as shown in example_cfg.py. Be sure to change the keys before deploying in production!

