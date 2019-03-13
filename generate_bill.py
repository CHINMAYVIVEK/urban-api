import urllib.request, json, requests, base64
from urllib import request 
from urllib.request import urlopen

json_headers = base64.b64encode('PartnerID:AuthKey'.encode('utf-8'))
print(json_headers)
json_headers = json_headers.decode('utf-8')

values = """
    {
        "TemplateDetails": {
        "TemplateName": "DEFAULT_TEMPLATE"
    },
        "CustomerDetails": {
        "Name": "Customer Name",
        "Phone": "99XXXXXXXX",
        "CountryCode": 91,
        "Email": {
        "recepientEmail": "customer@email.com",
        "subject": "Welcome",
        "fromEmail": "receipts@oxebox.com",
        "fromName": "Billing System",
        "replyToEmail": "replyto@yourcompany.com"
        }
    },
        "PartnerDetails": {
        "PartnerID": "Your PartnerID",
        "AuthKey": "Your Account AuthKey"
        },
        "StoreDetails": {
        "StoreID": "Merchant StoreID"
        },
        "BillingDetails": {
        "BillReceiptID": "0001",
        "TransactionDate": "2019-03-13",
        "TransactionTime": "05:43:34",
        "AdditionalDetails": [
        {
            "Name": "Table No",
            "Value": "1234"
        },
        {
            "Name": "Order No",
            "Value": "06161"
        }
        ],
        "PaymentDetails": [
            {
                "Amount": 4000,
                "Type": "card",
                "Cashier": "John Rock"
            },
            {
                "Amount": 1646,
                "Type": "cash",
                "Cashier": "John Rock"
            }
            ],
            "ItemDetails": [
            {
                "ItemCode": "Pizza - 01",
                "ItemName": "Exotica Supreme Pizza",
                "ItemHeader": "12 medium, extra cheeze,olives",
                "ItemQty": 20,
                "ItemUnit": "pcs",
                "ItemPrice": 40,
                "ItemTotal": 800,
                "SubItems": [
            {
                "ItemName": "Extra cheese",
                "ItemQty": 1,
                "ItemUnit": "pcs",
                "ItemPrice": 29,
                "ItemTotal": 29
            },
            {
                "ItemName": "Extra Toppings",
                "ItemQty": 2,
                "ItemUnit": "pcs",
                "ItemPrice": 55,
                "ItemTotal": 110
            }
            ]
            },
            {
                "ItemCode": "Pizza-02",
                "ItemName": "Triple chicken feast pizza",
                "ItemHeader": "Crust: Pan, Medium, spicy",
                "ItemQty": 40,
                "ItemUnit": "pcs",
                "ItemPrice": 100,
                "ItemTotal": 4000,
                "Discounts": [
            {
                "Name": "Store Promo",
                "Total": 99,
                "Percent": 0
            },
            {
                "Name": "Additional discount",
                "Total": 18,
                "Percent": 9
            }
            ],
                "Taxes": [
            {
                "Name": "SGST 6",
                "Total": 240,
                "Percent": 6
            },
            {
                "Name": "SGST 9",
                "Total": 240,
                "Percent": 9
            }
            ]
            }
            ],
            "Discounts": [
            {
                "Name": "Store Promo",
                "Total": 99,
                "Percent": ""
            },
            {
                "Name": "Bulk discount",
                "Total": 400,
                "Percent": ""
            }
            ],
            "Taxes": [
            {
                "Name": "SGST",
                "Total": 222.86,
                "Percent": 6
            },
            {
                "Name": "CGST",
                "Total": 222.86,
                "Percent": 9
            }
            ],
                "SubTotal": 5600,
                "GrandTotal": 0,
                "RoundOff": 0.29,
                "TotalBillAmount": 5646,
                "AdditionalCharges": [
            {
                "Name": "Delivery Charges",
                "Amount": 4000,
                "Discounts": [
                    {
                        "Name": "Store Promo",
                        "Total": 99,
                        "Percent": ""
                    },
            {
                "Name": "Additional discount",
                "Total": 18,
                "Percent": 9
            }
            ],
            "Taxes": [
                {
                    "Name": "CGST 9",
                    "Total": 7.63,
                    "Percent": 9
                },
                {
                    "Name": "SGST 9",
                    "Total": 7.63,
                    "Percent": 9
                }
                ]
                }
                ],
                    "BillingAddress": {
                    "AddressLine1": "address line 1",
                    "AddressLine2": "address line 2",
                    "Area": "BTM",
                    "City": "Bengalaru",
                    "State": "Karnataka",
                    "Zip": 11111,
                    "Country": "India",
                    "Name": "Customer Name",
                    "Phone": "99XXXXXXXX"
                },
                    "ShippingAddress": {
                    "AddressLine1": "address line 1",
                    "AddressLine2": "address line 2",
                    "Area": "BTM",
                    "City": "Bengalaru",
                    "State": "Karnataka",
                    "Zip": 11111,
                    "Country": "India",
                    "Name": "Customer Name",
                    "Phone": "99XXXXXXXX"
                }
                }
                }
        """

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Basic '+json_headers,
  'Content-Length': 'Payload length'
}

html = values.encode("utf-8")
request = urllib.request.Request('https://www.oxebox.com/pbrapi/alpha/v1/index.php/PBR/generateBill', headers=headers)
response_body = urllib.request.urlopen(request, data=html).read()
print (response_body)
