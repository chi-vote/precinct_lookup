import csv, json, re

### START CONFIG ###
#voter_reg_file_path = 'data/Chicago-Active-Inactive-Voters-2018-11-13.csv'
voter_reg_file_path = 'data/M2019-Precincts-Wards-By-Address.csv'
json_output_path = 'output/'
address_field, ward_field, precinct_field = 'Address','WRD','PCT'
### END CONFIG ###


# create dict
address_precincts = {}

# load data
voters = [x for x in csv.DictReader(open(voter_reg_file_path))]

# iterate through file,
# build dict
# with keys -> address:{ward,precinct}
for voter in voters:
    address_raw = voter[address_field]
    address = re.sub('\s+',' ',address_raw).strip()
    street_no = address.split(' ')[0]
    if street_no not in address_precincts:
        address_precincts[street_no] = {}
    # TODO: figure out how to chop off apt numbers
    if address not in address_precincts[street_no]:
        address_precincts[street_no][address] = {'ward':voter[ward_field],'precinct':voter[precinct_field]}

# for each key in dict:
# write json file named after key
for street_no in address_precincts:
    json_file_path = json_output_path + street_no + '.json'
    json_file = open(json_file_path,'w')
    json.dump(address_precincts[street_no],json_file)
    json_file.close()
    
