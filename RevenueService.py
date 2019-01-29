from suds.client import Client


class ServiceClient:
    mainUser = ""
    mainPass = ""

    def __init__(self, user: str, password: str):
        self.client = Client("http://services.rs.ge/WayBillService/WayBillService.asmx?WSDL")
        self.user = user
        self.password = password
        self.client.set_options(timeout=260)

    def chek_service_user(self):
        return RS_GE_Responses.chek_service_user_response(
            self.client.service.chek_service_user(self.user, self.password))

    def close_waybill(self, idWayBill: int) -> int:
        return self.client.service.close_waybill(self.user, self.password, idWayBill)

    def close_waybill_transporter(self, waybill_id: int, reception_info: str, receiver_info: str, delivery_date) -> int:
        return self.client.service.close_waybill_transporter(self.user, self.password, waybill_id, reception_info,
                                                             receiver_info, delivery_date)

    def close_waybill_vd(self, delivery_date, waybill_id: int) -> int:
        return self.client.service.close_waybill_vd(self.user, self.password, delivery_date, waybill_id)

    def confirm_waybill(self, waybill_id: int) -> bool:
        return self.client.service.confirm_waybill(self.user, self.password, waybill_id)

    def create_service_user(self, name: str, su: str, sp: str) -> bool:
        if self.mainUser == self.mainPass == "":
            raise Exception("Please input main user and pass")
        ip = self.what_is_my_ip()
        return self.client.service.create_service_user(self.mainUser, self.mainPass, ip, name, su, sp)

    def del_waybill(self, waybill_id: int) -> int:
        return self.client.service.del_waybill(self.user, self.password, waybill_id)

    def delete_bar_code(self, bar_code: str) -> int:
        return self.client.service.delete_bar_code(self.user, self.password, bar_code)

    def delete_car_numbers(self, car_number: str) -> int:
        return self.client.service.delete_car_numbers(self.user, self.password, car_number)

    def delete_waybill_tamplate(self, id: int) -> int:
        return self.client.service.delete_waybill_tamplate(self.user, self.password, id)

    def get_adjusted_waybill(self, id: int):
        return RS_GE_Responses.get_adjusted_waybill_response(
            self.client.service.get_adjusted_waybill(self.user, self.password, id))

    def get_adjusted_waybills(self, waybill_id: int):
        return self.client.service.get_adjusted_waybills(self.user, self.password, waybill_id)

    def get_akciz_codes(self, s_text: str = ""):
        return self.client.service.get_akciz_codes(self.user, self.password, s_text)

    def get_bar_codes(self, bar_code: str):
        return RS_GE_Responses.get_bar_codes_response(
            self.client.service.get_bar_codes(self.user, self.password, bar_code))

    def get_buyer_waybilll_goods_list(self, itypes: str = "", seller_tin: str = "", statuses: str = "",
                                      car_number: str = "",
                                      begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                                      driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                                      full_amount: float = 0, waybill_number: str = "",
                                      close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = ""):
        resp = self.client.service.get_buyer_waybilll_goods_list(self.user, self.password, itypes, seller_tin, statuses,
                                                                 car_number,
                                                                 begin_date_s, begin_date_e, create_date_s,
                                                                 create_date_e, driver_tin,
                                                                 delivery_date_s, delivery_date_e, full_amount,
                                                                 waybill_number, close_date_s,
                                                                 close_date_e, s_user_ids, comment)
        return RS_GE_Responses.get_buyer_waybilll_goods_list(resp)

    def get_buyer_waybills(self, itypes: str = "", seller_tin: str = "", statuses: str = "", car_number: str = "",
                           begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                           driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                           full_amount: float = 0, waybill_number: str = "",
                           close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = ""):
        resp = self.client.service.get_buyer_waybills(self.user, self.password, itypes, seller_tin, statuses,
                                                      car_number,
                                                      begin_date_s, begin_date_e, create_date_s, create_date_e,
                                                      driver_tin,
                                                      delivery_date_s, delivery_date_e, full_amount, waybill_number,
                                                      close_date_s,
                                                      close_date_e, s_user_ids, comment)
        return RS_GE_Responses.get_buyer_waybills(resp)

    def get_buyer_waybills_ex(self, itypes: str = "", seller_tin: str = "", statuses: str = "", car_number: str = "",
                              begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                              driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                              full_amount: float = 0, waybill_number: str = "",
                              close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = "",
                              is_confirmed: int = 0):
        resp = self.client.service.get_buyer_waybills_ex(self.user, self.password, itypes, seller_tin, statuses,
                                                         car_number,
                                                         begin_date_s, begin_date_e, create_date_s, create_date_e,
                                                         driver_tin,
                                                         delivery_date_s, delivery_date_e, full_amount, waybill_number,
                                                         close_date_s,
                                                         close_date_e, s_user_ids, comment, is_confirmed)
        return RS_GE_Responses.get_buyer_waybills(resp)

    def get_c_waybill(self, s_dt, e_dt):
        return self.client.service.get_c_waybill(self.user, self.password, s_dt, e_dt)

    def get_car_numbers(self):
        return RS_GE_Responses.get_car_numbers(self.client.service.get_car_numbers(self.user, self.password))

    def get_error_codes(self):
        return RS_GE_Responses.get_error_codes_response(self.client.service.get_error_codes(self.user, self.password))

    def get_name_from_tin(self, tin: str):
        return self.client.service.get_name_from_tin(self.user, self.password, tin)

    def get_payer_type_from_un_id(self, un_id: int):
        return self.client.service.get_payer_type_from_un_id(self.user, self.password, un_id)

    def get_print_pdf(self, waybill_id: int):
        return self.client.service.get_print_pdf(self.user, self.password, waybill_id)

    def get_server_time(self):
        return self.client.service.get_server_time()

    def get_service_users(self):
        if self.mainUser == self.mainPass == "":
            raise Exception("Please input main user and pass")
        return self.client.service.get_service_users(self.mainUser, self.mainPass)

    def get_tin_from_un_id(self, un_id: int):
        return self.client.service.get_tin_from_un_id(self.user, self.password, un_id)

    def get_transporter_waybills(self, itypes: str = "", seller_tin: str = "", statuses: str = "", car_number: str = "",
                                 begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                                 driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                                 full_amount: float = 0, waybill_number: str = "",
                                 close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = "",
                                 is_confirmed: int = 0):
        return self.client.service.get_transporter_waybills(self.user, self.password, itypes, seller_tin, statuses,
                                                            car_number,
                                                            begin_date_s, begin_date_e, create_date_s, create_date_e,
                                                            driver_tin,
                                                            delivery_date_s, delivery_date_e, full_amount,
                                                            waybill_number, close_date_s,
                                                            close_date_e, s_user_ids, comment, is_confirmed)

    def get_trans_types(self):
        return self.client.service.get_trans_types(self.user, self.password)

    def get_waybill(self, waybill_id: int):
        return self.client.service.get_waybill(self.user, self.password, waybill_id)

    def get_waybill_by_number(self, waybill_number: str):
        return self.client.service.get_waybill_by_number(self.user, self.password, waybill_number)

    def get_waybill_goods_list(self, itypes: str = "", seller_tin: str = "", statuses: str = "", car_number: str = "",
                               begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                               driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                               full_amount: float = 0, waybill_number: str = "",
                               close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = "", ):
        resp = self.client.service.get_waybill_goods_list(self.user, self.password, itypes, seller_tin, statuses,
                                                          car_number,
                                                          begin_date_s, begin_date_e, create_date_s, create_date_e,
                                                          driver_tin,
                                                          delivery_date_s, delivery_date_e, full_amount, waybill_number,
                                                          close_date_s,
                                                          close_date_e, s_user_ids, comment)
        return RS_GE_Responses.get_waybill_goods_list(resp)

    def get_waybill_tamplate(self, id: int):
        return self.client.service.get_waybill_tamplate(self.user, self.password, id)

    def get_waybill_tamplates(self):
        return self.client.service.get_waybill_tamplates(self.user, self.password)

    def get_waybill_types(self):
        return self.client.service.get_waybill_types(self.user, self.password)

    def get_waybill_units(self):
        return self.client.service.get_waybill_units(self.user, self.password)

    def get_waybills(self, itypes: str = "", seller_tin: str = "", statuses: str = "", car_number: str = "",
                     begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                     driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                     full_amount: float = 0, waybill_number: str = "",
                     close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = ""):
        response = self.client.service.get_waybills(self.user, self.password, itypes, seller_tin, statuses, car_number,
                                                begin_date_s, begin_date_e, create_date_s, create_date_e, driver_tin,
                                                delivery_date_s, delivery_date_e, full_amount, waybill_number,
                                                close_date_s,
                                                close_date_e, s_user_ids, comment)
        return RS_GE_Responses.get_waybills(response)

    def get_waybills_ex(self, itypes: str = "", seller_tin: str = "", statuses: str = "", car_number: str = "",
                        begin_date_s=None, begin_date_e=None, create_date_s=None, create_date_e=None,
                        driver_tin: str = "", delivery_date_s=None, delivery_date_e=None,
                        full_amount: float = 0, waybill_number: str = "",
                        close_date_s=None, close_date_e=None, s_user_ids: str = "", comment: str = "",
                        is_confirmed: int = 0):
        return self.client.service.get_waybills_ex(self.user, self.password, itypes, seller_tin, statuses, car_number,
                                                   begin_date_s, begin_date_e, create_date_s, create_date_e, driver_tin,
                                                   delivery_date_s, delivery_date_e, full_amount, waybill_number,
                                                   close_date_s,
                                                   close_date_e, s_user_ids, comment, is_confirmed)

    def get_wood_types(self):
        return self.client.service.get_wood_types(self.user, self.password)

    def is_vat_payer(self, un_id: int):
        return self.client.service.is_vat_payer(self.user, self.password, un_id)

    def is_vat_payer_tin(self, tin: str):
        return self.client.service.is_vat_payer_tin(self.user, self.password, tin)

    def ref_waybill(self, waybill_id: int):
        return self.client.service.ref_waybill(self.user, self.password, waybill_id)

    def ref_waybill_vd(self, waybill_id: int, comment: str = "", ):
        return self.client.service.ref_waybill_vd(self.user, self.password, waybill_id, comment)

    def reject_waybill(self, waybill_id: int):
        return self.client.service.reject_waybill(self.user, self.password, waybill_id)

    def save_bar_code(self, bar_code: str, goods_name: str, unit_id: int, unit_txt: str, a_id: int):
        return self.client.service.save_bar_code(self.user, self.password, bar_code, goods_name, unit_id, unit_txt,
                                                 a_id)

    def save_car_numbers(self, car_number: str):
        return self.client.service.save_car_numbers(self.user, self.password, car_number)

    def save_invoice(self, waybill_id: int, in_inv_id: int):
        return self.client.service.save_invoice(self.user, self.password, waybill_id, in_inv_id)

    def save_waybill(self, waybill: str):
        return self.client.service.save_waybill(self.user, self.password, waybill)

    def save_waybill_tamplate(self, v_name: str, waybill: str):
        return self.client.service.save_waybill_tamplate(self.user, self.password, v_name, waybill)

    def save_waybill_transporter(self, waybill_id: int, car_number: str, driver_tin: str, chek_driver_tin: int,
                                 driver_name: str, trans_id: int, trans_txt: str, reception_info: str = "",
                                 receiver_info: str = ""):
        return self.client.service.save_waybill_transporter(self.user, self.password, car_number, driver_tin,
                                                            chek_driver_tin, driver_name, trans_id, trans_txt,
                                                            reception_info, receiver_info)

    def send_waybil_vd(self, begin_date, waybill_id: int):
        return self.client.service.send_waybil_vd(self.user, self.password, begin_date, waybill_id)

    def send_waybill(self, waybill_id: int):
        return self.client.service.send_waybill(self.user, self.password, waybill_id)

    def send_waybill_transporter(self, waybill_id: int, begin_date):
        return self.client.service.send_waybill_transporter(self.user, self.password, waybill_id, begin_date)

    def update_service_user(self):
        if self.mainUser == self.mainPass == "":
            raise Exception("Please input main user and pass")
        return self.client.service.update_service_user(self.mainUser, self.mainPass)

    def what_is_my_ip(self) -> str:
        return self.client.service.what_is_my_ip()


