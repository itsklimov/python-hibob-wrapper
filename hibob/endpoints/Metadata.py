#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Metadata(BaseEndpoint):

    def company_lists(self):
        """
        Get all company lists

        References:
            https://apidocs.hibob.com/reference#get_company-named-lists
        """
        return self.client.get('company/named-lists')

    def company_list_by_name(self, list_name):
        """
        Get a specific company list by name

        Args:
            list_name (str): internal name of the list

        References:
            https://apidocs.hibob.com/reference#get_company-named-lists-listname
        """
        return self.client.get(
            'company/named-lists/{list_name}'.format(
                list_name=list_name
            )
        )

    def add_item_to_list(self, list_name, name):
        """
        Add a new item to an existing list

        Args:
            list_name (str): internal name of the list
            name (str): Name of the item

        References:
            https://apidocs.hibob.com/reference#post_company-named-lists-listname
        """
        return self.client.post(
            'company/named-lists/{list_name}'.format(
                list_name=list_name
            ),
            json_body={
                'name': name
            }
        )
