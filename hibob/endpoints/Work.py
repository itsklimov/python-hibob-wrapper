#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Work(BaseEndpoint):

    def history(self, employee_id):
        """
        List employee's work history.
        Returns a list of work history entries for a given employee

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_people-id-work
        """
        return self.client.get(
            'people/{employee_id}/work'.format(
                employee_id=employee_id
            )
        )

    def create_entry(
            self,
            employee_id,
            reason,
            effective_date,
            title,
            department,
            site,
            site_id,
            reports_to
    ):
        """
        Creates a new work entry for a given employee

        Args:
            employee_id (str): employee id
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            title (str): work title
            department (str): employee's department
            site (str): job location
            site_id (int): job location id
            reports_to (str): The manager's employee id

        References:
            https://apidocs.hibob.com/reference#post_people-id-work
        """
        return self.client.post(
            'people/{employee_id}/work'.format(
                employee_id=employee_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'title': title,
                'department': department,
                'site': site,
                'siteId': site_id,
                'reportsTo': reports_to
            }
        )

    def delete_entry(self, employee_id, entry_id):
        """
        Deletes a work entry from the employees list

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to delete

        References:
            https://apidocs.hibob.com/reference#delete_people-id-work-entry-id
        """
        return self.client.delete(
            'people/{employee_id}/work/{entry_id}'.format(
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
            title,
            department,
            site,
            site_id,
            reports_to
    ):
        """
        Updates a work entry from the employees list

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to update
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            title (str): work title
            department (str): employee's department
            site (str): job location
            site_id (int): job location id
            reports_to (str): The manager's employee id

        References:
            https://apidocs.hibob.com/reference#put_people-id-work-entry-id
        """
        return self.client.put(
            'people/{employee_id}/work/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'title': title,
                'department': department,
                'site': site,
                'siteId': site_id,
                'reportsTo': reports_to
            }
        )
