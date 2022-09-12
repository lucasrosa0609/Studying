# XML Schema
# Desciprtion of the legal format of an XML document.
# Expressed in terms of constraints on the structure and content of documents.
# often used to specify a "contract" between systems -
# " My system will only accept XML that conforms to this particular Schema."

# XML Document        ->
# Schema contract     ->         XML VALIDATION

# many XML Schema Languages
# document type definition (DTD)
# standard generalized markup language
# XML SCHEMA FROM W3C

# XSD XML Schema
# we will focus on the world wide web consortium version. it is often called
# "w3c schema" because "schema" is considered generic. more commonly it is
# called XSD because the file names end in .xsd

# XSD Structude
# xs: element
# xs: sequence
# xs:complexType

# <person>
#   <lastname>Severance</lastname>
#   <age>17</age>
#   <dateborn>2001-04-17</dateborn>
# </person>

#  <xs:element name="person">
#   <xs:complexType>
#     <xs:sequence>
#       <xs:element name="full_name" type="xs:string"
#         minOccurs="1" maxOccurs="1"/>
#       <xs:element name="chidl_name" type="xs:string"
#         minOccurs="1" maxOccurs="10"/>
#     </xs:sequence>
#   </xs:complexType>
# <xs:element>

# <person>
#   <full_name>Tove Refsnes</full_name>
#   <child_name>Hege</child_name>
#   <child_name>Stale</child_name>
#   <child_name>Jim</child_name>
#   <child_name>Borge</child_name>
# </person>

# ISO 8601 Date/Time Format
# 2002-05-30T09:30:10Z
# year-month-day/time-of-day/timezone - typically specified in UTC/GMT rather
# than local time zone

import xml.etree.ElementTree as ETree

data = '''
<person>
<name>Chuck</name>
<phone type="intl">
    +1 734 303 4456
    </phone>
    <email hide="yes">
</person>
'''

tree = ETree.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
