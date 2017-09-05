---
layout:     post
title:      CentOS7安装docker
subtitle:   CentOS7安装docker
date:       2017-9-4
author:     BY
header-img: img/post-bg-ios9-web.jpg
catalog: true
tags:
    - centos7
    - docker
---
第一步，下载docker安装包
https://download.docker.com/linux/centos/7/x86_64/stable/Packages/
第二步，安装
    $ sudo yum install /path/to/package.rpm
第三步，启动
    $ sudo systemctl start docker
第三步，验证
    $ sudo docker run hello-world
更新
    yum -y upgrade
    yum -y install

卸载
    $ sudo yum remove docker-ce
    $ sudo rm -rf /var/lib/docker

