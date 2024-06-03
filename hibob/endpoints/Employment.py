#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Employment(BaseEndpoint):

    def history(self, employee_id):
        """
        List employee's employment history

        Returns a list of employment history entries for a given employee.

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_people-id-employment
        """
        return self.client.get(
            'people/{employee_id}/employment'.format(
                employee_id=employee_id
            )
        )

    def create_entry(
            self,
            employee_id,
            reason,
            effective_date,
            contract,
            entry_type,
            salary_pay_type,
    ):
        """
        Creates a new employment entry for a given employee

        Args:
            employee_id (str): employee id
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            contract (str):
            entry_type (str):
            salary_pay_type (str):

        References:
            https://apidocs.hibob.com/reference#post_people-id-employment
        """
        return self.client.post(
            'people/{employee_id}/employment'.format(
               employee_id=employee_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'contract': contract,
                'type': entry_type,
                'salaryPayType': salary_pay_type
            }
        )

    def delete_entry(self, employee_id, entry_id):
        """
        Deletes a employment entry from the employees list

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to delete

        References:
            https://apidocs.hibob.com/reference#delete_people-id-employment-entry-id
        """
        return self.client.delete(
            'people/{employee_id}/employment/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            )
        )

    def update_entry(
            self,
            employee_id,
            entry_id,
            reason,
            effective_date,
            contract,
            entry_type,
            salary_pay_type,
    ):
        """
        Updates a employment entry from the employees list

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to update
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            contract (str):
            entry_type (str):
            salary_pay_type (str):

        References:
            https://apidocs.hibob.com/reference#put_people-id-employment-entry-id
        """
        return self.client.put(
            'people/{employee_id}/employment/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'contract': contract,
                'type': entry_type,
                'salaryPayType': salary_pay_type
            }
        )
