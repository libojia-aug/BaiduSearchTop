一个百度风云榜爬虫

抓取实时热点、热度、对应百度搜索的快照

## Geting Started

##### 环境

```
python:3.7.3
```

##### 模块

```
requests==2.23.0
bs4==0.0.1
schedule==1.0.0
retrying==1.3.3
```

##### 模块安装与管理工具

```shell
pip3 install --upgrade pip -i https://pypi.douban.com/simple
pip3 install -r ./requirements.txt -i https://pypi.douban.com/simple
```

##### 运行

```shell
python3 main.py
```

##### 控制台输出

```
Begin at 2021-04-15 10:39:33
Get 30 topics
topics list: 境外反华势力拉拢内地学生内幕|日本宣布下架放射性氚吉祥物|美国将于5月1日前开始从阿富汗撤军|韩国生育率连续两年全球最低|多地渔民捞到境外间谍装置|生物安全法今起实施|张小斐给贾玲妈妈扫墓|央视起底反中乱港分子的幕后金主|江歌母亲起诉刘鑫案开庭|女网红遭CEO男友65页长文控诉|谭警官回应现实版的活着|李宁公司回应“天价鞋”|欧冠半决赛对阵出炉|央视曝光山寨叶圣陶杯比赛|贾跃亭回应终身禁入证券市场|华尔街金融巨骗麦道夫在狱中去世|岳云鹏带全家坐游艇|八旬大爷相亲想找年轻女性|吉野家一年净亏75亿日元|大雄静香要结婚了|任豪发文回应言论争议|孩子爬上抚顺地标建筑当滑梯|王子文认爱吴永恩后被偶遇|妇联回应女子5年4次起诉离婚被驳|成都一养老项目爆雷套住7亿资金|美国禁止日本食品进入|动物园回应狼圈养哈士奇|徐睿知被曝日常行为恶劣|外交部:太平洋不是日本的下水道|中国足额缴纳2021年联合国会费
End at 2021-04-15 10:45:06
Use 333.1485261917114 seconds
```

##### 输出文件结构

```
|-- data
    |-- 2021
        |-- 04-15
            |-- 10
            |-- 12
            ...
        |-- 04-16
            |-- 10
            ...
        ...
    |-- 2022
    ...
```

##### 文件名

```
{热度}_{话题名}
```

##### 数据结构

```
{
    "timeline": [
    {
        "time": "...",
        "title": "..."
    }],
    "video": [
    {
        "title": "..."
    }],
    "info": [
    {
        "title": "...",
        "desc": "..."
    }]
}
```

##### 截图

<img src="https://github.com/libojia-aug/BaiduSearchTop/blob/main/pics/filestree.jpeg" width = "200"  alt="" align=center />
<img src="https://github.com/libojia-aug/BaiduSearchTop/blob/main/pics/data.jpeg" width = "200"  alt="" align=center />

## Docker

##### 编译

```shell
make image
```

##### 运行

```shell l
docker run -v /BaiduSearchTop/data:/code/data baidu-search-top
```

## 定时任务

```python
if __name__ == '__main__':
    schedule.every(2).hour.do(main)
    while True:
        schedule.run_pending()
        time.sleep(1)
```

