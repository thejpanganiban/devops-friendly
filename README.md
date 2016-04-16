Devops Friendly App
===

A complimentary code example for the talk: Building Devops Friendly Apps in Python.

Goal
---

Reduce friction between the development team and the other technical operations
teams such as the system administrators and the tecnical support engineers.

Dependencies
---

See `src/requirements.txt` for this application's dependencies.

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

Read more about [Virtualenv](https://virtualenv.pypa.io/en/latest/)


Now that we have virtualenv ready and a codebase with a declared set of
dependencies, we can install the dependencies now.

```sh
(env) $ pip install -r src/requirements.txt  # Installs our dependencies
(env) $ pip freeze  # Let's check.
Flask==0.10.1
itsdangerous==0.24
...
```

Config
---

See `src/config.py` for this application's configurations.

* Don't use static files to declare configs (eg. config.yml, production.yml)
* The configuration should be picked-up from the system environment (`os.environ['CONFIG']`)
* You can declare your configs in a single module that picks-up from the system
  environment.

So normally, we run the application by

```sh
(env) $ python server.py
```

To override the configuration defaults:

```sh
# We're not pointed to a different database.
(env) $ DATABASE_URL=mysql://username:password@anotherdbhost:1234/x python server.py
# And another instance pointed to another one.
(env) $ DATABASE_URL=mysql://username:password@anotherdbhost:1234/x2 python server.py
```

*Why named-environments are an anti-pattern*

henever we need a new configuration (eg. app to point to a different db),
we'd need to declare a new config file (ie. different-db.yml) when we can
explicitly declare this in the command (ie. CONFIG=VALUE python script.py)

Port Binding
---

See `src/run.sh`. This is how we run the application.

* Run applications with a declared port (eg. http://localhost:5000)
* No distinction between local and third-party services.
* Avoid the use of unix sockets (Dependency injection is ugly).

In the example `src/run.sh`, we can see that we're running gunicorn on the
environment-set `HOST` and `PORT`.

Logging
---

See `src/logconfig.py` on how it was configured and `src/server.py` on how
it was used.

* Stream to stdout.
* Allow sysad to manage the logs from stdout (eg. script.py > logfile.log,
  docker logs mycontainer, etc).
* Having different ways to manage logs (to syslog, to file, log rotation, etc)
  makes it painful for sysads to manage logs.
* Don't use print!
* Use the appropriate logging levels (INFO, DEBUG, etc)

Python has a great documentation on how to use and configure the logging system.
Read more about [Python Logging](https://docs.python.org/2/library/logging.html).

Although they are a bunch of other ways to setup logging, we'll be using the
most basic method in our example (logging.basicConfig).

This is one of the areas where convention shines over configuration.
