from ..base_service import BaseService
from cimpress.errors import CimpressError


class Documents(BaseService):

    def create(self, data, sku, scale, method):
        """
        :param payload:
        :return:
        """

        payload = {
            "Sku": sku,
            "ScaleType": scale
        }

        if method == "urls":
            payload['ImageUrls'] = data
            url = '/v2/documents/creators/url'
        elif method == "ids":
            payload['ImageIds'] = data
            url = '/v2/documents/creators/imageids'
        else:
            raise CimpressError("Method for documentation creation is not allowed")

        response = self.client.post(url, payload)

        return response

    def edit(self, payload):
        response = self.client.post('/v2/documents/edit', payload)
        return response

    def preview(self, sku, document, width):

        payload = {
            'sku': sku,
            'documentReferenceUrl': document,
            'width': width
        }

        response = self.client.get('/v2/documents/previews', payload)

        return response

    def scenes(self, document, width):

        payload = {
            'documentReferenceUrl': document,
            'width': width
        }

        response = self.client.get('/v2/documents/previews', payload)

        return response
