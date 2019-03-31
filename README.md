# ThreeFive challenger Python impllementation
[![CircleCI](https://circleci.com/gh/alvaropaco/py-three-five.svg?style=svg)](https://circleci.com/gh/alvaropaco/py-three-five)

This repository expose a simple ThreeFive challenger implementation using
a Docker image of Python 3.7 version.

### Proposal

Return a string repesentation when a numero is multiple from Three, Five or
Both. When a number, from a range between 1 and 100 was multiple of Three, the
code will display a string `Three`. When the number was multiple of five, the
program will display a string `Five`. And when the number was multiple of both,
three and five will display `ThreeFive` string. In the same way, the code will
display the current number when it wasn't a multiple of three or five.

### Usage

1. `docker compose -t threefive .`
2. `docker run threefive`

This steps will build and run the code tests with coverage report.