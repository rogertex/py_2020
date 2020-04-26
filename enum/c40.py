from enum import Enum
from enum import IntEnum


class VIP (Enum):
    YELLOW = 1
    GREEN = 2
    GREEN_ALIAS=2 #两个数字相同用别名
    BLACK = 3
    RED = 4
# VIP.YELLOW=6  枚举的值不能被更改.
print(VIP.YELLOW.value)
print(VIP.YELLOW.name)
print(VIP.YELLOW)
for v in VIP.__members__: #遍历枚举类型
    print(v)
    # print(v.name)
    # print(v.value)
print(VIP(1)) 



