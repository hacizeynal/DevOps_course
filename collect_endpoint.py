"""
First version of this script will be used to collect all IP/MAC mappings from full ACI fabric
"""
# new comment from GitHub

from login_request import get_token
import requests
import json
from prettytable import PrettyTable

apic_ip = "10.66.51.90"
base_url = 'https://%s/api/' % apic_ip
token = get_token()

request_url = '/node/class/fvCEp.json'
# string concatenation with base URL and lldp query
request_endpoint_data = requests.get(base_url + request_url, cookies=token, verify=False)
structured_output = json.loads(request_endpoint_data.text)  # convert JSON to dictionary
fields = [ 'mac', 'encap', 'hostingServer','dn']
data = [ ]
for endpoints in structured_output [ "imdata" ]:
    for endpoint_data in endpoints [ "fvCEp" ].items():
        # print(endpoint_data)
        line_dict = {}
        for field in fields:
            line_dict [ field ] = endpoint_data [ 1 ] [ field ]
        data.append(line_dict)
# print(data)
table = PrettyTable()
table.field_names = ['IP Address','MAC Address',"VLAN","Tenant"]
for row in data:
    table.add_row([row['hostingServer'],row['mac'],row["encap"],row['dn'].split("/")[1]])
print(table)
