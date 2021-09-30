#!/usr/bin/python3

import _location as location

# Test data.
test_data = {
        '123.125.71.29/32': {
            'ccode': 'CN',
            'cname': 'China',
            'ccontinent': 'AS',
            'asnumber': 4808,
            'asname': 'China Unicom', 
        },
        '82.165.177.154/32': {
            'ccode': 'DE',
            'cname': 'Germany',
            'ccontinent': 'EU',
            'asnumber': 8560,
            'asname': '1&1 IONOS SE',
        }
    }

db = location.Writer()

# Set the vendor
db.vendor = "suricata-verify"

# Set a description
db.description = "suricata-verify location test database"

# Set a license
db.license = "CC"

# Loop through the dict of testdata
for addr, data in test_data.items():
    # Add country and details
    country = db.add_country(data["ccode"])
    country.continent_code = data["ccontinent"]
    country.name = data["cname"]

    # Add AS and data
    asn = db.add_as(data["asnumber"])
    asn.name = data["asname"]

    # Add a network
    net = db.add_network(addr)
    net.country_code = data["ccode"]
    net.asn = asn.number

# Write the database to disk
db.write("test.db")
