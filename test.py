#需求：对于一个有10万条数据的excel文件，将所有第7列数据有重复现象的行都抽取出来，写入另一个excel文件。(最多有两行数据的第七列重复)

import pandas as pd
def duplicate_filter():
    # 读取新文件
    read_n = pd.read_excel('dingzhou.xls', sheet_name = '删除废数据') #读取数据
    id_list = []       #记录遍历过的对象的第7列数据
    id_repeat_list = []     # 重复数据的个数
    datas = [] #筛选出的重复数据
    row_list =[] #存储遍历过的对象数据
    single_id_list = []# 存储遍历过的不重复数据
    rows = read_n.iterrows() #获得生成器
    for index, row in rows: #row是pandas.series数据类型
        id_list.append(str(row.iloc[6])) #将当前遍历对象的第7列数据存入list
        row_list.append(row) #将
        if str(row.iloc[6]) not in single_id_list: #是否是第一次出现
            single_id_list.append(str(row.iloc[6])) 
        else:
            datas.append(row) #将第7列数据和之前重复的对象写入datas
            firstindex  = id_list.index(str(row.iloc[6]))#获取第一次出现这个重复值的index
            # duplicate_index = [i for i,x in enumerate(id_list) if x == str(row.iloc[6])] #获取之前所有等于当前行第7列数据的行的索引（包括当前行）
            # print("duplicate_index",duplicate_index)
            # for i in duplicate_index:
            #     datas.append(row_list[i])
            id_repeat_list.append(str(row.iloc[6]))
    print('id_list = ', len(id_list))
    print('id_repeat_list = ', len(id_repeat_list))
    # 保存重复的数据到xls文件
    df = pd.DataFrame(datas)
    df.to_excel('right_new_new.xls', index=False, encoding='utf_8_sig')
#duplicate_filter()
read_n = pd.DataFrame(["1","11","111","1111","111","11","1"])
read_n = pd.DataFrame([1,11,111,1111,111,11,1,1])
id_list = []
rows = read_n.iterrows() #获得生成器 
for index, row in rows:
    id_list.append(row[0]) #将当前遍历对象的第7列数据存入list
    print(type(row[0]))
    duplicate_index = [i for i,x in enumerate(id_list) if x == row[0]] #获取之前所有等于当前行第7列数据的行的索引（包括当前行）
    print("duplicate_index",duplicate_index)
