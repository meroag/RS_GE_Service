# <?xml version="1.0" encoding="utf-8"?>
# <soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:xsd="http://www.w3.org/2001/XMLSchema">
#       <soap:Body>
#           <is_vat_payer_tinResponse xmlns="http://tempuri.org/">
#               <is_vat_payer_tinResult>true</is_vat_payer_tinResult>
#           </is_vat_payer_tinResponse>
#        </soap:Body>
# </soap:Envelope>'


def process(strin_xml):
    parts = str(strin_xml).split('<')

    startIndex = parts.index("soap:Body>")
    endIndex = parts.index("/soap:Body>")

    body = []
    for i in range(startIndex + 1, endIndex):
        body.append(parts[i])

    result = []

    for i in body:
        x = i.split('>')
        if len(x) < 2:
            continue
        if x[1] != "":
            result.append({str(x[0]): x[1]})

    return result
