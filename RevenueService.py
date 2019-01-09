from suds.client import Client


class ServiceClient:
    mainUser = ""
    mainPass = ""

    def __init__(self, user: str, password: str):
        self.client = Client("http://services.rs.ge/WayBillService/WayBillService.asmx?WSDL")
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

    def get_buyer_waybills(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = ""):
        return self.client.get_buyer_waybills(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment)

    def get_buyer_waybills_ex(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = "",
                              is_confirmed:int = 0):
        return self.client.get_buyer_waybills_ex(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment,is_confirmed)

    def get_c_waybill(self,s_dt,e_dt):
        return self.client.get_c_waybill(self.user, self.password,s_dt,e_dt)

    def get_car_numbers(self):
        return self.client.get_car_numbers(self.user, self.password)

    def get_error_codes(self):
        return self.client.get_error_codes(self.user, self.password)

    def get_name_from_tin(self,tin:str):
        return self.client.get_name_from_tin(self.user, self.password,tin)

    def get_payer_type_from_un_id(self,un_id:int):
        return self.client.get_payer_type_from_un_id(self.user, self.password,un_id)

    def get_print_pdf(self,waybill_id:int):
        return self.client.get_print_pdf(self.user, self.password,waybill_id)

    def get_server_time(self):
        return self.client.get_server_time()

    def get_service_users(self):
        return self.client.get_service_users(self.mainUser, self.mainPass)

    def get_tin_from_un_id(self,un_id:int):
        return self.client.get_tin_from_un_id(self.user, self.password,un_id)

    def get_transporter_waybills(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = "",
                              is_confirmed:int = 0):
        return self.client.get_transporter_waybills(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment,is_confirmed)

    def get_trans_types(self):
        return self.client.get_trans_types(self.user, self.password)

    def get_waybill(self,waybill_id:int):
        return self.client.get_waybill(self.user, self.password,waybill_id)

    def get_waybill_by_number(self,waybill_number:str):
        return self.client.get_waybill_by_number(self.user, self.password,waybill_number)

    def get_waybill_goods_list(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = "",):
        return self.client.get_waybill_goods_list(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment)

    def get_waybill_tamplate(self,id:int):
        return self.client.get_waybill_tamplate(self.user, self.password,id)

    def get_waybill_tamplates(self):
        return self.client.get_waybill_tamplates(self.user, self.password)

    def get_waybill_types(self):
        return self.client.get_waybill_types(self.user, self.password)

    def get_waybill_units(self):
        return self.client.get_waybill_units(self.user, self.password)

    def get_waybills(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = ""):
        return self.client.get_waybills(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment)

    def get_waybills_ex(self,itypes:str = "",seller_tin:str = "",statuses:str = "",car_number:str = "",
                                      begin_date_s = None,begin_date_e = None,create_date_s = None,create_date_e = None,
                                      driver_tin:str = "",delivery_date_s = None,delivery_date_e = None,
                                      full_amount:float = 0,waybill_number:str = "",
                                      close_date_s = None,close_date_e = None,s_user_ids:str = "",comment:str = "",is_confirmed:int = 0):
        return self.client.get_waybills_ex(self.user, self.password,itypes,seller_tin,statuses,car_number,
                                                         begin_date_s,begin_date_e,create_date_s,create_date_e,driver_tin,
                                                         delivery_date_s,delivery_date_e,full_amount,waybill_number,close_date_s,
                                                         close_date_e,s_user_ids,comment,is_confirmed)

    def get_wood_types(self):
        return self.client.get_wood_types(self.user, self.password)

    def is_vat_payer(self,un_id:int):
        return self.client.is_vat_payer(self.user, self.password,un_id)

    def is_vat_payer_tin(self,tin:str):
        return self.client.is_vat_payer_tin(self.user, self.password,tin)

    def ref_waybill(self,waybill_id:int):
        return self.client.ref_waybill(self.user, self.password,waybill_id)

    def ref_waybill_vd(self,waybill_id:int,comment:str = "",):
        return self.client.ref_waybill_vd(self.user, self.password,waybill_id,comment)

    def reject_waybill(self,waybill_id:int):
        return self.client.reject_waybill(self.user, self.password,waybill_id)

    def save_bar_code(self,bar_code:str,goods_name:str,unit_id:int,unit_txt:str,a_id:int):
        return self.client.save_bar_code(self.user, self.password,bar_code,goods_name,unit_id,unit_txt,a_id)

    def save_car_numbers(self,car_number:str):
        return self.client.save_car_numbers(self.user, self.password,car_number)

    def save_invoice(self,waybill_id:int,in_inv_id:int):
        return self.client.save_invoice(self.user, self.password,waybill_id,in_inv_id)

    def save_waybill(self,waybill:str):
        return self.client.save_waybill(self.user, self.password,waybill)

    def save_waybill_tamplate(self,v_name:str,waybill:str):
        return self.client.save_waybill_tamplate(self.user, self.password,v_name,waybill)

    def save_waybill_transporter(self,waybill_id:int,car_number:str,driver_tin:str,chek_driver_tin:int,
                                 driver_name:str,trans_id:int,trans_txt:str,reception_info:str = "",receiver_info:str = ""):
        return self.client.save_waybill_transporter(self.user, self.password,car_number,driver_tin,
                                                    chek_driver_tin,driver_name,trans_id,trans_txt,reception_info,receiver_info)

    def send_waybil_vd(self,begin_date,waybill_id:int):
        return self.client.send_waybil_vd(self.user, self.password,begin_date,waybill_id)

    def send_waybill(self,waybill_id:int):
        return self.client.send_waybill(self.user, self.password,waybill_id)

    def send_waybill_transporter(self,waybill_id:int,begin_date):
        return self.client.send_waybill_transporter(self.user, self.password,waybill_id,begin_date)

    def update_service_user(self):
        return self.client.update_service_user(self.mainUser,self.mainPass)

    def what_is_my_ip(self):
        return self.client.what_is_my_ip()
