#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Equities(BaseEndpoint):

    def list(self, employee_id):
        """
        Returns a list of equity grants for a given employee.

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_people-id-equities
        """
        return self.client.get(
            'people/{employee_id}/equities'.format(
                employee_id=employee_id
            )
        )

    def create_entry(
            self,
            employee_id,
            reason,
            effective_date,
            quantity,
            equity_type,
            vesting_commencement_date,
            consent_number,
            grant_date,
            exercise_price_value,
            exercise_price_currency,
            vesting_term,
            grant_type,
            option_expiration=None,
    ):
        """
        Creates a new equity grant for a given employee

        Args:
            employee_id (str): employee id
            reason (str): reason for this change
            effective_date (date): the date this entry becomes effective
            quantity (float): number of equities granted
            equity_type (str): The type of the grant
            vesting_commencement_date (date): Vesting commencement date
            consent_number (str): Consent number
            grant_date (date): Date the equity was granted
            exercise_price_value (float):
            exercise_price_currency (str): 3 letter currency code
            vesting_term (str): Terms for exercising this grant
            grant_type (str): Grant type.
                One of: Initial Grant, Merit Grant
            option_expiration (date): Date the options expire

        References:
            https://apidocs.hibob.com/reference#post_people-id-equities
        """
        payload = {
            'reason': reason,
            'effectiveDate': str(effective_date),
            'quantity': quantity,
            'equityType': equity_type,
            'vestingCommencementDate': str(vesting_commencement_date),
            'consentNumber': consent_number,
            'grantDate': str(grant_date),
            'exercisePrice': {
                'value': exercise_price_value,
                'currency': exercise_price_currency
            },
            'vestingTerm': vesting_term,
            'grantType': grant_type
        }

        if option_expiration:
            payload['optionExpiration'] = str(option_expiration)

        return self.client.post(
            'people/{employee_id}/equities'.format(
                employee_id=employee_id
            ),
            json_body=payload
        )

    def delete_entry(self, employee_id, entry_id):
        """
        Deletes an equity grant for an employee

        Args:
            employee_id (str): employee id
            entry_id (int): the entry id to delete

        References:
            https://apidocs.hibob.com/reference#delete_people-id-equities-entry-id
        """
        return self.client.delete(
            'people/{employee_id}/equities/{entry_id}'.format(
                employee_id=employee_id,
                entry_id=entry_id
            )
        )
