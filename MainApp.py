from WebServiceProcessor import ServiceClient

if __name__ == "__main__":
    isPayer = ServiceClient.is_vat_payer_tin(org_code="202311738")
    print(isPayer)
