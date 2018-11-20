# Homework 3A : Design an experiment to measure the metrics of your computer's storage and network

## 1. 存储

- 工具：`WinSat`
- 测试环境：
    - C盘：128GB的SSD, LITEON CV3-8D128
    - D盘：1TB的HDD, WDC WD18SPCX-24HWST1

### 1.1. 操作步骤

1. 以管理员身份运行命令行程序，`win+R->输入cmd并回车`。

![cmd](https://i.loli.net/2018/11/20/5bf365a0301f3.png)

2. 输入命令`winsat disk`并回车，此时为默认扫描系统盘，一般也就是C盘。

![ssd](https://i.loli.net/2018/11/20/5bf3670984a1a.png)

3. 输入`winsat disk` + 参数`-drive 盘符`，就是扫描指定盘了。

例如扫描D盘：`winsat disk -drive d`

![hdd](https://i.loli.net/2018/11/20/5bf367b9747c1.png)

### 1.2. 结果分析

SSD的读写在300M/s左右。而HHD不及SSD的三分之一，尤其在随机读上连SSD的零头都不如。在读写速度上，SSD相较于HDD有显著提升。当然容量和价格是HDD的优势。

## 2. 网络

- 工具：`ping`
- 测试环境：
    - SJTU校内无线网络
    - 上海联通4G热点
    - 寝室无线网络
    - 寝室有线连接

### 2.1. 操作步骤

1. 连接SJTU校内无线网络，运行命令行程序，`win+R->输入cmd并回车`。

![cmd](https://i.loli.net/2018/11/20/5bf365a0301f3.png)

2. 输入命令`ping www.baidu.com`并回车，查看访问百度具体的延迟时间。

![SJTU](https://i.loli.net/2018/11/20/5bf370c58a61e.png)

3. 依次切换为上海联通4G热点、寝室无线网络、寝室有线连接并重复`步骤2`。

上海联通4G热点：

![上海联通4G热点](https://i.loli.net/2018/11/20/5bf370c58c26a.png)

寝室无线网络：

![寝室无线网络](https://i.loli.net/2018/11/20/5bf393d8ecf64.png)

寝室有线连接：

![寝室有线连接](https://i.loli.net/2018/11/20/5bf3959b5cd41.png)

### 1.2. 结果分析

寝室有线连接的延迟时间在27ms左右。而寝室无线网络的延迟时间达到了420ms，是有线连接的十几倍。在网络速度上，有线连接相较于无线连接有显著提升。另外，有线连接更为稳定。当然便捷性和成本是无线连接的优势。