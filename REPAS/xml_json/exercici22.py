
import xml.etree.ElementTree as ET 

def funcionQueDevuelveXML():
    p =ET.Element('students')
    c=ET.SubElement(p,'Student', {"name":"sasha","surname":"jovanovic", "gmail": "2023_aleksandra.jovanovic@iticbcn.cat","dni":"XXXXX333" })
    tree = ET.ElementTree(p)
    tree.write("ejercicio22.xml")
    ET.dump(p)
    c=ET.SubElement(p,'Student', {"name":"victoria","surname":"sanchez", "gmail": "2023_victoria.sanchez@iticbcn.cat","dni":"XXXXXX1111" })
    tree = ET.ElementTree(p)
    tree.write("ejercicio22.xml")
    c=ET.SubElement(p,'Student', {"name":"daniel","surname":"Jimenez", "gmail": "danielJimenez@gmail.com","dni":"XXXXX123" })
    tree = ET.ElementTree(p)
    tree.write("ejercicio22.xml")
    c=ET.SubElement(p,'Student', {"name":"sonia","surname":"gutierrez", "gmail": "soniaG@gmail.com","dni":"XXX232323" })
    tree = ET.ElementTree(p)
    tree.write("ejercicio22.xml")
    c=ET.SubElement(p,'Student', {"name":"Jordi","surname":"Cruz", "gmail": "JordiCruz@gmail.com","dni":"235435353L" })
    tree = ET.ElementTree(p)
    tree.write("ejercicio22.xml")
    """ tree = ET.parse('ejercicio22.xml')
    root = tree.getroot()
    element = root[0]
    element.set('name','sasha')
    element.set('surname','jovanovic')
    element.set('gmail', '2023_aleksandra.jovanovic@iticbcn.cat')
    element.set('dni','XXXXX333')
    tree.write('ejercicio22.xml')

    element.set('name','victoria')
    element.set('surname','sanchez')
    element.set('gmail', '2023_victoria.sanchez@iticbcn.cat')
    element.set('dni','XXXXXX1111')
    tree.write('ejercicio22.xml')

    element.set('name','daniel')
    element.set('surname','Jimenez')
    element.set('gmail', 'danielJimenez@gmail.com')
    element.set('dni','XXXXX123')
    tree.write('ejercicio22.xml')
   
    element.set('name','sonia')
    element.set('surname','gutierrez')
    element.set('gmail', 'soniaG@gmail.com')
    element.set('dni','XXX232323')
    tree.write('ejercicio22.xml')
    
    element.set('name','Jordi')
    element.set('surname','Cruz')
    element.set('gmail', 'JordiCruz@gmail.com')
    element.set('dni','235435353L')
    tree.write('ejercicio22.xml')"""
    
    
    
    
    
    

    
funcionQueDevuelveXML()