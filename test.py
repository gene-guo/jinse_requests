"""
用来做 json数据的常规出流程
"""

# 1. 导入模块
import requests
import json

# 目标地址  （直接获取数据）
url = 'http://api.help.bj.cn/apis/life27/?id=长春'

# 发送get请求
response = requests.get(url)  # 得到的是response对象

# 使用response对象中的属性 获取响应内容，类型：字符串
result = response.text
# 使用json模块将 str类型 ==> Python中的字典类型
result_dict = json.loads(result)

# 获取时间
time = result_dict['update']
print(time)
# 获取空气质量
info = result_dict['data']['zs_kqwr']
info_name = info['name']
print(info_name)
info_level = info['level']
print(info_level)
info_type = info['type']
print(info_type)
info_info = info['info']
print(info_info)
"""
json中两个比较重要的方法

json  str    ===>     dict
从Python外部  转换     Python内部的数据类型
            放入、加载到
            json.loads()  

dict         ==>      json str
Python内部的数据类型     从Python外部
            降级、抛出的过程
            json.dumps()             
"""