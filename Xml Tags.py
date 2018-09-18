import xml.etree.ElementTree as ET
def xmlTags(xml):
    root = ET.fromstring(xml)
    stack = [root]
    processor = dict()
    while len(stack)!=0:
        parent = stack.pop()
        children = parent.getchildren()
        stack = stack + children[::-1]
        if parent.tag in processor.keys():
            processor[parent.tag] += [i.tag for i in children if i.tag not in processor[parent.tag]]
            processor[parent.tag+"_attr"].update(parent.attrib)
        else:
            temp = [i.tag for i in children]
            processor[parent.tag] = sorted(set(temp), key=temp.index)
            processor[parent.tag+"_attr"] = set(parent.attrib)
    
    stack=[root.tag]
    result = []
    count = 0
    
    while len(stack)!=0:
        parent = stack.pop()
        if parent == '-':
            count-=1
            continue
        stack+='-'
        stack+=(processor[parent])[::-1]
        result.append('--'* count + parent+'('+ ', '.join(sorted(processor[parent+"_attr"])) +')')
        count+=1
    return result
        
