import xml.etree.ElementTree as ET
import urllib.request

# XML 데이터 가져오기
r = urllib.request.urlopen('http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=1120067000')
xml_data = r.read().decode('utf-8')

# Parsing
root = ET.fromstring(xml_data)
print(root.find('channel').find('item').find('description').find('body').find('data').find('wfKor').text)

