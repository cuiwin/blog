#### 临时获取root权限

重置root密码

```
sudo passwd root
```

切换至root

```
su root
```

#### 网络配置生效

```
cui@ubuntu1804:~$ sudo netplan apply
```

####　修改网卡名称为标准的eth0

```
root@ubuntu: vim /etc/default/grub
GRUB_CMDLINE_LINUX="net.ifnames=0 biosdevname=0"
root@ubuntu: update-grub
root@ubuntu: reboot
```

#### 常用安装命令-docker环境

```
# apt purge ufw lxd lxd-client lxcfs lxc-common
# apt install iproute2 ntpdate tcpdump telnet traceroute nfs-kernel-server nfs-
common lrzsz tree openssl libssl-dev libpcre3 libpcre3-dev zlib1g-dev ntpdate
tcpdump telnet traceroute gcc openssh-server lrzsz tree openssl libssl-dev libpcre3
libpcre3-dev zlib1g-dev ntpdate tcpdump telnet traceroute iotop unzip zip
```

#### apt命令

```
# apt list #列出已经安装的软件包
# apt install apache2 #安装软件包
# apt remove apache2 #卸载软件包但是保留配置文件
# apt purge apache2 #卸载软件包删除配置文件
# apt update #更新本地软件包列表索引，修改了apt仓库后必须执行
# apt upgrade #升级所有已安装且可升级到新版本的软件包
# apt-cache madison nginx #查看仓库中软件包有哪些版本可以安装
# apt install nginx=1.14.0-0ubuntu1.6 #安装软件包的时候指定安装具体的版本
```

### 更改apt源为国内阿里

```
https://opsx.alibaba.com/mirror

选择ubuntu,点击帮助，按照说明安装

apt update #更新本地软件包列表索引，修改了apt仓库后必须执行
```















