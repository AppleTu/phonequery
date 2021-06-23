# encoding: utf-8
import time
import pandas as pd
import json
from phone import Phone

time1 = time.time()

province1 = []
phone_type1 = []
city1 = []
area_code1 = []
phone1 = []
zip_code1 = []

f1 = open(u'erro.txt', 'w+')

# 读入数据
df = pd.read_excel('Tel.xls')
mobile_1 = []
for i in range(0, len(df)):
    mobile = df.iloc[i, 0]
    p = Phone()
    result = p.find(mobile)
    result1 = json.dumps(result)
    result2 = json.loads(result1)
    # print(result2)
    if result2 is None:
        province = ''
        phone_type = ''
        city = ''
        area_code = ''
        phone = str(df.iloc[i, 0])
        zip_code = ''
    else:
        province = result2['province']
        phone_type = result2['phone_type']
        city = result2['city']
        area_code = result2['area_code']
        phone = result2['phone']
        zip_code = result2['zip_code']

    province1.append(province)
    phone_type1.append(phone_type)
    city1.append(city)
    area_code1.append(area_code)
    phone1.append(phone)
    zip_code1.append(zip_code)
    print(phone, province, city, phone_type, area_code, zip_code)


if __name__ == '__main__':
    data = pd.DataFrame(
        {"mobile": phone1, "province": province1, "city": city1, "area_code": area_code1, "zip_code": zip_code1,
         "phone_type": phone_type1})
    # print(len(data))
    # 写出excel
    writer = pd.ExcelWriter(r'hhaha.xlsx', engine='xlsxwriter', options={'strings_to_urls': False})
    data.to_excel(writer, index=False)
    writer.close()
    time2 = time.time()
    print(u'ok,爬虫结束!')
    print(u'总共耗时：' + str(time2 - time1) + 's')
