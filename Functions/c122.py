# R skill1 Skill2

def damage(skill1,skill2):
        damage1=skill1*2
        damage2=skill2*2+10
        return damage1,damage2

skill1_damage,skill2_damage=damage(3,6)# 用有意义的变量名来接受函数的返回值.
#序列解包
# print(type(damages))
print(skill1_damage,skill2_damage)