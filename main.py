from xml.etree import ElementTree as ET
def recx(level, points=1):
  points+=1
  for c in level:
    dic[c.attrib['color']]+=points
    print (c.attrib, points)    
    recx(c,points)    
   
tree = ET.parse("tree.xml")
root = tree.getroot()   
dic = {"red": 0, "green": 0, "blue": 0}
dic[root.attrib['color']]+=1
recx(root)
print(dic)