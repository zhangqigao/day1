# __auther__ == zhangqigao

from three_menus.config.settings import tree_menu_list

#三级菜单信息
def county_info(province_name,city_name):
    county_name_temp_list = []
    all_county_name_list = []
    #获取一级菜单列表
    for tree_menu in tree_menu_list:
        if list(tree_menu.keys())[0] == province_name:
            break
    city_info_list = tree_menu[province_name]
    #获取二级菜单列表
    for city_info in city_info_list:
        if list(city_info.keys())[0] == city_name:
            county_name_list = city_info[city_name]
            break
    #获取三级菜单编号和菜单名，[(1,三级菜单名)]
    county_name_list_len = len(county_name_list)
    for i in range(county_name_list_len):
        str_i = str(i)
        county_name_temp_list.append(str_i)
        county_name_temp_list.append(county_name_list[i])
        county_name_temp_tuple = tuple(county_name_temp_list)
        all_county_name_list.append(county_name_temp_tuple)
        county_name_temp_list = []

    return all_county_name_list
