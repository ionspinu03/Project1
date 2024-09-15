from request_report import vlt_lists
from create_ct_lists.data_operation import search_element


def create_ct_list():
    ct_formated_list = formate_outlet_list()
    return ct_formated_list

def formate_outlet_list():
    ct_formated_list = []
    # request for obtail list vlt
    ct_list = vlt_lists()
    ct_list = search_element()
    # return ct_list
    ct_formated_list = ct_formated_list + ct_list
    return ct_formated_list

