[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/joez/schulte-table)](https://hub.docker.com/r/joez/schulte-table/builds)

# About
schulte-table is a [Schulte Table] generator. It generates Schulte tables randomly as you required, and save them as a `.xlsx` file, so you can print it out for your children.

> A Schulte table is a grid with randomly distributed numbers or letters used for development of speed reading, peripheral vision, attention and visual perception.

# Quick start

Ensure you have [Docker][] installed, run the command:

    docker run --rm -v $(pwd):/work joez/schulte-table

You will find a file `schulte-table.xlsx` is generated, open it and print it out

# Usage

    usage: schulte-table.py [-h] [-v] [-r ROWS] [-c COLS] [-n NUMS]

    A Schulte Table generator

    optional arguments:
    -h, --help            show this help message and exit
    -v, --version         show program's version number and exit
    -r ROWS, --rows ROWS  table rows (default: 4)
    -c COLS, --cols COLS  table columns (default: 4)
    -n NUMS, --nums NUMS  number of tables (default: 5)

E.g. to generate 10 tables with size 6x6, run the following command

    docker run --rm -v $(pwd):/work joez/schulte-table -r 6 -c 6 -n 10
# Tips

The generated file will be owned by `root` user by default on Linux, to resolve this you can run the container as your current UID/GID with option `-u`, e.g.

    docker run --rm -v $(pwd):/work -u $(id -u):$(id -g) joez/schulte-table
# See also

* [Schulte Table]
* [Docker]
* [drafterleo/schulte]

[Schulte Table]: https://handwiki.org/wiki/Schulte_table
[Docker]: https://www.docker.com/
[drafterleo/schulte]: https://drafterleo.github.io/schulte/