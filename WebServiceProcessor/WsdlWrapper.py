import requests
import WebServiceProcessor.XMLProcessor as xmlProcessor

url = "http://services.rs.ge/WayBillService/WayBillService.asmx?WSDL"


class Wrapper:

    def __init__(self, method, data=None):
        self.data = data
        self.method = method
        action = "\"http://tempuri.org/" + method + "\""
        self.header = {
            "Content-Type": "text/xml; charset=utf-8",
            "SOAPAction": action
        }

    def create_response(self):
        print("Sending:\n\t\t" + self.method)
        print("Headers:\n\t\t" + str(self.header))
        body = ""
        for i in self.data:
            body += "<{0}>{1}</{0}> ".format(i, self.data[i])
        data = """<?xml version="1.0" encoding="utf-8"?> <soap:Envelope 
        xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" 
        xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/"> <soap:Body> <{0} xmlns="http://tempuri.org/"> {1} </{0}> </soap:Body> </soap:Envelope>""".format(self.method, body)
        print("Data:\n\t\t"+data)
        try:
            resp = requests.post(url, data=data, headers=self.header)
            if resp.ok:
                print("Response:\n\t\t".format(resp.content))
                return xmlProcessor.process(resp.content)
            else:
                print("Resonse Error :" + resp)
        except Exception as e:
            print(e)
