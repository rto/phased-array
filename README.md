# Phased Array

## What?

A script that generates a privacy-focussed list of tracker domains that have been identified by [DuckDuckGo's Tracker Radar](https://spreadprivacy.com/duckduckgo-tracker-radar/) for use in ad blocker solutions like pi-hole.

## Requirements?

This script requires Python >= 3.6.

## How?

```bash
git clone --recurse-submodules https://github.com/rto/phased-array.git phased-array
cd phased-array
python generate_lists.py
```

You can customise the input directory, output file pathname, and the line prefix via the command-line (see `--help` for a full list):

```bash
python generate_lists.py --input-directory my-tracker/domains --output-pathname /path/to/my-output.txt --line-prefix '203.0.113.1 '
```

## Limitations / Warnings

At present this is a particularly blunt tool, blocking entire domains, rather than individual trackers. This may result in 'undesirable behaviour', i.e. your favourite website/app may stop working.

**For example, github.com will be blocked by default.**

## Future improvements

 - Generate different types of output (domains, hosts, regex)
 - Allow a threshold to be set for inclusion

Any help on these gratefully received! :-)

## Source data

This project makes use of the Tracker Radar data from DuckDuckGo is [licensed](https://raw.githubusercontent.com/duckduckgo/tracker-radar/master/LICENSE) under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
