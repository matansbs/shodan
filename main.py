import shodan

SHODAN_API_KEY = "insert your API key here"

api = shodan.Shodan(SHODAN_API_KEY)


# Lookup the host®®
host = api.host('217.140.75.46')

# # Print general info
# print("""
#         IP: {}
#         Organization: {}
#         Operating System: {}
# """.format(host['ip_str'], host.get('org', 'n/a'), host.get('os', 'n/a')))
#
# # Print all banners
# for item in host['data']:
#         print("""
#                 Port: {}
#                 Banner: {}
#
#         """.format(item['port'], item['data']))
