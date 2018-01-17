import os

# 配置文件的根目录
config_base_dir = os.path.dirname(os.path.abspath(__file__))

# 用户信息文件
user_info_path = os.path.join(config_base_dir,"user_info")

# 锁定用户信息的文件
lock_info_path = os.path.join(config_base_dir,"lock_info")