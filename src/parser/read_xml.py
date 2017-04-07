from collections import defaultdict
from lxml import etree


authors = defaultdict(set)

for event, element in etree.iterparse('dblp.xml', load_dtd=True, dtd_validation=True):
    # print all children
    if element.tag == 'dblp':
        continue
    if element.tag == 'mastersthesis':
        #print(element.get('key'))
        for a_auth1 in element.findall('author'):
            for a_auth2 in element.findall('author'):
                authors[a_auth1.text].add(a_auth2.text)
        element.clear()
        continue
    if element.tag == 'author':
        continue
    #print("cleared", element.tag)

    element.clear()


print(len(authors))
