# __auther__ == zhangqigao

from user_login.config.settings import user_info_path
#获取用户信息函数
def user_info():
    user_info_dict = {}
    flag = False
    #从用户信息文件中获取用户的用户名和密码
    with open(user_info_path,"r") as user_info_file:
        all_user_info = user_info_file.read()
        user_info_list = all_user_info.split('\n')
        for user in user_info_list:
             username,password = user.split(" ")
             user_info_dict[username] = password
        else:
            flag = True

    return flag,user_info_dict