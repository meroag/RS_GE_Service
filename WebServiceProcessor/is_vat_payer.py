import requests
import GlobalVariables

header = u"""Host: services.rs.ge\nContent-Type: text/xml; charset=utf-8\nContent-Length: length\nSOAPAction: "http://tempuri.org/is_vat_payer_tin'"""


def get(org_code):
    body = u"""<soap:Envelope xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema" xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/">
      <soap:Body>
        <is_vat_payer_tin xmlns="http://tempuri.org/">
          <su>{0}</su>
          <sp>{1}</sp>
          <tin>{2}</tin>
        </is_vat_payer_tin>
      </soap:Body>
    </soap:Envelope>""".format(GlobalVariables.su, GlobalVariables.sp, org_code)
    ans = requests.get(GlobalVariables.url, body)
    return ans
