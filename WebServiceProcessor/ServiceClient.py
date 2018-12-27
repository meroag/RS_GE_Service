import GlobalVariables
from WebServiceProcessor.WsdlWrapper import Wrapper
from enum import Enum


class ServiceList(Enum):
    chek_service_user = "chek_service_user"
    close_waybill = "close_waybill"
    close_waybill_transporter = "close_waybill_transporter"
    close_waybill_vd = "close_waybill_vd"
    confirm_waybill = "confirm_waybill"
    create_service_user = "create_service_user"
    del_waybill = "del_waybill"
    delete_bar_code = "delete_bar_code"
    delete_car_numbers = "delete_car_numbers"
    delete_waybill_tamplate = "delete_waybill_tamplate"
    get_adjusted_waybill = "get_adjusted_waybill"
    get_adjusted_waybills = "get_adjusted_waybills"
    get_akciz_codes = "get_akciz_codes"
    get_bar_codes = "get_bar_codes"
    get_buyer_waybilll_goods_list = "get_buyer_waybilll_goods_list"
    get_buyer_waybills = "get_buyer_waybills"
    get_buyer_waybills_ex = "get_buyer_waybills_ex"
    get_c_waybill = "get_c_waybill"
    get_car_numbers = "get_car_numbers"
    get_error_codes = "get_error_codes"
    get_name_from_tin = "get_name_from_tin"
    get_payer_type_from_un_id = "get_payer_type_from_un_id"
    get_print_pdf = "get_print_pdf"
    get_server_time = "get_server_time"
    get_service_users = "get_service_users"
    get_tin_from_un_id = "get_tin_from_un_id"
    get_trans_types = "get_trans_types"
    get_transporter_waybills = "get_transporter_waybills"
    get_waybill = "get_waybill"
    get_waybill_by_number = "get_waybill_by_number"
    get_waybill_goods_list = "get_waybill_goods_list"
    get_waybill_tamplate = "get_waybill_tamplate"
    get_waybill_tamplates = "get_waybill_tamplates"
    get_waybill_types = "get_waybill_types"
    get_waybill_units = "get_waybill_units"
    get_waybills = "get_waybills"
    get_waybills_ex = "get_waybills_ex"
    get_wood_types = "get_wood_types"
    is_vat_payer = "is_vat_payer"
    is_vat_payer_tin = "is_vat_payer_tin"
    ref_waybill = "ref_waybill"
    ref_waybill_vd = "ref_waybill_vd"
    reject_waybill = "reject_waybill"
    save_bar_code = "save_bar_code"
    save_car_numbers = "save_car_numbers"
    save_invoice = "save_invoice"
    save_waybill = "save_waybill"
    save_waybill_tamplate = "save_waybill_tamplate"
    save_waybill_transporter = "save_waybill_transporter"
    send_waybil_vd = "send_waybil_vd"
    send_waybill = "send_waybill"
    send_waybill_transporter = "send_waybill_transporter"
    update_service_user = "update_service_user"
    what_is_my_ip = "what_is_my_ip"


def is_vat_payer_tin(org_code):
    params = GlobalVariables.ServiceParameters()
    wr = Wrapper(ServiceList.is_vat_payer_tin.value)
    wr.data = {
        "su":params.su,
        "sp":params.sp,
        "tin":str(org_code)
    }
    x = wr.create_response()
    return x[0].values()
