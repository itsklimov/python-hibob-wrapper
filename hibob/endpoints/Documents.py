#!/usr/bin/env python3
# -*- coding: utf8 -*-
from .BaseEndpoint import BaseEndpoint


class Documents(BaseEndpoint):

    def add_document(self, employee_id, doc_name, doc_url, tags=None, shared=True):
        """
        Add a document to an employee to the shared or confidential folder

        Args:
            employee_id (str): employee id
            doc_name (str): document name
            doc_url (str): URL of the document to upload
            tags (List[str]): document's tags
            shared (bool): whether document should be uploaded to shared folder or confidential

        References:
            https://apidocs.hibob.com/reference#post_docs-people-id-shared
            https://apidocs.hibob.com/reference#post_docs-people-id-confidential
        """
        tags = tags or []
        return self.client.post(
            "docs/people/{employee_id}/{folder}".format(
                employee_id=employee_id,
                folder='shared' if shared else 'confidential'
            ),
            json_body={
                'documentName': doc_name,
                'documentUrl': doc_url,
                'tags': tags
            }
        )

    def delete_document(self, employee_id, doc_id, shared=True):
        """
        Delete specific document from employee's shared or confidential folder

        Args:
            employee_id (str): employee id
            doc_id (str): document id
            shared (bool): whether document should be deleted from shared folder or confidential

        References:
            https://apidocs.hibob.com/reference#delete_docs-people-id-shared-docid
            https://apidocs.hibob.com/reference#delete_docs-people-id-confidential-docid
        """
        return self.client.delete(
            "docs/people/{employee_id}/{folder}/{doc_id}".format(
                employee_id=employee_id,
                folder='shared' if shared else 'confidential',
                doc_id=doc_id
            )
        )

    def list(self, employee_id):
        """
        Download employee's documents
        Returns list of documents and download links.

        Args:
            employee_id (str): employee id

        References:
            https://apidocs.hibob.com/reference#get_docs-people-id
        """
        return self.client.get(
            'docs/people/{employee_id}'.format(
                employee_id=employee_id
            )
        )
