from WebServiceProcessor import ServiceClient
import GlobalVariables

if __name__ == "__main__":
    GlobalVariables.debug = True
    #print("\nis_vat_payer_tin:{0}".format(ServiceClient.is_vat_payer_tin(org_code="202311738")))
    #print("\nchek_service_user:{0}".format(ServiceClient.chek_service_user()))
    #print("\nwhat_is_my_ip:{0}".format(ServiceClient.what_is_my_ip()))
    print("\nget_error_codes:{0}".format(ServiceClient.get_error_codes()))
    #print("\nget_car_numbers:{0}".format(ServiceClient.get_car_numbers()))
    #print("\nget_trans_types:{0}".format(ServiceClient.get_trans_types()))
    #print("\nget_server_time:{0}".format(ServiceClient.get_server_time()))





