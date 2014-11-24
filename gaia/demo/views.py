from gaia.api.core import bind


@bind("demo.test")
def test(a,b):
	return a+b




