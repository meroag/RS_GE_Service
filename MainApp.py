from RevenueService import ServiceClient

if __name__ == "__main__":
    client = ServiceClient('POCKET:202311738',password='trd@1234')

    print(client.chek_service_user())



