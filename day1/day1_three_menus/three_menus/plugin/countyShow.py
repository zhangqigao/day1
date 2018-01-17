# __auther__ == zhangqigao

from three_menus.module.countyInfo import county_info

#显示三级菜单
def county_show(province_id,province_name,city_id,city_name):
    #存放三级菜单字符串列表
    county_name_str_list = []
    all_county_name_list = county_info(province_name,city_name)
    #通过二级菜单获取三级菜单
    for all_county_name in all_county_name_list:
        county_id,county_name = all_county_name
        county_name_str = "|---{0}：{1}县".format(county_id,county_name)
        county_name_str_list.append(county_name_str)
    #一级菜单名称
    province_name_str = "|-{0}：{1}省\n".format(province_id,province_name)
    #二级菜单名称
    city_name_str = "|--{0}：{1}市\n".format(city_id,city_name)
    #三级菜单名称
    all_county_name_str = "\n".join(county_name_str_list)
    #总的菜单名称
    total_county_name_str = province_name_str + city_name_str + all_county_name_str

    return total_county_name_str