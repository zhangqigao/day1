# __auther__ == zhangqigao

from user_login.config.settings import lock_info_path

# 获取锁定客户信息列表
def locker_info():
    #从锁定文件中获取锁定用户列表
    with open(lock_info_path,'r') as locker_info_file:
        all_locker_info = locker_info_file.read()
        locker_info_list = all_locker_info.split("\n")
    return locker_info_list