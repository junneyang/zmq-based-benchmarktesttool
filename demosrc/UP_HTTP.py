#-*- coding: utf-8 -*-
#!/usr/bin/env python
import httplib
import json

conn = httplib.HTTPConnection("10.81.15.47:18080")
headers = {"Content-type":"application/json"}
params = ({
               "service": "UserService",
            	"method": "GetUserPreference",
               "request": {
            	  "header": {
               	   "subservice":"sub",
               	   "secretkey": "pass",
               	   "servicekey": "key1"
           	   },
               "cuid": "fed3641138107dca4c101fd70fa96979",
               "srcType": ["MAP_CATEGORY","TUANGOU_PRICE"],
            "include_tag":[u"医疗",u"建材市场"],
            "exclude_tag":[u"体检中心",u"文具店"]
    	   }
    })
conn.request("POST", "/lbs/da/openservice", json.JSONEncoder().encode(params), headers)
try:
    response = conn.getresponse()
    data = response.read()
    print data
except Exception as e:
    print(e)
finally:
    conn.close()
