from gaia.api.core import bind


@bind("demo.test")
def test(a,b):
	return str(a+b)




