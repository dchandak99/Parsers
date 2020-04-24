import xml.etree.ElementTree as ET

tree = ET.parse('sample.tei.xml')
root = tree.getroot()

list(root[0])

list(root[0][2])

list(root[0][2][0][0])

root[0][2][0][0][0].text #abstract

list(root[1][0])

list(root[1][0][0])

for i in list(root[1][0][0]):
    print(i.text)


