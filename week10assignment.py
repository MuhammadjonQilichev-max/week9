def track_usage(data_log):
    data = {}
    for i in data_log:
        d, u, m = i.split(';')
        if d in data:
            lst = data[d]
            lst.append((u, int(m)))
            data[d] = lst
        else:
            data[d] = [(u, int(m))]
    return data
def audit_departments(network_dict: dict) -> str:
    s = ''
    for i, j in network_dict.items():
        s += str(i)+': '
        total_mb = 0
        for user, mb in j:
            total_mb += mb
        s += f"{total_mb} MB total\n"
    return s
# Testing Inputs (Copy this into your code):

data_log = [
    "Sales;Alice;500",
    "Engineering;Bob;1200",
    "Sales;Charlie;300",
    "HR;David;150",
    "Engineering;Eve;800",
    "HR;Frank;100"
]
print(audit_departments(track_usage(data_log)))
# Expected Output:

# Sales: 800 MB total
# Engineering: 2000 MB total
# HR: 250 MB total