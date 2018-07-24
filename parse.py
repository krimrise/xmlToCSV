# -*- coding: utf-8 -*-
from lxml import etree
import codecs

def parseXML(xmlFile):
    
    with open(xmlFile) as fobj:
        xml = fobj.read()

    root = etree.fromstring(xml)
    
    test = ""
    gi = 0
    ii = 0
    for appt in root.getchildren():
#        print(appt.get('name'))
        group = appt.get('name')
        gi += 1
        for el in appt.getchildren():
            ii += 1
            name = el.get('value')
            em = ""
            web = ""
            comm = ""
            password = ""
            login = ""
            for elem in el.getchildren():
                if elem.get('name') == u'Логин':
                    login = elem.text
                elif elem.get('name') == u'Пароль':
                    password = elem.text
                elif elem.get('name') == 'E-mail':
                    em = elem.text
                elif elem.get('name') == u'Web':
                    web = elem.text
                elif elem.get('name') == u'Комментарий':
                    comm = elem.text
                    
            print('"IMPORT\\\\' + group + '","' + name + '","' + login + '","' + password + '","' + em + '","' + web + '","' + comm + '"')
            s = '"IMPORT\\\\' + group + '","' + name + '","' + login + '","' + password + '","' + em + '","' + web + '","' + comm + '"'
            with codecs.open('pa3.csv', 'a', encoding='utf-8') as f:
                f.write(s + "\n")
    print(gi)
    print(ii)

                                                       
if __name__ == "__main__":
    parseXML("12.xml")
