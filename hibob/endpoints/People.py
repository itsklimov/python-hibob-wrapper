#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint
from .Employment import Employment
from .Salaries import Salaries
from .Training import Training
from .VariablePayments import VariablePayments
from .Work import Work
from .Equities import Equities

class People(BaseEndpoint):

    @property
    def employment(self):
        return Employment(self.client)

    @property
    def work(self):
        return Work(self.client)

    @property
    def salaries(self):
        return Salaries(self.client)

    @property
    def variable_payments(self):
        return VariablePayments(self.client)

    @property
    def training(self):
        return Training(self.client)

    @property
    def equities(self):
        return Equities(self.client)

    def list(self, show_inactive=False):
        """
        Read company people

        List of all active people of the company,
        data is filtered based on the access level of the logged-in user.

        Only viewable categories are returned.

        Args:
            show_inactive (bool): should include inactive employees

        References:
            https://apidocs.hibob.com/reference#get_people
        """
        return self.client.get(
            "people",
            query={
                'showInactive': show_inactive
            }
        )

    def search_employee(self, identifier):
        """
        Read company people by id or email

        Returns the employee by the specified id or email.

        Args:
            identifier (str): employee id or email

        References:
            https://apidocs.hibob.com/reference#get_people-identifier
        """
        return self.client.get(
            "people/{identifier}".format(
                identifier=identifier
            )
        )

    def uninvite(self, employee_id):
        """
        Revoke access to bob for employee

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#post_employees-identifier-uninvite
        """
        return self.client.post(
            'employees/{employee_id}/uninvite'.format(
                employee_id=employee_id
            )
        )

    def invite(self, employee_id, wizard_id):
        """
        Invite an employee with a welcome wizard Id.

        Args:
            employee_id (str): employee id
            wizard_id (int):

        References:
            https://apidocs.hibob.com/reference#post_employees-employeeid-invitations
        """
        return self.client.post(
            'employees/{employee_id}/invitations'.format(
                employee_id=employee_id
            ),
            json_body={
                "welcomeWizardId": wizard_id
            }
        )

    def start_date(self, employee_id, start_date, reason=None):
        """
        Set or update employee's start-date.

        Args:
            employee_id (str): employee id
            start_date (date): the date this entry becomes effective
            reason (str): additional info for the start date update

        References:
            https://apidocs.hibob.com/reference#post_employees-employeeid-start-date
        """

        options = {
            'startDate': str(start_date)
        }
        if isinstance(reason, str):
            options['reason'] = reason

        return self.client.post(
            'employees/{employee_id}/start-date'.format(
                employee_id=employee_id
            ),
            json_body=options
        )

    def profiles(self, sort_by="firstName"):
        """
        Read public profile section of an employee
        Returns the public section of all the active employees of the logged-in user company

        Args:
            sort_by (str): optional field name to sort by, defaults to firstName

        References:
            https://apidocs.hibob.com/reference#get_profiles
        """
        return self.client.get(
            "profiles",
            query={
                'sortBy': sort_by
            }
        )

    def read_avatar(self, email):
        """
        Read avatar for an employee

        Args:
            email (str): employee email

        References:
            https://apidocs.hibob.com/reference#get_avatars
        """
        return self.client.get(
            'avatars',
            query={
                'email': email
            }
        )

    def read_avatar_by_id(self, employee_id):
        """
        Read avatar for an employee id

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_avatars-employeeid
        """
        return self.client.get(
            'avatars/{employee_id}'.format(
                employee_id=employee_id
            )
        )

    def upload_avatar_by_id(self, employee_id, url):
        """
        Upload employee's avatar by providing a URL to the image to upload.

        Args:
            employee_id (str): employee id
            url (str): the image to upload.

        References:
            https://apidocs.hibob.com/reference#put_avatars-employeeid
        """
        return self.client.put(
            'avatars/{employee_id}'.format(
                employee_id=employee_id
            ),
            json_body={
                'url': url
            }
        )

    def my_avatar(self):
        """
        Read logged-in user avatar

        References:
            https://apidocs.hibob.com/reference#get_my-avatar
        """
        return self.client.get('my/avatar')

    def update_email(self, employee_id, email):
        """
        Change an employee's email.
        Can't change self email, an invitation will be sent to the new address
        to verify the email if the employee is invited/active

        Args:
            employee_id (str): employee id
            email (str): new employee's email

        References:
            https://apidocs.hibob.com/reference#put_people-id-email
        """
        return self.client.put(
            'people/{employee_id}/email'.format(
                employee_id=employee_id
            ),
            json_body={
                'email': email
            }
        )

    def lifecycle(self, employee_id):
        """
        List employee's life-cycle status history
        Returns a list of life-cycle history entries for a given employee.

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_people-id-lifecycle
        """
        return self.client.get(
            'people/{employee_id}/lifecycle'.format(
                employee_id=employee_id
            )
        )
