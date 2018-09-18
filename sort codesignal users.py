def sortCodesignalUsers(codefighters):
    res = [CodeFighter(*codefighter) for codefighter in codefighters]
    res.sort(reverse=True)
    return map(str, res)

import functools
@functools.total_ordering
class CodeFighter:
    def __init__(self, *args):
        self.fighter_name = args[0]
        self.fighter_id = int(args[1])
        self.fighter_xp = int(args[2])
    def __lt__(self, other):
        if self.fighter_xp < other.fighter_xp:
            return self.fighter_xp < other.fighter_xp
        elif self.fighter_xp == other.fighter_xp:
            return self.fighter_id>other.fighter_id
        return False
    
    def __str__(self):
        return self.fighter_name
    

