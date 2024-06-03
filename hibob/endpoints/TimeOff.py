#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint
import datetime


class TimeOff(BaseEndpoint):

    def submit_request(
            self,
            employee_id,
            policy_type,
            start_date,
            end_date,
            description='',
            start_date_portion='all_day',
            end_date_portion='all_day',
            skip_manager_approval=False,
    ):
        """
        Submits a new time off request.

        Args:
            employee_id (str): employee id
            policy_type (str): Request policy type, e.g. Holiday, Sick or any custom type defined
            start_date (date): Date of the first day of the time off
            end_date (date): Date of the last day of the time off
            description (str): request reason
            start_date_portion (str): Portion of the first day (all_day, morning, afternoon)
            end_date_portion (str): Portion of the last day (all_day, morning, afternoon)
            skip_manager_approval (bool): Admins only can skip the approval policy,
                setting this field to true will create an approved request

        References:
            https://apidocs.hibob.com/reference#post_timeoff-employees-id-requests
        """
        return self.client.post(
            'timeoff/employees/{employee_id}/requests'.format(
                employee_id=employee_id
            ),
            json_body={
                'policyType': policy_type,
                'startDate': str(start_date),
                'startDatePortion': start_date_portion,
                'endDate': str(end_date),
                'endDatePortion': end_date_portion,
                'skipManagerApproval': skip_manager_approval,
                'description': description
            }
        )

    def get_request_by_id(self, employee_id, request_id):
        """
        Supplies detailed info about an existing time off request.

        Args:
            employee_id (str): employee id
            request_id (str): request id


        References:
            https://apidocs.hibob.com/reference#get_timeoff-employees-id-requests-requestid
        """
        return self.client.get(
            'timeoff/employees/{employee_id}/requests/{request_id}'.format(
                employee_id=employee_id,
                request_id=request_id
            )
        )

    def cancel_request(self, employee_id, request_id):
        """
        Cancels an existing time off request.

        Args:
            employee_id (str): employee id
            request_id (str): request id

        References:
            https://apidocs.hibob.com/reference#delete_timeoff-employees-id-requests-requestid
        """
        return self.client.delete(
            'timeoff/employees/{employee_id}/requests/{request_id}'.format(
                employee_id=employee_id,
                request_id=request_id
            )
        )

    def get_requests_since_date(self, since):
        """
        Returns the list of time off requests approved or canceled since the specified date.

        Args:
            since (datetime.datetime): Timestamp starting from which to return the changes.
                Should be in ISO-8601 format, e.g. 2007-04-05T14:30:24.345Z or 2007-04-05T12:30-02:00

        References:
            https://apidocs.hibob.com/reference#get_timeoff-requests-changes
        """
        date_string = since.isoformat(timespec='milliseconds')

        if since.tzinfo is None or since.tzinfo.utcoffset(since) is None:
            # datetime is naive so fetching using utc tz
            date_string += 'Z'

        return self.client.get(
            'timeoff/requests/changes',
            query={
                'since': date_string
            }
        )

    def who_is_out(self, since, until):
        """
        Returns time off information for a given date range.

        Args:
            since (date): Start period date
            until (date): End period date

        References:
            https://apidocs.hibob.com/reference#get_timeoff-whosout
        """
        return self.client.get(
            'timeoff/whosout',
            query={
                'from': str(since),
                'to': str(until)
            }
        )

    def who_is_out_today(self, today=None):
        """
        Returns the list of people that have a time off request today or on the specified date.

        Args:
            today (date): Date to report out of the office.
                If not specified, the date at UTC at the time of the request is used

        References:
            https://apidocs.hibob.com/reference#get_timeoff-outtoday
        """
        if today is None:
            query = {}
        else:
            query = {
                'today': today
            }

        return self.client.get(
            'timeoff/outtoday',
            query=query
        )
