# __auther__ == zhangqigao

from three_menus.module import provinceInfo


def province_show():
    #一级菜单字符串列表
    province_info_str_list = []
    #获取所有一级菜单信息
    all_province_list = provinceInfo.province_info()
    #获取一级菜单编号和一级菜单名称
    for province_tuple in all_province_list:
        province_id,province_name = province_tuple
        province_info_str = "|-{0}：{1}省".format(province_id,province_name)
        province_info_str_list.append(province_info_str)
    #获取到一级菜单的字符串
    all_province_info_str = '\n'.join(province_info_str_list)

    return all_province_info_str