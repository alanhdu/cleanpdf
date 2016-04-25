#!/usr/bin/env python3
import subprocess
import os

import click

@click.command()
@click.argument("src", type=click.Path(exists=True, dir_okay=False))
@click.argument("dest",
                type=click.Path(exists=True, file_okay=False, writable=True))
@click.option("--memory", "-m", type=click.FLOAT, default=4.0,
              help="The maximum RAM to use in GB (default=4.0 GiB)")
@click.option("--quiet", "-q", is_flag=True, help="suppress output")
def convert(src, dest, memory, quiet):
    """Converts SRC (a pdf file) into a series of .jpg images in the DEST
    directory.
    """
    args = [
        "convert",
        "-density", "600",
        "-limit", "memory", "{0}GiB".format(memory),
        "-trim",
        src,
        "-quality", "100",
        "-sharpen", "0x1.0",
        os.path.join(dest, "%d.jpg")
    ]

    if not quiet:
        args.insert(1, "-verbose")

    subprocess.call(args)


if __name__ == "__main__":
    convert()
