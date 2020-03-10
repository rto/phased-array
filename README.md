# Phased Array

## What?

A script that generates a privacy-focussed list of tracker domains that have been identified by [DuckDuckGo's Tracker Radar](https://spreadprivacy.com/duckduckgo-tracker-radar/) for use in ad blocker solutions like pi-hole.

## How?

`python generate_lists.py`

You can customise a few things by editing the variables at the top of **generate_lists.py**:

 - *input_directory* tells the script where to look for the .json files from the domains directory of the source data. (Default: 'tracker-radar/domains/')
 - *output_file* specifies where the output should be written to. (Default: 'phased_array_hosts.txt')
 - *line_prefix* is added to each line before the domain. (Default: '127.0.0.1	')
 - *intro_text* appears in the output file above the block list.

## Limitations / Warnings

At present this is a particularly blunt tool, blocking entire domains, rather than individual trackers. This may result in 'undesirable behaviour', i.e. your favourite website/app may stop working.

**For example, github.com will be blocked by default.**

## Future improvements

 - Generate different types of output (domains, hosts, regex)
 - Allow a threshold to be set for inclusion

Any help on these gratefully received! :-)

## Source data

This project makes use of the Tracker Radar data from DuckDuckGo is [licensed](https://raw.githubusercontent.com/duckduckgo/tracker-radar/master/LICENSE) under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
