#!/usr/bin/python3
# coding=utf8

red = "\033[0;31;1m"
green = "\033[0;32;1m"
yellow = "\033[0;33;1m"
magenta = "\033[0;35;1m"
cyan = "\033[0;36;1m"
default = "\033[0m"

print("\t Punycode 字符替换")

key = {
    "a": "а",
    "b": "ь",
    "c": "с",
    "d": "d",
    "e": "е",
    "f": "f",  # ENG
    "g": "g",  # ENG
    "h": "Н",
    "i": "І",
    "j": "Ј",
    "k": "к",
    # "K": "К",  # UPPERCASE (Alt.)
    "l": "ӏ",
    "m": "м",
    # "M": "М",  # UPPERCASE (Alt.)
    "n": "и",
    "o": "о",
    "p": "р",
    "q": "ԛ",
    "r": "г",
    "s": "ѕ",
    "t": "т",
    "u": "u",  # ENG
    "v": "v",  # ENG
    "w": "ԝ",
    "x": "х",
    "y": "у",
    "z": "z",  # ENG
}
try:
    ascii = str(input(cyan + "输入要转换为的ASCII字符串(不区分大小写,非符号):" + green))
    ascii = ascii.lower()
    print(red + " ASCII: " + cyan + ascii, magenta + "转换后的 Unicode (Cyrillic-西里尔文) 如下: " + cyan)
    if ("f" in ascii) or ("g" in ascii) or ("u" in ascii) or ("v" in ascii) or ("z" in ascii):
        print("ASCII 中包含 存在明显差异的字符串，这些字符串将不进行替换，如：f，g，u，v，z")

    I = 0
    while I < len(ascii):
        if key.get(ascii[I]):
            ens = ascii.replace(ascii[I], key.get(ascii[I]))
            print((" ASCII[" + magenta + "%s,hex(%s)" + cyan + "]->NewCode[" + magenta + "%s,hex(%s)" + cyan + "]") 
            % (ascii[I], hex(ord(ascii[I])), key.get(ascii[I]), hex(ord(key.get(ascii[I])))),end=' ')
            print(ascii.replace(ascii[I], red + key.get(ascii[I]) + cyan),"[Domain:xn--%s]" % ens.encode('punycode').decode('utf-8'))
        I += 1

    print(default + "\n")
except Exception as e:
    print("\n\n" + red + "转换错误:请输入英文字母中的字符." + default + "\n")
