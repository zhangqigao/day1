# __auther__ == zhangqigao

from three_menus.config.settings import tree_menu_list

#一级菜单信息
def province_info():
    province_name_list = []
    province_list = []
    all_province_tuple_list = []
    #获取一级菜单名
    for tree_menu in tree_menu_list:
        province_name_list.append(list(tree_menu.keys())[0])
    province_name_list_len = len(province_name_list)
    # 获取菜单编号和菜单名列表
    for i in range(province_name_list_len):
        str_i = str(i)
        province_list.append(str_i)
        province_list.append(province_name_list[i])
        province_tuple = tuple(province_list)
        province_list = []
        all_province_tuple_list.append(province_tuple)

    return all_province_tuple_list