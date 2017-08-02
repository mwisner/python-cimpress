from ..base_service import BaseService


class Products(BaseService):

    def list_all(self):
        response = self.client.get("/v1/partner/products", {})
        return response

    def list_all_prices(self):
        response = self.client.get("/v1/partner/product-prices", {})
        return response

    def get_product(self, sku):
        response = self.client.get("/v1/products/%s" % sku, {})
        return response

    def get_product_surfaces(self, sku):
        response = self.client.get("/v1/products/%s/surfaces" % sku, {})
        return response
