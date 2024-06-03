#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Salaries(BaseEndpoint):

    def history(self, employee_id):
        """
        List employee's salary history
        Returns a list of salary history entries for a given employee.

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_people-id-salaries
        """
        return self.client.get(
            'people/{employee_id}/salaries'.format(
                employee_id=employee_id
            )
        )

    def create_entry(
            self,
            employee_id,
            reason,
            effective_date,
            base_value,
            base_currency,
            pay_period,
            pay_frequency
    ):
        """
        Creates a new salary entry for a given employee

        Args:
            employee_id (str): employee id
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            base_value (float):
            base_currency (str): 3 letter currency code
            pay_period (str): represents the period for this salary entry.
                One of: Annual, Hourly, Daily, Weekly, Monthly
            pay_frequency (str): represents the frequency the salary is paid.
                One of: Weekly, Monthly, Pro rata, Every two weeks, Twice a month, Four weekly

        References:
            https://apidocs.hibob.com/reference#post_people-id-salaries
        """
        return self.client.post(
            'people/{employee_id}/salaries'.format(
                employee_id=employee_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'base': {
                    'value': base_value,
                    'currency': base_currency
                },
                'payPeriod': pay_period,
                'payFrequency': pay_frequency
            }
        )

    def delete_entry(self, employee_id, entry_id):
        """
        Deletes a salary entry from the employees list

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to delete

        References:
            https://apidocs.hibob.com/reference#delete_people-id-salaries-entry-id
        """
        return self.client.delete(
            'people/{employee_id}/salaries/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            )
        )
