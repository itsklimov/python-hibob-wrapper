#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .client import Client
from .endpoints import Documents
from .endpoints import Metadata
from .endpoints import Onboarding
from .endpoints import Payroll
from .endpoints import People
from .endpoints import Reports
from .endpoints import Tasks
from .endpoints import TimeOff


class Driver:

    def __init__(self, api_token):
        self.client = Client(api_token=api_token)

    @property
    def documents(self):
        """
        Api endpoint for documents

        Returns:
            Instance of :class:`~endpoints.Documents.Documents`
        """
        return Documents(self.client)

    @property
    def metadata(self):
        """
        Api endpoint for metadata

        Returns:
            Instance of :class:`~endpoints.Metadata.Metadata`
        """
        return Metadata(self.client)

    @property
    def onboarding(self):
        """
        Api endpoint for onboarding

        Returns:
             Instance of :class:`~endpoints.Onboarding.Onboarding`
        """
        return Onboarding(self.client)

    @property
    def payroll(self):
        """
        Api endpoint for payroll

        Returns:
            Instance of :class:`~endpoints.Payroll.Payroll`
        """
        return Payroll(self.client)

    @property
    def people(self):
        """
        Api endpoint for people

        Returns:
            Instance of :class:`~endpoints.People.People`
        """
        return People(self.client)

    @property
    def reports(self):
        """
        Api endpoint for reports

        Returns:
            Instance of :class:`~endpoints.Reports.Reports`
        """
        return Reports(self.client)

    @property
    def tasks(self):
        """
        Api endpoint for tasks

        Returns:
            Instance of :class:`~endpoints.Tasks.Tasks`
        """
        return Tasks(self.client)

    @property
    def time_off(self):
        """
        Api endpoint for time off

        Returns:
             Instance of :class:`~endpoints.TimeOff.TimeOff`
        """
        return TimeOff(self.client)
