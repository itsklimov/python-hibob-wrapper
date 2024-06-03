#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Reports(BaseEndpoint):

    def list(self):
        """
        Returns a list of all company defined reports,
        data is filtered based on the access level of the logged-in user.

        Only viewable categories are returned.

        References:
            https://apidocs.hibob.com/reference#get_company-reports
        """
        return self.client.get('company/reports')

    def download_report(self, report_id, formatting, include_info=False, locale=None):
        """
        Download the report by id

        Returns report data file of the specified format

        Args:
            report_id (float): Report id
            formatting (str): File format
            include_info (bool): Should include info
            locale (str):
                Requested language for the report columns in the format of locale (e.g. fr-FR),
                if not provided, the user preferences locale is used.

        References:
            https://apidocs.hibob.com/reference#get_company-reports-reportid-download
        """
        params = {
            'format': formatting,
            'includeInfo': include_info
        }

        if isinstance(locale, str):
            params['locale'] = locale

        return self.client.get(
            'company/reports/{report_id}/download'.format(
                report_id=report_id
            ),
            query=params
        )
