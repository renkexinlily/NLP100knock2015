#!/usr/bin/python
#-*-coding:utf-8-*-
#2015/06/03 17:44:14 Shin Kanouchi

import argparse
import knock020
import knock025
import re


def main(info_dic):
    infobox = dict([(key, value.replace("'''''", "").replace("'''", "").replace("''", "")) for key, value in info_dic.items()])
    infobox = dict([(key, re.sub(r"\[\[.*\]\]", lambda x: x.group().replace("[[", "").replace("]]", "").split("|")[0].split("#")[0], value)) for key, value in infobox.items()])
    print "\n".join([key+": "+infobox[key] for key in infobox.keys()])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--train', dest='train', default='../data/jawiki-country.json', help='input training data')
    parser.add_argument('-c', '--country', dest='country', default='イギリス', help='input training data')
    args = parser.parse_args()
    my_country = knock020.get_country_text(args.train, args.country)
    info_dic = knock025.get_info(my_country)
    main(info_dic)