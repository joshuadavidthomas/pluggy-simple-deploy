# django-simple-deploy w/ Plugins

**Proof of concept**

This is meant to a proof of concept for adding plugins to django-simple-deploy. It is not feature complete (it doesn't actually do anything except print to the console), but it is to show a potential way to add plugins to django-simple-deploy using [`pluggy`](https://pluggy.readthedocs.io/en/stable/).

Truthfully I wouldn't even say it's a good way of doing this, but just a quick way to show how it could be done and to get the conversation started.

## Setup

1. Create a virtual environment and activate it.

```bash
python -m venv venv
source venv/bin/activate
```

2. Change to the `simple_deploy` directory and install the package.

```bash
cd simple_deploy
pip install -e .
```

3. Change to the `example_project` directory and install the requirements.

```bash
cd ../example_project
pip install -r requirements.txt
```

## Usage (no plugins)

1. Within the `example_project` directory, run the `simple_deploy` command with any of the built-in platform plugins (Heroku, Fly.io, or Platform.sh).

```bash
python -m manage simple_deploy --platform {heroku,flyio,platformsh}
```

2. If you try to use a plugin that doesn't exist, you'll get an error.

## Usage (with AWS plugin)

1. Change to the `simple_deploy_aws` directory and install the package.

```bash
cd simple_deploy_aws
pip install -e .
```

2. Change back to the `example_project` directory and run the `simple_deploy` command with the AWS plugin.

```bash
cd ../example_project
python -m manage simple_deploy --platform aws
```
