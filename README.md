Forked from https://github.com/uvoteam/python-hibob

continuing support for hibob python wrapper

# python-hibob

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

python-hibob is an unofficial python3 driver for [HiBob](https://www.hibob.com/) [API](https://apidocs.hibob.com/)

## Installation

Clone this repo to use this package:

`git clone git@github.com:uvoteam/python-hibob.git hibob`

Install required packages:

`pip3 install -r hibob/requirements.txt`

## Usage

```python
from hibob import Driver

driver = Driver(
    api_token="YOUR_TOKEN_HERE"
)

# Read company people
people = driver.people.list()
```
For more detailed info check [wiki](https://github.com/uvoteam/python-hibob/wiki)

## Roadmap

* Installation from [PyPi](https://pypi.org/)
* Improved docstrings
* Unittests

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENCE.md)
