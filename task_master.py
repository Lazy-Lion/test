# task_master.py

# windows 查看端口占用进程： 
# netstat -ano
# netstat -ano|findstr "PID number"
# tasklist|findstr "PID number"

import random,time,queue
from multiprocessing.managers import BaseManager

task_queue = queue.Queue()  # 发送任务的队列
result_queue = queue.Queue() # 接收结果的队列

class QueueManager(BaseManager): # 继承BaseManager
	pass

def return_task_queue():
	return task_queue

def return_result_queue():
	return result_queue


if __name__ == '__main__':
	# 把两个队列注册到网络上
#	QueueManager.register('get_task_queue', callable=lambda : task_queue)  # pickle序列化不支持匿名函数
#	QueueManager.register('get_result_queue', callable=lambda : result_queue)
	QueueManager.register('get_task_queue', callable=return_task_queue)  # pickle序列化不支持匿名函数
	QueueManager.register('get_result_queue', callable=return_result_queue)


	manager = QueueManager(address=('127.0.0.1',5000),authkey=b'abc') # 绑定端口5000,设置验证码abc

	manager.start() # 启动Queue

	#通过网络访问的Queue对象
	task = manager.get_task_queue()  
	result = manager.get_result_queue()

	# 添加几个任务
	for i in range(10):
		n = random.randint(0, 10000)
		print('put task %d...' % n)
		task.put(n)

	# 从result队列读取结果
	print('Try get Results...')
	for i in range(10):
		r = result.get()
		#r = result.get(timeout=10)
		print('result: %s' % r)

	# 关闭
	manager.shutdown()
	print('master exit')