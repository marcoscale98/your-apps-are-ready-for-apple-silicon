import functools
import operator

with open('programmi.txt','r') as fp:
    link = 'https://isapplesiliconready.com/it?apps='
    apps=fp.read().splitlines()
    apps_tradotte = map(lambda app: app.translate({ord(i): '%20' for i in app if i == ' '}), filter(lambda app: app!='',apps))
    apps_tradotte = functools.reduce(operator.add, map(lambda app: app+',',apps_tradotte))
    print(link+apps_tradotte[:-1])