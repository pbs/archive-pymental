# Pymental  [![PyPI version](https://badge.fury.io/py/pumental.svg)](https://badge.fury.io/py/pymental)

Pymental is a python client used for interacting with AWS Elemental Conductor

## Installation

Install using pip:
```
pip install pymental
```


## Authentication
Authenticating in Elemental Conductor with the **pymental** library can be made:
- Explicitly:
```python
from pymental.client import Conductor
client = Conductor(
    user='elemental_user',
    key='elemental_key',
    server_url='https://fooserver.cloud.elementaltechnologies.com/'
)
```

- Implicitly by setting the following authentication details on the environment:
    - ELEMENTAL_USER
    - ELEMENTAL_KEY
    - ELEMENTAL_SERVER_URL
```python
from pymental.client import Conductor
# if the user, key and server_url params are not provided the credentials are 
# extracted from the environment variables
client = Conductor()
```

## Usage

Take a look at the examples [here](src/examples/)

The client uses certain endpoints like the **JobEndpoint** to interact with the Elemental API

For example:
```python
from pymental.client import Conductor

elemental_job_id = 125
client = Conductor()

job = client.jobs.get(elemental_job_id)  # .jobs is the JobEndpoint interface
```

Actions on endpoints like `client.jobs.get(1)` return a **Job** instance 

For more details about **endpoints** click: [here](docs/Endpoints.md)

For more information and usage examples click: [here](docs/Usage.md)

## Contribution
If you would like to contribute to this library feel free to make a pull request.
