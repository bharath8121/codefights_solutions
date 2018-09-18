import json
from collections import OrderedDict
def buildCommand(j):
    t = json.loads(j, object_pairs_hook = OrderedDict)
    stack = [t]
    while len(stack)>0:
        temp = stack.pop()
        for i in temp.keys():
            if type(temp[i]) is OrderedDict:
                stack.append(temp[i])
            else:
                if type(temp[i]) is float:
                    temp[i] = 0
                temp[i] *= 0
    
    return json.dumps(t)
