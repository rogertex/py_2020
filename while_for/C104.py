'''
@Author: Roger
@Date: 2020-05-05 15:49:39
@LastEditors: Roger
@LastEditTime: 2020-05-05 18:22:46
@Email: qunlin.gu@163.com
@Description: if else 语句
'''

ACCOUNT = 'peter'
PASSWORD = '123'
# 常量用全部大写.L
class Login_test():
    def tst(self):
        print('please input user ACCOUNT')
        user_ACCOUNT = input()
        print('please input PASSWORD')
        user_PASSWORD = input()


        if ACCOUNT == user_ACCOUNT and PASSWORD == user_PASSWORD:
            print('sucess')
        else:
            print('failed')
if __name__ == "__main__":
    tst = Login_test()
    tst.tst()
    