Devops Friendly App
===

A complimentary code example for the talk: Building Devops Friendly Apps in Python.

2. Dependencies
---

* Dependencies should be declared explicity in the code.
* Versions should be explicity stated.
* Dependency installation should be isolated per
  application.

To install virtualenv and quickly setup one.

```sh
$ sudo pip virtulenv             # Installs virtualenv
$ virtualenv --distribute myenv  # Creates an environment called 'env'
$ source ./myenv/bin/activate    # Activates the environment called 'env'
(env) $ pip freeze               # Show return no dependencies
```
https://virtualenv.pypa.io/en/latest/

See `src/requirements.txt` for this application's dependencies.

Now that we have virtualenv ready and a codebase with a declared set of
dependencies, we can install the dependencies now.

```sh
(env) $ pip install -r src/requirements.txt  # Installs our dependencies
(env) $ pip freeze  # Let's check.
Flask==0.10.1
itsdangerous==0.24
...
```
