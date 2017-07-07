# Pymental Usage

## Creating elemental jobs

##### From an XML Profile

- Instantiate the pymental client/conductor

    ```python
    from pymental.client import Conductor
    client = Conductor()
    
    ```

- Create an Input instance
    
    Used for setting the job `source/input url` and other information like `authentication_details`
    
    ```python
    from pymental.models import Input, Location
    location = Location(uri='https://foo.bar/qux.mp4')
    job_input = Input(file_input=location)
    ```
    Input and all other pymental instances can be created also by parsing an XML like this `Input.parse(input_xml)`

- Create a JobProfile instance from the existing job profile XML
    ```python
    from pymental.models import JobProfile
    
    profile_xml = open('../src/examples/payloads/job_profile_example.xml', 'rb')
    job_profile = JobProfile.parse(profile_xml)
    ```

- Create the elemental job using the `.create_from_profile` helper
    ```python
    job = client.jobs.create_from_profile(input=job_input, profile=job_profile)
    ```

A full example can be found here: [from_profile.py](../src/examples/from_profile.py)

## Get existing job details

```python
from pymental.client import Conductor

elemental_job_id = 113
client = Conductor()
job_instance = client.jobs.get(elemental_job_id)
print(job_instance.input.file_input.uri)  # => 'https://foo.bar/qux.mp4'
print(job_instance.status)  # => 'complete'
print(job_instance.pct_complete)  # => '100'
```


## Get existing job status details

```python
from pymental.client import Conductor

elemental_job_id = 94
client = Conductor()
status_instance = client.jobs.status(elemental_job_id)
print(status_instance.status)  # => 'running'
print(status_instance.pct_complete)  # => '25'
```
