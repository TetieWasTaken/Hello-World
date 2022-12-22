#!/usr/bin/env python3

# Credits to @Richienb, @yahesh and @MrBrain295 for the original code!

import os
from urllib.parse import quote
import re


def regexReplace(string, search, replacement):
    return re.compile(search).sub(replacement, string)


languageCount = 0
languagesText = ""

root_dir = "Hello, World!"
language_dir = "EN"

# List the available languages
for directory in sorted(os.listdir(os.path.join(root_dir, language_dir))):
    if not (directory == '.' or directory == '..' or directory[0] == '.'
            or os.path.isfile(directory)):
        for filename in sorted(os.listdir(os.path.join(root_dir, language_dir, directory)), key=lambda s: s.lower()):
            if os.path.isfile(os.path.join(root_dir, language_dir, directory, filename)):
                language = (os.path.splitext(filename)[0].replace(
                    "-", "-").replace("∕", "/").replace("＼", "\\").replace(
                        "˸", ":").replace("∗", "*").replace("？", "?").replace(
                            "＂",
                            "\"").replace("﹤",
                                          "<").replace("﹥",
                                                       ">").replace("❘", "|"))
                file_path = os.path.join(root_dir, language_dir, directory, filename)
                languagesText += f'* [{language}]({quote(file_path)})\n'
                languageCount += 1

result = f"""<!--Languages start-->
## Languages ({languageCount} total)
{languagesText}<!--Languages end-->"""

readmeContents = open('readme.md', 'r', encoding="utf-8").read()

open('readme.md', 'w', encoding="utf-8").write(
    regexReplace(readmeContents,
                 r"<!--Languages start-->(.|\n)*<!--Languages end-->", result))