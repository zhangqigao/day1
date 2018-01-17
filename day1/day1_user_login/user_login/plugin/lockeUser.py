# __auther__ == zhangqigao

from user_login.config.settings import lock_info_path

#锁定动作
def lock_user(username):
    #将锁定用户信息输入到锁定文件中
    with open(lock_info_path,'a') as lock_file:
        lock_file.write(username+'\n')