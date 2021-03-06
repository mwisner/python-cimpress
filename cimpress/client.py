import requests
from .errors import CimpressError


class Client(object):

    def __init__(self, token, environment="sandbox"):

        if environment == "sandbox":
            self.base_url = "https://api.cimpress.io/sandbox/vcs/printapi"
        elif environment == "production":
            self.base_url = "https://api.cimpress.io/sandbox/vcs/printapi"
        else:
            raise CimpressError("Invalid environment selected")

        self.token = token

        self.rate_limit_details = {}
        self.http_session = requests.Session()

    @property
    def _auth(self):
        return self.token

    @property
    def v1_products(self):
        from .service.v1 import products
        return products.Products(self)

    @property
    def v2_documents(self):
        from .service.v2 import documents
        return documents.Documents(self)

    @property
    def v2_orders(self):
        from .service.v2 import orders
        return orders.Orders(self)

    def _execute_request(self, request, params):
        result = request.execute(self.base_url, self._auth, params)

        return result

    def get(self, path, params):
        from . import request
        req = request.Request('GET', path, self.http_session)
        return self._execute_request(req, params)

    def post(self, path, params):
        from . import request
        req = request.Request('POST', path, self.http_session)

        return self._execute_request(req, params)

    def put(self, path, params):
        from . import request
        req = request.Request('PUT', path, self.http_session)
        return self._execute_request(req, params)

    def delete(self, path, params):
        from . import request
        req = request.Request('DELETE', path, self.http_session)
        return self._execute_request(req, params)
