##
## IDS566: For Homework 2
##

from lxml import etree, objectify


# Read the dictionary file.
Parser = objectify.makeparser(recover=True)
Tree = objectify.fromstring(''.join(open('dictionary.xml').readlines()), Parser)


# function: 
def getSenses(word, pos):
    global Tree
    item = Tree.xpath("//lexelt[@item='%s.%s']" % (word, pos))    
    senses = []
    for sense in item[0].getchildren():
        senses.append(dict(zip(sense.keys(), sense.values())))
    return senses


# function:
def getSense(word, pos, sense_id):
    global Tree
    sense = Tree.xpath("//lexelt[@item='%s.%s']/sense[@id='%d']" % (word, pos, sense_id))
    return dict(zip(sense[0].keys(), sense[0].values()))


# Example
print(getSense('begin', 'v', 2))
print(getSenses('begin', 'v'))



