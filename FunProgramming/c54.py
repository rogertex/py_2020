origin =0

def factory(pos):
    def go(step):
        nonlocal pos #强制把pos设置为环境变量, 环境变量记忆了上次的值.
        new_pos=pos+step
        pos = new_pos
        return new_pos
    return go    
tourist = factory(origin)   

print(tourist(2))
print(tourist(3))
print(tourist(5))
