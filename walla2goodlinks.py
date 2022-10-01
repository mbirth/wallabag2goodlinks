#!/usr/bin/env python3

import html
import json
import re
from datetime import datetime

# https://stackoverflow.com/questions/9662346/python-code-to-remove-html-tags-from-a-string
CLEANR = re.compile(r"<.*?>")

with open("Wallabag All articles.json", "rt") as f:
    json_obj = json.load(f)

output_obj = []
for rec in json_obj:
    time_added = datetime.fromisoformat(rec["created_at"])
    time_read = time_added
    html_str = html.unescape(rec["content"])
    html_str = html_str.replace("\n", " ")
    html_str = re.sub(CLEANR, "", html_str)
    tags = rec["tags"]
    tags.append("+IMPORTED")
    new_obj = {
        "readAt": time_read.timestamp(),
        "addedAt": time_added.timestamp(),
        "summary": html_str[:199],
        "starred": (rec["is_starred"] == 1),
        "title": rec["title"],
        "tags": tags,
        "url": rec["url"],
    }
    print(repr(rec))
    print(repr(new_obj))
    output_obj.append(new_obj)

with open("walla2goodlinks.json", "w") as f:
    json.dump(output_obj, f)
