## Cron Mon via Compose

This example shows how to setup and run Cron Mon via [Docker Compose](https://docs.docker.com/compose/).

## Quick start

The quickest way to get going with this example is to make use of the provided `Makefile` in this directory, which contains the following commands.

* `run`: Run Cron Mon, using a single tenant Keycloak realm.
* `run-single-tenant`: The same as `run` (`run` is an alias for this command).
* `run-user-tenant`: Run Cron Mon, using a user tenant Keycloak realm.
* `purge-volumes`: Remove the persisted data from the PostgreSQL database and Caddy server.

> [!TIP]
> For more information on _tenancy_ and _Keycloak realms_, see [the _Keycloak_ section in the main README](../../README.md/#keycloak)
