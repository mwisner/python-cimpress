from ..base_service import BaseService


class Products(BaseService):
    def list_products(self):

        response = self.client.get("/v1/partner/products", {})

        return response
