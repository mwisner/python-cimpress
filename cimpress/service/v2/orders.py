from ..base_service import BaseService


class Orders(BaseService):

    def submit(self, payload):
        """
        {
          "PartnerOrderId": "string",
          "CustomerId": "string",
          "Items": [
            {
              "Quantity": 0,
              "Sku": "string",
              "DocumentReferenceUrl": "string",
              "PartnerItemId": "string",
              "PartnerProductName": "string",
              "BusinessDays": 0
            }
          ],
          "DestinationAddress": {
            "FirstName": "string",
            "LastName": "string",
            "MiddleName": "string",
            "CompanyName": "string",
            "Phone": "string",
            "PhoneExtension": "string",
            "AddressLine1": "string",
            "AddressLine2": "string",
            "City": "string",
            "StateOrRegion": "string",
            "PostalCode": "string",
            "CountryCode": "string",
            "County": "string"
          },
          "DeliveryOptionId": "string",
          "BusinessDays": 0,
          "Metadata": "string",
          "ShippingLabelDetail": {
            "MerchantDisplayName": "string",
            "ReturnAddress": {
              "CompanyName": "string",
              "Email": "string",
              "Phone": "string"
            }
          }
        }

        :param payload:
        :return:
        """
        response = self.client.get("/v2/orders", payload)
        return response
