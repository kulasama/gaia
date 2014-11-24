import json

def test_demo_api(gaia):
   	r = gaia.call("demo.test",a=1,b=2)
   	assert r["result"] == 3
