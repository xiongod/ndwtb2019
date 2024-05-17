import uuid
import requests
from bs4 import BeautifulSoup
from xUtils import download_video,toMp3,mp4Time
import re
from Mp3Data import Mp3Data,CustomEncoder
import os
import json

# 获取所有的原始视频
# 打开文件，假设文件名为 'example.txt'
with open('wtb.html', 'r', encoding='utf-8') as file:
    # 读取文件内容
    content = file.read()

    soup = BeautifulSoup(content, 'lxml')
    eas = soup.find_all('a')
    # 解析图片
    index = 0
    data_list = []
    for a in eas:
        try:
            # 获取图片的src地址
            ariaLabel = a['aria-label']
            href = a['href']
            if "5年前" in ariaLabel:
                mp3_data = Mp3Data()
                title = re.sub(r"\s+", "", a.text)
                # print(ariaLabel)
                # print(href)
                # print(title)

                # 下载
                print("下载")
                mp4Name = download_video(href, './')
                # 获取时长
                print("获取时长")
                durationStr = mp4Time(mp4Name)
                # 转mp3 删除视频
                print("删除视频")
                mp3Name = toMp3(mp4Name)
                # 数据集成json
                print("数据集成json")
                mp3_data.title = title
                mp3_data.url = "https://xiongod.github.io/ndwtb2019/" + mp3Name
                mp3_data.duration = durationStr

                index += 1
        except Exception as e:
            continue
    print("将对象转成js")
    json_data = json.dumps(mp3_data, cls=CustomEncoder, indent=4, ensure_ascii=False)
    print("打印js")
    print(json_data)
    print("写入js")
    os.makedirs("./js")
    with open('./js/script.js', 'w', encoding='utf-8') as file:
        # 写入JavaScript代码
        file.write("123")
print(index)
