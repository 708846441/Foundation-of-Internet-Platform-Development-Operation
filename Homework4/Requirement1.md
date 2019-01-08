# Requirement I
本次CI/CD环境搭建选择jenkins+github，实现了在每次git push之后，jenkins能够监测到这个push,进行CI/CD并构建docker镜像。

具体步骤如下：
- 搭建CI/CD环境
- 构建docker镜像
- 自动构建docker镜像

## 搭建CI/CD环境
CI/CD 环境搭建参考上学期CI/CD团队作业，这里稍作描述，并展示搭建成果。

- 步骤一：在Jenkins中安装Maven插件，并新建一个Maven项目。Jenkins会利用pom文件，从而大大减轻构建配置。
  ![在Jenkins中安装Maven插件，并新建一个Maven项目。Jenkins会利用pom文件，从而大大减轻构建配置.png](https://i.loli.net/2019/01/08/5c34b8ffa7602.png)
- 步骤二：在配置页中，源码管理选择Git，填入地址。默认使用master分支。如果需要口令，在Credentials中添加用户名/口令，或者使用SSH Key 
  ![在配置页中，源码管理选择Git，填入地址。默认使用master分支。如果需要口令，在Credentials中添加用户名口令，或者使用SSH Key.png](https://i.loli.net/2019/01/08/5c34b8ffa75f4.png)
- 步骤三：配置构建触发器，定时检查版本库，发现有新的提交就触发构建。这种方式对git、SVN等所有版本管理系统都是通用的。 
  ![配置构建触发器，定时检查版本库，发现有新的提交就触发构建。这种方式对git、SVN等所有版本管理系统都是通用的。 .png](https://i.loli.net/2019/01/08/5c34b8ff851af.png)
- 步骤四：配置构建选项，本项目直接使用maven的pom.xml进行构建，需要配置好pom.xml文件路径以及配置参数，这里的参数是跳过test选项。在pom.xml里的build标签添加<defaultGoal> 标签，值为package阶段，这样build结束后才会生成可运行jar文件，或者直接在配置选项中写好构建命令。
  ![配置构建选项，本项目直接使用maven的pom.xml进行构建，需要配置好pom.xml文件路径以及配置参数，这里的参数是跳过test选项。在pom.xml里的build标签添加defaultGoal 标签，值为package阶段，这样build结束后才会生成可运行jar文件，或者直接在配置选项中写好构建命令.png](https://i.loli.net/2019/01/08/5c34b8ff94e40.png)
- 步骤五：github配置webhook，每当master分支发生变动，merge pull request 或有新的commit，就会将信息push到jenkins平台上，并自动构建。

### 搭建成果

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