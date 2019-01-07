from RevenueService import ServiceClient


def show(value,name: str):
    print(name + "\n{0}".format(value))


if __name__ == "__main__":
    #user = input("Service User:")
    #pasword = input("Service Password")
    user = 'POCKET:202311738'
    password = 'trd@1234'
    client = ServiceClient(str(user), password=password)

    x = client.get_server_time()
