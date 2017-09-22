
爬虫IP代理池
=======
[![Build Status](https://travis-ci.org/jhao104/proxy_pool.svg?branch=master)](https://travis-ci.org/jhao104/proxy_pool)
[![](https://img.shields.io/badge/Powered%20by-@j_hao104-green.svg)](http://www.spiderpy.cn/blog/)
[![Requirements Status](https://requires.io/github/jhao104/proxy_pool/requirements.svg?branch=master)](https://requires.io/github/jhao104/proxy_pool/requirements/?branch=master)
[![Packagist](https://img.shields.io/packagist/l/doctrine/orm.svg)](https://github.com/jhao104/proxy_pool/blob/master/LICENSE)
[![GitHub contributors](https://img.shields.io/github/contributors/jhao104/proxy_pool.svg)](https://github.com/jhao104/proxy_pool/graphs/contributors)
[![](https://img.shields.io/badge/language-Python-green.svg)](https://github.com/jhao104/proxy_pool)

##### [介绍文档](https://github.com/jhao104/proxy_pool/blob/master/doc/introduce.md)

* 支持版本 ![](https://img.shields.io/badge/Python-2.x-green.svg) ![](https://img.shields.io/badge/Python-3.x-blue.svg)

* 测试地址: http://123.207.35.36:5010 单机勿压测。谢谢

### 下载安装

* 下载源码:

```shell
git clone git@github.com:jhao104/proxy_pool.git

或者直接到https://github.com/jhao104/proxy_pool 下载zip文件
```

* 安装依赖:

```shell
pip install -r requirements.txt
```

* 配置Config.ini:

```shell
# Config.ini 为项目配置文件
# 配置DB
type = SSDB       # 如果使用SSDB或redis数据库，均配置为SSDB
host = localhost  # db host
port = 8888       # db port
name = proxy      # 默认配置

# 配置 ProxyGetter
freeProxyFirst  = 1  # 这里是启动的抓取函数，可在ProxyGetter/getFreeProxy.py 扩展
freeProxySecond = 1
....

# 配置 HOST (api服务)
ip = 127.0.0.1       # 监听ip,0.0.0.0开启外网访问
port = 5010          # 监听端口
# 上面配置启动后，代理api地址为 http://127.0.0.1:5010

```

* 启动:

```shell
# 如果你的依赖已经安全完成并且具备运行条件,可以直接在Run下运行main.py
# 到Run目录下:
>>>python main.py

# 如果运行成功你应该看到有4个main.py进程

# 你也可以分别运行他们,
# 依次到Api下启动ProxyApi.py,Schedule下启动ProxyRefreshSchedule.py和ProxyValidSchedule.py即可.
```

### 使用

启动过几分钟后就能看到抓取到的代理IP，你可以直接到数据库中查看，推荐一个[SSDB可视化工具](https://github.com/jhao104/SSDBAdmin)。

也可以通过api访问http://127.0.0.1:5010 查看。

* Api

| api | method | Description | arg|
| ----| ---- | ---- | ----|
| / | GET | api介绍 | None |
| /get | GET | 随机获取一个代理 | None|
| /get_all | GET | 获取所有代理 |None|
| /get_status | GET | 查看代理数量 |None|
| /delete | GET | 删除代理  |proxy=host:ip|

* 爬虫使用

如果要在爬虫代码中使用的话， 可以将此api封装成函数直接使用，例如：

```python
import requests

def get_proxy():
    return requests.get("http://127.0.0.1:5010/get/").content

def delete_proxy(proxy):
    requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

# your spider code

def getHtml():
    # ....
    retry_count = 5
    proxy = get_proxy()
    while retry_count > 0:
        try:
            html = requests.get('https://www.example.com', proxies={"http": "http://{}".format(proxy)})
            # 使用代理访问
            return html
        except Exception:
            retry_count -= 1
    # 出错5次, 删除代理池中代理
    delete_proxy(proxy)
    return None
```

### 问题反馈

任何问题欢迎在[Issues](https://github.com/jhao104/proxy_pool/issues) 中反馈，如果没有账号可以去 我的[博客](http://www.spiderpy.cn/blog/message)中留言。

你的反馈会让此项目变得更加完美。

### 贡献代码

本项目仅作为基本的通用的代理池架构，不接收特有功能(当然,不限于特别好的idea)。

本项目依然不够完善，如果发现bug或有新的功能添加，请在[Issues](https://github.com/jhao104/proxy_pool/issues)中提交bug(或新功能)描述，在确认后提交你的代码。

这里感谢以下contributor的无私奉献：

　　[@kangnwh](https://github.com/kangnwh)| [@bobobo80](https://github.com/bobobo80)| [@halleywj](https://github.com/halleywj)| [@newlyedward](https://github.com/newlyedward)| [@wang-ye](https://github.com/wang-ye)| [@gladmo](https://github.com/gladmo)| [@bernieyangmh](https://github.com/bernieyangmh)| [@PythonYXY](https://github.com/PythonYXY)| [@zuijiawoniu](https://github.com/zuijiawoniu)




