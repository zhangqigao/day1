# __auther__ == zhangqigao

from three_menus.module.provinceInfo import province_info
from three_menus.plugin.provinceShow import province_show
from three_menus.module.cityInfo import city_info
from three_menus.plugin.cityShow import city_show
from three_menus.plugin.countyShow import county_show
import  os,sys
#设置执行路劲
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)

if __name__ == "__main__":
    while True:
        #显示所有省份
        show_province_name = province_show()
        print("\033[33m省：\033[0m\n{0}".format(show_province_name))
        #通过省Id显示市
        province_id = input("\033[32m省id：\033[0m".strip())
        if province_id == "q":
            exit("您已退出。。")
        all_province_tuple_list = province_info()
        all_province_dict = dict(all_province_tuple_list)
        if province_id not in list(all_province_dict.keys()):
            print("\033[31m省id不存在\033[0m")
            continue
        province_name = all_province_dict[province_id]
        show_city_name = city_show(province_id,province_name)
        while True:
            print("\033[31m市：\033[0m\n{0}".format(show_city_name))
            #通过市id显示县
            city_id = input("\033[34m市id：\033[0m".strip())
            if city_id == "b":
                print("返回省")
                break
            elif city_id == "q":
                exit("\033[32m您已退出。。\033[0m")
            else:
                all_city_name_list = city_info(province_name)
                all_city_name_dict = dict(all_city_name_list)
                if city_id not in list(all_city_name_dict.keys()):
                    print("\033[31m市id不存在\033[0m")
                    continue
                city_name = all_city_name_dict[city_id]
                show_county = county_show(province_id,province_name,city_id,city_name)
            while True:
                print("\033[31m县：\033[0m\n{0}".format(show_county))
                #设置结束符
                end = input("\033[34m返回(b)or退出(q)？:\033[0m")
                if end == "b":
                    print("返回市")
                    break
                elif end == "q":
                    exit("您已退出。。")
                else:
                    print("\033[31m输入错误，b(返回)、q(退出)字符\033[0m")