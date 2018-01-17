# __auther__ == zhangqigao
from three_menus.module.cityInfo import city_info


def city_show(province_id,province_name):
    city_info_str_list = []
    all_city_name = city_info(province_name)
    #通过一级菜单获取二级菜单的详细信息
    for city_name_tuple in all_city_name:
        city_id,city_name = city_name_tuple
        city_info_str = "|--{0}：{1}市".format(city_id,city_name)
        city_info_str_list.append(city_info_str)
    #一级菜单名
    province_info_str = "|-{0}：{1}省\n".format(province_id,province_name)
    #二级菜单名
    all_city_str = "\n".join(city_info_str_list)
    #总的菜单名
    all_city_info_str = province_info_str + all_city_str

    return all_city_info_str