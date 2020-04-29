# Flask Rest API

## Dependencies

- [Python 3.8](https://www.python.org/downloads/) 
- [pip](https://pip.pypa.io/en/stable/installing/)
- [Flask](https://flask.palletsprojects.com/en/1.1.x/installation/#install-flask)


## Getting Started

Clone the project

```bash
$ git clone https://github.com/balalistens/flask-rest-api.git <my-project-name>
$ cd <my-project-name>
```

Install dependencies

```bash
$ cp .env.example .env                  # Copy env file 
$ pip install -r requirements.txt       # Install the pip dependencies
```

Run the server

```bash
$ python src/app.py                  # Run the python server
```

## API Routes
```bash
# env variables APPLICATION_HOST & APPLICATION_PORT determine the base url
/v1/api/posts
/v1/api/comments
```

## Application Structure

MVC is the design pattern followed. But due to the lack of DB Models in this repo, it currently has only [Flask Blueprints](https://flask.palletsprojects.com/en/1.1.x/blueprints/)

```
src                    # Application source code
- resources            # Controller / Logic for HTTP verbs of the routes
- routes               # Routes definitions linked to the associated resources (Blueprints)
- util                 # Helper functions
- config.py            # Project configuration
- app.py               # App/Server configuration
.env                   # Environment variables
```