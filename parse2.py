# -*- coding: utf-8 -*-
from lxml import etree
import csv
import codecs
from io import open

def parseXML(xmlfile):
    
    with open(xmlfile, 'rb') as f:
        xml = f.read()
    
    root = etree.fromstring(xml)

    group_dict = {}
    items = []
    g = 0
    i = 0
    for group in root.getchildren():
        group_name = group.get('name')
        g += 1
        for item in group.getchildren():
            item_name = item.get('value')
            login = ""
            password = ""
            email = ""
            web = ""
            comment = ""
            group_dict = {}
            i += 1
            for field in item.getchildren():
                if field.get('name') == u'Логин':
                    login = field.text
                elif field.get('name') == u'Пароль':
                    password = field.text
                elif field.get('name') == 'E-mail':
                    email = field.text
                elif field.get('name') == u'Web':
                    web = field.text
                elif field.get('name') == u'Комментарий':
                    comment = field.text
            group_dict['group'] = 'IMPORT\\\\' + group_name.encode('utf8')
            group_dict['item_name'] = item_name.encode('utf8')
            group_dict['login'] = login.encode('utf8')
            group_dict['password'] = password.encode('utf8')
            group_dict['email'] = email.encode('utf8')
            group_dict['web'] = web.encode('utf8')
            group_dict['comment'] = comment.encode('utf8')
            items.append(group_dict)
    print(g,i)
    return items
                                                                                                                                                                                         
def writeCSV(data, fieldnames,  file_name):
    with open(file_name, 'wb') as f:
        writer = csv.DictWriter(f, delimiter=',', fieldnames=fieldnames, quoting=csv.QUOTE_ALL)
        writer.writeheader()
        for row in data:
            writer.writerow(row)


if __name__ == '__main__':
    fieldnames = ["group", "item_name", "login", "password", "email", "web", "comment"]
    writeCSV(parseXML('12.xml'), fieldnames, 'ps5.csv')
