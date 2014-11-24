import json

def test_demo_api(client):
	payload = {
		"method":"demo.test",
		"params":json.dumps({"a":1,"b":2})
	}
   	r = client.post("/api/",data=payload)
   	assert r.data == "3"
