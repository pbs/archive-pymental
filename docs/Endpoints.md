# Pymental Endpoints

Interacting with Elemental API is done through interfaced **Endpoints**

Base Endpoints:
- JobEndpoint
- JobProfileEndpoint

Endpoints are defined here: [endpoints.py](../src/pymental/endpoints.py)

All the endpoints are mapped on the client at initialization and they are accessible on the client instance.
```python
from pymental.client import Conductor

client = Conductor()

elemental_job_id = 12
job = client.jobs.get(elemental_job_id)  # returns a Job instance

elemental_job_profile_id = 43
job_profile = client.profiles.get(elemental_job_profile_id)  # returns a JobProfile instance

```

Pymental models like **Job**, **JobProfile** and many more are defined [here](../src/pymental/models/)
