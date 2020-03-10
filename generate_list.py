import os
import json

input_directory = 'tracker-radar/domains/'
output_file = 'phased_array_hosts.txt'
line_prefix = '127.0.0.1	'
intro_text = """
# # PHASED ARRAY
#
# A privacy-focussed list of tracker domains that have been identified by
# DuckDuckGo's Tracker Radar for use in ad blocker solutions like pi-hole.
#
# At present this is a particularly blunt tool, blocking entire domains,
# rather than individual trackers. This may result in 'undesirable
# behaviour', i.e. your favourite website/app may stop working.
#
# Project website:
#
#  - https://github.com/rto/phased-array
#
# Find out more about Tracker Radar at:
#
#  - https://spreadprivacy.com/duckduckgo-tracker-radar/
#  - https://github.com/duckduckgo/tracker-radar
#
# Find out more about Pi-hole at:
#
#  - https://pi-hole.net

"""

output_buffer = ''
file_count = 0
domain_count = 0

file_list = os.scandir(input_directory)

for entry in file_list:
	if (entry.path.endswith(".json") and entry.is_file()):
		file_count += 1
		print("Parsing : " + entry.path)
		data = json.load(open(entry.path, 'r'))
		print("Adding  : " + data['domain'])
		output_buffer += line_prefix + data['domain'] + '\n'

file_list.close()

print ("Files   : " + str(file_count))
print ("Writing : " + output_file)

out = open(output_file, "w")
out.write(intro_text)
out.write(output_buffer)
out.close()

print ("DONE!")
