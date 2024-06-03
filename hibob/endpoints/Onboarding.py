#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Onboarding(BaseEndpoint):

    def wizards(self):
        """
        Get summary about all onboarding wizards.
        Wizard info includes Wizard Id, name and description.

        References:
            https://apidocs.hibob.com/reference#get_onboarding-wizards
        """
        return self.client.get('onboarding/wizards')

