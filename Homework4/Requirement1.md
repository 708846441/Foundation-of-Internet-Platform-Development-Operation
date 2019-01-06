# Requirement I
本次CI/CD环境搭建选择jenkins+github，实现了在每次git push之后，jenkins能够监测到这个push,进行CI/CD并构建docker镜像。

具体步骤如下：
- 搭建CI/CD环境
- 构建docker镜像
- 自动构建docker镜像

## 搭建CI/CD环境
CI/CD 环境搭建参考上学期CI/CD团队作业，这里不再赘述，仅展示搭建成果。

- 修改代码并push,jenkins检测,触发构建

 ![代码修改.png](https://i.loli.net/2019/01/06/5c31ee98010bd.png)

  ![push.png](https://i.loli.net/2019/01/06/5c31ee97f336f.png)

![jenkins检测到push.png](https://i.loli.net/2019/01/06/5c31ed09d540c.png)

- jenkins构建成功，执行构建后操作，拷贝jar包并部署bookstore项目
- ![jenkins构建成功，执行构建后操作，拷贝jar包并部署bookstore项目.png](https://i.loli.net/2019/01/06/5c31f12a7bc66.png)
- 部署成功
- ![部署成功.png](https://i.loli.net/2019/01/06/5c31ee3b39ce4.png)

## 构建docker镜像
### 在拷贝出的jar包目录下建立Dockerfile文件

- 文件内容：

```
FROM java:8
ADD bookstore.jar app.jar
RUN bash -c 'touch /app.jar'
ENTRYPOINT ["java","-jar","/app.jar"]
```

- 在该目录下制作镜像

![制作镜像.png](https://i.loli.net/2019/01/06/5c31f2c861e08.png)

- 关闭正在运行的项目，运行docker容器
- ![关闭正在运行的项目后，运行docker容器.png](https://i.loli.net/2019/01/06/5c31f3a392310.png)
- 运行成功，界面同部署成功时界面。

## 自动构建docker镜像

- 在jenkins的构建后操作中添加构建docker命令

![在jenkins的构建后操作中添加构建docker命令.png](https://i.loli.net/2019/01/06/5c31f5207a70e.png)

- 同CI/CD部分，修改代码并push,jenkins检测,触发构建
- jenkins构建成功，执行构建后操作，拷贝jar包并构建docker镜像
- ![jenkins构建成功，执行构建后操作，拷贝jar包并构建docker镜像.png](https://i.loli.net/2019/01/06/5c31f6cf338d6.png)
- 运行成功
- ![运行成功.png](https://i.loli.net/2019/01/06/5c31f74724990.png)