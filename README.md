# precinct_lookup
a web form that gets ward/precinct from a chicago address, with autocomplete

# to-dos
## s3 
upload json files to bucket
note: each json file is named after a distinct numeric portion of a chicago address
the structure of each file is as follows:
{'address':{'ward':ward_no,'precinct':precinct_no} ... }

these files can be optimized by 1.) reducing key size e.g. 'w','p', 2.) restructuring the json, e.g. 'address':\[w,p\]' or 3.) via compression. that said, the largest file is <10kb.


## js
create a 'look up your ward' form field

on space bar push, take the first (numeric) string segment, e.g. '111'

use that string segment to async look up the appropriate json file, i.e., 111.json

use contents of that file's keys to populate autocomplete options, e.g. '111 N This, 111 S That, etc.'

user selects an option, e.g. '111 W Jackson' from autocomplete, which is the key to identify ward/precinct
