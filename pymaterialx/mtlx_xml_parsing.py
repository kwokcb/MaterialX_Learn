# %%
import MaterialX as mx
import xml.etree.ElementTree as ET

def is_well_formed_xml(xml_string):
    try:
        ET.fromstring(xml_string)  
        print("- XML : is well-formed.")
    except ET.ParseError as e:
        print("- XML :", e)    
    print(xml_string)
    print('\n')

print("*"*40)
test_string = '<?xml version="1.0"?><materialx version="1.39"><implementation name="IM_logical_and_genglsl" nodedef="ND_logical_and" target="genglsl" sourcecode="{{in1}} && {{in2}}"/></materialx>'

doc = mx.createDocument()
mx.readFromXmlString(doc, test_string)
is_well_formed_xml(test_string)
impl = doc.getImplementation("IM_logical_and_genglsl")
print('- Source code: :', impl.getAttribute("sourcecode"))
out_string = mx.writeToXmlString(doc)
is_well_formed_xml(out_string)

print("*"*40)

test_string = '<?xml version="1.0"?><materialx version="1.39"><implementation name="IM_logical_and_genglsl" nodedef="ND_logical_and" target="genglsl" sourcecode="{{in1}} && < {{in2}}"/></materialx>'
doc = mx.createDocument()
mx.readFromXmlString(doc, test_string)
print('- Source code: :', impl.getAttribute("sourcecode"))
out_string = mx.writeToXmlString(doc)
is_well_formed_xml(out_string)




