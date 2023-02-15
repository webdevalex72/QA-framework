## Configuration PyTest
---
For configuration pytest package we use **pytest.ini**.

Many pytest settings can be set in a configuration file,
which by convention resides in the root directory of your repository.

Here we registrate pytest.marks for our tests.


## Fixtures
---
Pytest fixtures provides in **conftest.py**.

::: conftest

## General configuration
---
In **cofig.yaml** file we define several settings:

- API URLs
- Database path
- UI driver path 

Then in config.py reads the config file & saves it to dictionary.
