#!/usr/bin/python
# coding=utf8

import json

red = "\033[0;31;1m"
green = "\033[0;32;1m"
yellow = "\033[0;33;1m"
magenta = "\033[0;35;1m"
cyan = "\033[0;36;1m"
default = "\033[0m"

print("\t Punycode 字符生成")

def hand(name, start, end, output):
    _start, _end = int(start, 16), int(end, 16)
    for i in range(_start, _end):
        try:
            unicode_str = str(hex(i))[2:].zfill(4).encode('utf-8')
            #print(unicode_str)
            new_str = unicode_str.decode("unicode_escape")
            if new_str.strip() != "":
                output.write("[%s]" % name.encode("utf8") + "-" + unicode_str.decode('utf-8') + "-")
                output.write(new_str)
                output.write("\n")
                output.flush()
        except Exception as e:
            print(e)


list_key = json.loads(open("./unicode.json", "r").read())

print("输出字符表...")
for key in list_key.keys():
    start, end = list_key[key]
    output = open("./out/%s.txt" % key.replace(" ",""), "w")
    print("\t 输入表: %s" % key.encode("utf8"))
    hand(key, start, end, output)
    output.close()