class RS_GE_Responses:
    class chek_service_user_response:
        def __init__(self, response):
            self.chek_service_userResult: bool = response["chek_service_userResult"]
            self.un_id: int = response["un_id"]
            self.s_user_id: int = response["s_user_id"]

        def __str__(self):
            return "chek_service_user_resonse\n\tchek_service_userResult:{0}\n\tun_id:{1}\n\ts_user_id:{2}" \
                .format(self.chek_service_userResult, self.un_id, self.s_user_id)

    class get_error_codes_response:
        def __init__(self, response):
            self.ERROR_CODES: list = response[0][0]

        def __str__(self):
            result = "ERROR_CODES"
            for i in self.ERROR_CODES:
                if 'TYPE' in i:
                    result += "\n\tID:{0},TEXT:{1},TYPE:{2}".format(i["ID"], i["TEXT"], i["TYPE"])
                else:
                    result += "\n\tID:{0},TEXT:{1}".format(i["ID"], i["TEXT"])
            return result

        def __getitem__(self, item):
            return self.ERROR_CODES[item]

        def __setitem__(self, key, value):
            self.ERROR_CODES[key] = value

        def __delitem__(self, key):
            self.ERROR_CODES.remove(self.ERROR_CODES[key])

        def get_error(self, id):
            for i in self.ERROR_CODES:
                if i['ID'] == id:
                    return i

        def get_error_text(self, id):
            for i in self.ERROR_CODES:
                if i['ID'] == id:
                    return i['TEXT']

    class get_adjusted_waybill_response:
        def __init__(self, response):
            self.RESULT: list = response[0]

        def __str__(self):
            return str(self.RESULT)

    class get_bar_codes_response:

        def __init__(self, response):
            self.get_bar_codesResult = response['get_bar_codesResult']
            self.BAR_CODES: list = []
            for i in response[1][0][0]:
                self.BAR_CODES.append(i)

        def __getitem__(self, item):
            return self.BAR_CODES[item]

        def __setitem__(self, key, value):
            self.BAR_CODES[key] = value

        def __delitem__(self, key):
            self.BAR_CODES.remove(self.BAR_CODES[key])

        def __str__(self):
            return self.BAR_CODES

    class get_car_numbers:
        def __init__(self, response):
            self.get_car_numbersResult = response['get_car_numbersResult']
            self.car_numbers: list = response['car_numbers'][0]

        def __getitem__(self, item):
            return self.car_numbers[item]

        def __setitem__(self, key, value):
            self.car_numbers[key] = value

        def __delitem__(self, key):
            self.car_numbers.remove(self.car_numbers[key])

        def __len__(self):
            return len(self.car_numbers)

        def __str__(self):
            return 'get_car_numbersResult:{0},car_numbers:{1}'.format(self.get_car_numbersResult, self.car_numbers)

    class get_buyer_waybills:
        def __init__(self, response):
            if hasattr(response, 'RESULT'):
                self.STATUS = response['RESULT']['STATUS']
                self.SUB_WAYBILLS: list = response['RESULT']['SUB_WAYBILLS']
                self.GOODS_LIST: list = response['RESULT']['GOODS_LIST']
            else:
                self.WAYBILL_LIST: list = response[0][0]

        def __getitem__(self, item):
            if hasattr(self, 'STATUS'):
                return None
            else:
                return self.WAYBILL_LIST[item]

        def __len__(self):
            if hasattr(self, 'STATUS'):
                return 0
            else:
                return len(self.WAYBILL_LIST)

        def __str__(self):
            if hasattr(self, 'STATUS'):
                return 'STATUS:{0},SUB_WAYBILLS:{1},GOODS_LIST:{2}'.format(self.STATUS, self.SUB_WAYBILLS,
                                                                           self.GOODS_LIST)
            else:
                return str(self.WAYBILL_LIST)

    class get_buyer_waybilll_goods_list:
        def __init__(self, response):
            if hasattr(response, 'RESULT'):
                self.STATUS = response['RESULT']['STATUS']
                self.SUB_WAYBILLS: list = response['RESULT']['SUB_WAYBILLS']
                self.GOODS_LIST: list = response['RESULT']['GOODS_LIST']
            else:
                self.WAYBILL_LIST: list = response[0][0]

        def __getitem__(self, item):
            if hasattr(self, 'STATUS'):
                return None
            else:
                return self.WAYBILL_LIST[item]

        def __len__(self):
            if hasattr(self, 'STATUS'):
                return 0
            else:
                return len(self.WAYBILL_LIST)

        def __str__(self):
            if hasattr(self, 'STATUS'):
                return 'STATUS:{0},SUB_WAYBILLS:{1},GOODS_LIST:{2}'.format(self.STATUS, self.SUB_WAYBILLS,
                                                                           self.GOODS_LIST)
            else:
                return str(self.WAYBILL_LIST)

    class get_waybill_goods_list:
        def __init__(self, response):
            if hasattr(response, 'RESULT'):
                self.STATUS = response['RESULT']['STATUS']
                self.SUB_WAYBILLS: list = response['RESULT']['SUB_WAYBILLS']
                self.GOODS_LIST: list = response['RESULT']['GOODS_LIST']
            else:
                self.WAYBILL_LIST: list = response[0]

        def __getitem__(self, item):
            if hasattr(self, 'STATUS'):
                return None
            else:
                return self.WAYBILL_LIST[item]

        def __len__(self):
            if hasattr(self, 'STATUS'):
                return 0
            else:
                return len(self.WAYBILL_LIST)

        def __str__(self):
            if hasattr(self, 'STATUS'):
                return 'STATUS:{0},SUB_WAYBILLS:{1},GOODS_LIST:{2}'.format(self.STATUS, self.SUB_WAYBILLS,
                                                                           self.GOODS_LIST)
            else:
                return str(self.WAYBILL_LIST)

    class get_waybills:
        def __init__(self, response):
            if hasattr(response, 'RESULT'):
                self.STATUS = response['RESULT']['STATUS']
                self.SUB_WAYBILLS: list = response['RESULT']['SUB_WAYBILLS']
                self.GOODS_LIST: list = response['RESULT']['GOODS_LIST']
            else:
                self.WAYBILL_LIST: list = response[0]

        def __getitem__(self, item):
            if hasattr(self, 'STATUS'):
                return None
            else:
                return self.WAYBILL_LIST[item]

        def __len__(self):
            if hasattr(self, 'STATUS'):
                return 0
            else:
                return len(self.WAYBILL_LIST)

        def __str__(self):
            if hasattr(self, 'STATUS'):
                return 'STATUS:{0},SUB_WAYBILLS:{1},GOODS_LIST:{2}'.format(self.STATUS, self.SUB_WAYBILLS,
                                                                           self.GOODS_LIST)
            else:
                return str(self.WAYBILL_LIST)
