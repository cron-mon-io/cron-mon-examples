# Cron Mon Examples

This repository contains examples for setting up Cron Mon in various ways.

## Required infrastructure

Cron Mon requires a PostgreSQL database and a running Keycloak server in order for it to function. All of these examples include this supporting infrastructure to give you an idea of how you might set this up yourself with the corresponding technology/ platform, but you are free to set this up however you so wish. So long as Cron Mon can access them, it does not matter where or how they are setup.

### Keycloak

This repository provides JSON files that can be used to import realms into Keycloak. Each realm demonstrates a different form of _tenancy_, namely *single-tenancy*, *multi-tenancy* and *'user-tenancy'*. Single and multi tenancy are likely tenant setups developers will have come across before. _User-tenancy_ is ultimately another form of multi-tenancy, only in this setup, every user has their own tenant, compared to the traditional multi-tenancy setup where a single tenant would serve a group of users.

> [!INFO]
> There currently isn't a multi-tenant realm, but this is on the TODO list.

## Compose

For an example of how Cron Mon can be set up using Compose, see [the `cron-mon/compose/` directory](cron-mon/compose/README.md).
