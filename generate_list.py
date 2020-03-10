import argparse
import json
import os


INTRO_TEXT = """
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


def parse_args():
    parser = argparse.ArgumentParser(
        description="Produce a hosts file from DuckDuckGo's Tracker Radar"
    )
    parser.add_argument(
        "--input-directory", "-i",
        # type=str,
        help="Path to a directory containing Tracker Radar files",
        default="tracker-radar/domains",
    )
    parser.add_argument(
        "--output-pathname", "-o",
        help="Pathname of a file to write to",
        default="phased_array_hosts.txt"
    )
    parser.add_argument(
        "--line-prefix", "-l",
        help="Prefix for each line in the output file",
        default="127.0.0.1\t",
    )

    parser.add_argument(
        "--exclude-categories", "-e",
        help="Domains matching one or more of these categories will be skipped",
        default="CDN,Embedded Content,Federated Login,Non-tracking,Online Payment,SSO"
    )
    return parser.parse_args()


def main():
    args = parse_args()

    file_count = 0
    domain_count_inc = 0
    domain_count_exc = 0

    output_file = open(args.output_pathname, "w")
    output_file.write(INTRO_TEXT)

    file_list = os.scandir(args.input_directory)

    for entry in file_list:
        if not entry.is_file() or not entry.path.endswith(".json"):
            continue
        file_count += 1
        data = json.load(open(entry.path, "r"))
        category_match = set(data['categories']).intersection(args.exclude_categories.split(","))
        if len(category_match) == 0:
            domain_count_inc += 1
            print("Adding: " + data["domain"])
            output_file.write(args.line_prefix + data["domain"] + "\n")
        else:
            domain_count_exc +=1
            print("Skipping: " + data['domain'])

    file_list.close()
    output_file.close()

    print(f"Parsed {file_count} files and added {domain_count_inc}/{domain_count_inc+domain_count_exc} domains to {args.output_pathname}")

if __name__ == "__main__":
    main()
