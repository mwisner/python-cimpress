from ..base_service import BaseService

class BulkOrderLookup(BaseService):

    def bulk_order_lookup(self, data):
        response = self.client.get("v1/bulk-order-lookup", data)
        return response
