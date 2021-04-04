[![Docker Cloud Build Status](https://img.shields.io/docker/cloud/build/joez/ptk)](https://hub.docker.com/r/joez/schulte-table/builds)

# About
schulte-table is a [Schulte Table] generator. It generates Schulte tables randomly as you required, and save them as a `.xlsx` file, so you can print it out for your children.

> A Schulte table is a grid with randomly distributed numbers or letters used for development of speed reading, peripheral vision, attention and visual perception.

# Quick start

Ensure you have [Docker][] installed, run the command:

    docker run --rm -v $(pwd):/work joez/schulte-table

You will find a file `schulte-table.xlsx` is generated, open it and print it out
# See also

* [Schulte Table]
* [Docker]
* [drafterleo/schulte]

[Schulte Table]: https://handwiki.org/wiki/Schulte_table
[Docker]: https://www.docker.com/
[drafterleo/schulte]: https://drafterleo.github.io/schulte/