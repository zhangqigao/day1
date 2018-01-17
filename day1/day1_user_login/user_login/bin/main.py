# __auther__ == zhangqigao

import os,sys
from user_login.module import userInfo,lockerInfo
from user_login.plugin import lockeUser

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

if __name__ == "__main__":
    #获取用户信息
    flag,user_info_dict = userInfo.user_info()
    if flag:
        print("\033[32m成功获取用户信息\033[0m")
    else:
        exit("\033[33m获取用户信息,已退出\033[0m")
    username = list(user_info_dict.keys())
    locker_info_list = lockerInfo.locker_info()
    count = 0
    while flag:
        user_name = input("用户名：").strip()
        #判断用户是否已经锁定
        if user_name not in locker_info_list:
            if user_name in username:
                while True:
                    pass_word = input("密码：").strip()
                    #提示密码是否正确
                    if pass_word == user_info_dict[user_name]:
                        exit("{username},欢迎登录".format(username=user_name))
                    else:
                        print("\033[31m{username}，密码错误,重新输入\033[0m".format(username=user_name))
                        continue
            #不存在用户输错三次，锁定该用户
            else:
                count += 1
                if count == 3:
                    lockeUser.lock_user(user_name)
                    print("\033[31m{username},输错三次已被锁定\033[0m".format(username=user_name))
                    flag = False
                else:
                    print("\033[31m{username}用户名输入错误,请重新输入\033[0m".format(username=user_name))
                    continue
        else:
            print("\033[33m{username}用户已被锁定，请重新输入\033[0m".format(username=user_name))
            continue