import re


def formatString(s):
    return re.sub('\s|\t|\n', '', s)
