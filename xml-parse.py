from urllib.request import urlopen
from xml.etree.ElementTree import parse

# Download the RSS feed and parse it
u = urlopen('https://www.w3schools.com/xml/note.xml')
doc = parse(u)

# Extract and output tags of interest
for item in doc.iterfind('./note'):
    to = item.findtext('to')
    fr = item.findtext('from')
    heading = item.findtext('heading')

    print(to)
    print(fr)
    print(heading)
    print()
