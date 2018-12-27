class ServiceParameters():
    su = ""
    sp = ""

    def __init__(self):
        x = open("params.ini")
        self.su = str(x.readline().replace("\n",""))
        self.sp = str(x.readline().replace("\n",""))
        x.close()
        print("Parameters initialized")
        print("su: {0},sp: {1}".format(self.su,self.sp))

