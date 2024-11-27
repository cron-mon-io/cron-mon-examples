## Sample cron job

This serves as a sample cron job, that's being monitored by CronMon.

> [!NOTE]
> You will need an installation of Python 3.x on your system in order to run this.

### Getting set up

To get setup you first need to have Cron Mon running. The `cron-mon/` directory in this repository features several examples of how you might set Cron Mon up - you can use any one of these with this sample cron job.
Once you have Cron Mon up and running, you'll then need to setup a _Monitor_ and an API Key within the application.

From here, you can prepare the sample cron job with just a few commands. Note you'll need the address that you have the Cron Mon API running at, the ID of your _Monitor_, and your API key:

> [!TIP]
> Take a look at [the `Makefile` section](#makefile) for full information on the arguments to supply to `setup-env`.

```
make install
make setup-env server-url="http://<your-cron-mon-address>" api-key="<your-api-key>" monitor-id="<your-monitor-id>"
```

### Usage

The following is the typical way this sample cron job might be driven:

**Run the cron job for 10 seconds**

```
make run duration=10
```

**Run the cron job for 5 seconds and then error**

```
make run duration=5 error='Uh oh, something went wrong'
```

### \`Makefile\`

As with the rest of this repository, a `Makefile` is provided to make this as quick and easy as possible.

* `install`: Setup a virtual Python environment and install the necessary packages.
* `setup-env`: Create a `.env` file, which is required in order for the cron job to run.
  Arguments:
    * `server-url`: The URL that the Cron Mon API is running at
    * `api-key`: An API key to allow the cron job to be monitored. Note you will need to create an API key via the Cron Mon application for this.
    * `monitor-id`: The ID of the monitor being used to monitor our cron job. You can get this from the Cron Mon application.
* `run`: Run the cron job:
  Arguments:
    * `duration`: The time, in seconds, for the cron job to be running.
    * `error`(optional): If provided the cron job will raise an `Exception`, using this value as the error message.
* `remove-venv`: Delete the virtual python environment.
