# Phased Array

## What?

A script that generates a privacy-focussed list of tracker domains that have been identified by [DuckDuckGo's Tracker Radar](https://spreadprivacy.com/duckduckgo-tracker-radar/) for use in ad blocker solutions like pi-hole.

## Requirements

This script requires Python >= 3.6.

## How?

```bash
git clone --recurse-submodules https://github.com/rto/phased-array.git phased-array
cd phased-array
python generate_lists.py
```

You can customise the input directory, output file pathname, and the line prefix via the command-line.

You will likely also want to pick which [categories](https://github.com/duckduckgo/tracker-radar/blob/master/docs/CATEGORIES.md) you want to exclude from the list (see Limitations / Warnings below).

Setting a `--line-prefix` can be used to generate a `hosts` formatted list.

```bash
python generate_lists.py \
    --input-directory my-tracker/domains \
    --output-pathname /path/to/my-output.txt \
    --line-prefix '127.0.0.1 ' \
    --exclude-uncategorized \
    --exclude-category CDN \
    --exclude-category 'Embedded Content' \
    --exclude-category 'Federated Login'
```

See `--help` for a full list of configuration options.

## Limitations / Warnings

_Striking a balance between privacy and usability is tough!_

Blocking by domain name can be a particularly blunt tool. By default the Tracker Radar includes domains for many popular websites and apps that you may wish to use on a daily basis. If you do not set any _exclude categories_ then your output may result in 'undesirable behaviour', i.e. your favourite website/app may stop working.

**For example, github.com, google.com, paypal.com, etc would all be blocked if we included every single domain.**

By default we have chosen to exclude any domain that matches one or more of the following categories: CDN, Embedded Content, Federated Login, Non-tracking, Online Payment, SSO.

Depending on your personal preference or concerns you may wish to filter on different [categories](https://github.com/duckduckgo/tracker-radar/blob/master/docs/CATEGORIES.md).


## Future improvements

 - Generate different types of output (domains, hosts, regex)
 - Improve the way that we filter domains in or out of the list

Any help on these gratefully received! :-)

## Source data

This project makes use of the Tracker Radar data from DuckDuckGo is [licensed](https://raw.githubusercontent.com/duckduckgo/tracker-radar/master/LICENSE) under Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0).
