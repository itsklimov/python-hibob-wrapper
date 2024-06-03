#!/usr/bin/env python3
# -*- coding: utf8 -*-
import logging
import requests
from .exceptions import HibobException

log = logging.getLogger("hibiob.client")
log.setLevel(logging.INFO)


class Client:
    request_timeout = 30
    url = "https://api.hibob.com/v1/"

    def __init__(self, api_token):
        self.api_token = api_token

    @staticmethod
    def parse_response(response):
        content_type = response.headers.get("Content-Type", "")

        if content_type != "application/json":
            log.debug("Response is not application/json, returning raw response")
            return response

        try:
            return response.json()
        except ValueError:
            log.debug("Could not convert response to json, returning raw response")

        return response

    def make_request(
        self, method, endpoint, json_body=None, query=None, body=None, files=None
    ):

        methods = {
            "get": requests.get,
            "post": requests.post,
            "put": requests.put,
            "delete": requests.delete,
        }

        method = method.lower()
        request = methods.get(method, requests.get)

        request_params = {
            "headers": {"Accept": "application/json", "Authorization": self.api_token},
            "json": json_body,
            "params": query,
            "data": body,
            "files": files,
            "timeout": self.request_timeout,
        }

        response = request(self.url + endpoint, **request_params)
        parsed_response = self.parse_response(response)
        try:
            response.raise_for_status()
        except requests.HTTPError as error:
            log.exception(error)
            log.debug(response)
            if isinstance(parsed_response, dict):
                # response is json and was parsed to dict
                raise HibobException(parsed_response.get("error"))

            # fallback to requests exception
            raise error

        return parsed_response

    def get(self, endpoint, query=None):
        return self.make_request("get", endpoint, query=query)

    def post(self, endpoint, json_body=None, query=None, body=None, files=None):
        return self.make_request(
            "post", endpoint, json_body=json_body, query=query, body=body, files=files
        )

    def put(self, endpoint, json_body=None, query=None, body=None, files=None):
        return self.make_request(
            "post", endpoint, json_body=json_body, query=query, body=body, files=files
        )

    def delete(self, endpoint, json_body=None, query=None, body=None, files=None):
        return self.make_request(
            "post", endpoint, json_body=json_body, query=query, body=body, files=files
        )
