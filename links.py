
def select_link(raport):

    if raport == "outlet":
        url = "https://wrmi.s219.vnet.services/ctTransactionsReport/form"
    elif raport == "ct":
        url = "https://wrmi.s219.vnet.services/ctTransactionsReport/execute"
    elif raport == "vlt":
        # url = "https://wrmi.s219.vnet.services/scopeSelectionFeatureReport/getOutletDevices"
        url ="https://wrmi.s219.vnet.services/ct/getCts"
    elif raport == "Job list":
        url = "https://wrmi.s219.vnet.services/recentReports/list"
    elif raport == "Open report by ID":
        url = "https://wrmi.s219.vnet.services/ctTransactionsReport/viewReport"
    return url