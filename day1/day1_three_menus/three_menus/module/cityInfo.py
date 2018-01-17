# __auther__ == zhangqigao

from three_menus.config.settings import tree_menu_list

def city_info(province_name):
    city_name_list = []
    all_city_name_list = []
    city_name_temp = []
    #通过一级菜单，获取二级菜单
    for tree_menu in tree_menu_list:
        if list(tree_menu.keys())[0] == province_name:
            break
    city_info_dict = tree_menu[province_name]
    #获取二级菜单列表
    for city_name_dict in city_info_dict:
        city_name = list(city_name_dict.keys())[0]
        city_name_list.append(city_name)
    #获取二级菜单编号和菜单名
    city_name_list_len = len(city_name_list)
    for i in range(city_name_list_len):
        str_i = str(i)
        city_name_temp.append(str_i)
        city_name_temp.append(city_name_list[i])
        city_name_temp_tuple = tuple(city_name_temp)
        all_city_name_list.append(city_name_temp_tuple)
        city_name_temp = []


    return all_city_name_list


