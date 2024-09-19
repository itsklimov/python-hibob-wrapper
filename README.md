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

driver = Driver(service_id="YOUR_SERVICE_ID", api_token="YOUR_TOKEN")

# Read company people
people = driver.people.list()
```
For more detailed info check [wiki](https://github.com/uvoteam/python-hibob/wiki)

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENCE.md)

## Endpoints TODO Checklist
x = Done, transitioned to new service-id api

### Documents
- [ ] add_document
- [ ] delete_document
- [ ] list

### Metadata
- [ ] company_lists
- [ ] company_list_by_name
- [ ] add_item_to_list

### Onboarding
- [ ] wizards

### Payroll
- [ ] history

### People
- [x] list
- [ ] search_employee
- [ ] uninvite
- [ ] invite
- [ ] start_date
- [x] profiles
- [ ] read_avatar
- [ ] read_avatar_by_id
- [ ] upload_avatar_by_id
- [ ] my_avatar
- [ ] update_email
- [ ] lifecycle

### Reports
- [ ] list
- [ ] download_report

### Tasks
- [ ] list
- [ ] my_tasks

### TimeOff
- [ ] submit_request
- [ ] get_request_by_id
- [ ] cancel_request
- [ ] get_requests_since_date
- [x] who_is_out
- [x] who_is_out_today

### Work
- [ ] history
- [ ] create_entry
- [ ] delete_entry
- [ ] update_entry

### Employment
- [ ] history
- [ ] create_entry
- [ ] delete_entry
- [ ] update_entry

### Salaries
- [ ] history
- [ ] create_entry
- [ ] delete_entry

### Training
- [ ] list
- [ ] create_entry
- [ ] delete_entry

### VariablePayments
- [ ] list
- [ ] create_entry
- [ ] delete_entry

### Equities
- [ ] list
- [ ] create_entry
- [ ] delete_entry