rpc服务框架实现

参考了淘宝的debbo实现

客户端调用方式

**test.py**

	from gaiarpc import GAIA
	server = GAIA("http://127.0.0.1:5000")
	server.call("demo.test",a=1,b=2)
