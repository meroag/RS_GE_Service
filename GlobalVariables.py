import os

debug = True


class ServiceParameters():
    su = ""
    sp = ""

    def __init__(self):
        if not os.path.isfile("params.ini"):
            print("Please input user and pass:")
            self.su = str(input("SU:"))
            self.sp = str(input("SP:"))
        else:
            x = open("params.ini")
            self.su = str(x.readline().replace("\n", ""))
            self.sp = str(x.readline().replace("\n", ""))
            x.close()

        if debug:
            print("Parameters initialized")
            print("su: {0},sp: {1}".format(self.su, self.sp))
