import urllib.request
from xml.etree.ElementTree import XML
import sys
#import pdb;pdb.set_trace()
import logging

if len(sys.argv) != 3:
    raise SystemExit('Usage: nextbus.py route stopid')
route = sys.argv[1]
stopid = sys.argv[2]

url = 'http://ctabustracker.com/bustime/map/getStopPredictions.jsp?route={}&stop={}'.format(route,stopid)
data = urllib.request.urlopen(url)
doc = data.read()
#print(doc)
bus=XML(doc)
for pt in bus.findall('.//pt'):
    print(pt.text)
