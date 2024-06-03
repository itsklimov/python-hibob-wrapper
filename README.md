Forked from https://github.com/uvoteam/python-hibob

continuing support for hibob python wrapper

# python-hibob

[![Project Status: WIP – Initial development is in progress, but there has not yet been a stable, usable release suitable for the public.](https://www.repostatus.org/badges/latest/wip.svg)](https://www.repostatus.org/#wip)

python-hibob is an unofficial python3 driver for [HiBob](https://www.hibob.com/) [API](https://apidocs.hibob.com/)

## Installation

pip install git+https://github.com/itsklimov/python-hibob-wrapper.git

# requirements.txt
git+https://github.com/itsklimov/python-hibob-wrapper.git#egg=hibob


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

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENCE.md)
