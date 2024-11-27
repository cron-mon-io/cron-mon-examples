import os
import time

import click
from cron_mon import monitor


@click.command()
@click.argument("duration", type=int)
@click.option("--error", default=None, type=str)
def main(duration: int, error: str | None) -> None:

    @monitor(os.environ["MONITOR_ID"])
    def cron_job() -> str:
        """A simple cron job that sleeps and returns a message."""
        print(f"Sleeping for {duration} seconds...")
        time.sleep(duration)

        if error:
            raise Exception(error)
        
        return "Finished cron-job."

    cron_job()

if __name__ == "__main__":
    main()

