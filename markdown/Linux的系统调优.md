进程调度：

​    OS:  硬件抽象，虚拟计算机

​             system  call

   CPU:  time slice  

​               优先级：

​                调度器：

​				O(1)

进程优先级    ：  动态优先级      静态优先级



2颗CPU，共8核心，运行Nginx，优化：

2个处理内核，处理终端

6个亲缘性绑定，绑定Nginx的进程。

DMA:

CPU与外部IO设备的方式。



```
CPU:调优
	cpu affinity
	优先级调整
		cgroups,
内存：
	overcommit_memory
	msg
	shm
	swapiness
	nr_hugepages
	
Disk IO:
	设定 io scheduler
	
文件系统：
	挂载选择
	nobarrier,noatime
	
Network IO:
    nginx 调优
    
那个进程对网络接口带宽占用大
iftop

lsof 
```





































​            