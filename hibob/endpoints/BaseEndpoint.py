#!/usr/bin/env python3
# -*- coding: utf8 -*-


class BaseEndpoint:
    """
    Base class for all endpoints
    """

    def __init__(self, client):
        self.client = client
