#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Training(BaseEndpoint):

    def list(self, employee_id):
        """
        List employee's training records

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_people-id-training
        """
        return self.client.get(
            'people/{employee_id}/training'.format(
                employee_id=employee_id
            )
        )

    def create_entry(
            self,
            employee_id,
            reason,
            effective_date,
            name,
            description,
            cost_value,
            cost_currency,
            status,
            frequency,
            start_date,
            end_date,
            document_id
    ):
        """
        Creates a new training records for a given employee

        Args:
            employee_id (str): employee id
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            name (str): Name of the training entry. The name must be of an item in the training list field
            description (str): Further description about the training entry
            cost_value (float):
            cost_currency (str): 3 letter currency code
            status (str): Status of the training entry
            frequency (str): Frequency of the training entry. The name must be of an item in the frequency list field
            start_date (date): the date this entry becomes effective
            end_date (date): date of training completion
            document_id (float): Document id of the document attached to this training entry

        References:
            https://apidocs.hibob.com/reference#post_people-id-training
        """
        return self.client.post(
            'people/{employee_id}/training'.format(
                employee_id=employee_id
            ),
            json_body={
                'reason': reason,
                'effectiveDate': str(effective_date),
                'name': name,
                'description': description,
                'cost': {
                    'value': cost_value,
                    'currency': cost_currency
                },
                'status': status,
                'frequency': frequency,
                'startDate': start_date,
                'endDate': end_date,
                'documentId': document_id
            }
        )

    def delete_entry(self, employee_id, entry_id):
        """
        Deletes a training record for an employee

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to delete

        References:
            https://apidocs.hibob.com/reference#delete_people-id-training-entry-id
        """
        return self.client.delete(
            'people/{employee_id}/training/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            )
        )
