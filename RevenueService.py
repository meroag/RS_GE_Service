from suds.client import Client

url = "http://services.rs.ge/WayBillService/WayBillService.asmx?WSDL"


class ServiceClient:
    mainUser = ""
    mainPass = ""

    def __init__(self, user: str, password: str):
        self.client = Client(url)
        self.user = user
        self.password = password

    def chek_service_user(self):
        return self.client.service.chek_service_user(self.user, self.password)

    def close_waybill(self, idWayBill: int):
        return self.client.service.close_waybill(self.user, self.password, idWayBill)

    def close_waybill_transporter(self, waybill_id: int, reception_info: str, receiver_info: str, delivery_date):
        return self.client.service.close_waybill_transporter(self.user, self.password, waybill_id, reception_info,
                                                             receiver_info, delivery_date)

    def close_waybill_vd(self,delivery_date,waybill_id:int):
        return self.client.close_waybill_vd(self.user, self.password,delivery_date,waybill_id)

    def confirm_waybill(self,waybill_id:int):
        return self.client.confirm_waybill(self.user, self.password,waybill_id)

    def create_service_user(self,name:str,su:str,sp:str):
        ip = self.what_is_my_ip()
        return self.client.create_service_user(self.mainUser, self.mainPass,ip,name,su,sp)

    def del_waybill(self,waybill_id:int):
        return self.client.del_waybill(self.user, self.password,waybill_id)

    def delete_bar_code(self,bar_code:str):
        return self.client.delete_bar_code(self.user, self.password,bar_code)

    def delete_car_numbers(self,car_number:str):
        return self.client.delete_car_numbers(self.user, self.password,car_number)

    def delete_waybill_tamplate(self,id:int):
        return self.client.delete_waybill_tamplate(self.user, self.password,id)

    def get_adjusted_waybill(self,id:int):
        return self.client.get_adjusted_waybill(self.user, self.password,id)

    def get_adjusted_waybills(self,waybill_id:int):
        return self.client.get_adjusted_waybills(self.user, self.password,waybill_id)

    def get_akciz_codes(self,s_text:str = ""):
        return self.client.get_akciz_codes(self.user, self.password,s_text)

    def get_bar_codes(self,bar_code:str):
        return self.client.get_bar_codes(self.user, self.password,bar_code)

    def get_buyer_waybilll_goods_list(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = ""):
        return self.client.get_buyer_waybilll_goods_list(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment)

    def get_buyer_waybills(self):
        return self.client.get_buyer_waybills(self.user, self.password)

    def get_buyer_waybills_ex(self):
        return self.client.get_buyer_waybills_ex(self.user, self.password)

    def get_c_waybill(self):
        return self.client.get_c_waybill(self.user, self.password)

    def get_car_numbers(self):
        return self.client.get_car_numbers(self.user, self.password)

    def get_error_codes(self):
        return self.client.get_error_codes(self.user, self.password)

    def get_name_from_tin(self):
        return self.client.get_name_from_tin(self.user, self.password)

    def get_payer_type_from_un_id(self):
        return self.client.get_payer_type_from_un_id(self.user, self.password)

    def get_print_pdf(self):
        return self.client.get_print_pdf(self.user, self.password)

    def get_server_time(self):
        return self.client.get_server_time(self.user, self.password)

    def get_service_users(self):
        return self.client.get_service_users(self.user, self.password)

    def get_tin_from_un_id(self):
        return self.client.get_tin_from_un_id(self.user, self.password)

    def get_transporter_waybills(self):
        return self.client.get_transporter_waybills(self.user, self.password)

    def get_trans_types(self):
        return self.client.get_trans_types(self.user, self.password)

    def get_waybill(self):
        return self.client.get_waybill(self.user, self.password)

    def get_waybill_by_number(self):
        return self.client.get_waybill_by_number(self.user, self.password)

    def get_waybill_goods_list(self):
        return self.client.get_waybill_goods_list(self.user, self.password)

    def get_waybill_tamplate(self):
        return self.client.get_waybill_tamplate(self.user, self.password)

    def get_waybill_tamplates(self):
        return self.client.get_waybill_tamplates(self.user, self.password)

    def get_waybill_types(self):
        return self.client.get_waybill_types(self.user, self.password)

    def get_waybill_units(self):
        return self.client.get_waybill_units(self.user, self.password)

    def get_waybills(self):
        return self.client.get_waybills(self.user, self.password)

    def get_waybills_ex(self):
        return self.client.get_waybills_ex(self.user, self.password)

    def get_wood_types(self):
        return self.client.get_wood_types(self.user, self.password)

    def is_vat_payer(self):
        return self.client.is_vat_payer(self.user, self.password)

    def is_vat_payer_tin(self):
        return self.client.is_vat_payer_tin(self.user, self.password)

    def ref_waybill(self):
        return self.client.ref_waybill(self.user, self.password)

    def ref_waybill_vd(self):
        return self.client.ref_waybill_vd(self.user, self.password)

    def reject_waybill(self):
        return self.client.reject_waybill(self.user, self.password)

    def save_bar_code(self):
        return self.client.save_bar_code(self.user, self.password)

    def save_car_numbers(self):
        return self.client.save_car_numbers(self.user, self.password)

    def save_invoice(self):
        return self.client.save_invoice(self.user, self.password)

    def save_waybill(self):
        return self.client.save_waybill(self.user, self.password)

    def save_waybill_tamplate(self):
        return self.client.save_waybill_tamplate(self.user, self.password)

    def save_waybill_transporter(self):
        return self.client.save_waybill_transporter(self.user, self.password)

    def send_waybil_vd(self):
        return self.client.send_waybil_vd(self.user, self.password)

    def send_waybill(self):
        return self.client.send_waybill(self.user, self.password)

    def send_waybill_transporter(self):
        return self.client.send_waybill_transporter(self.user, self.password)

    def update_service_user(self):
        return self.client.update_service_user(self.user, self.password)

    def what_is_my_ip(self):
        return self.client.what_is_my_ip()
