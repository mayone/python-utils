# -*- coding: utf-8 -*-

import json
from api import API

if __name__ == "__main__":
    api = API()
    api.set_url("http://127.0.0.1:5000/")
    print(api.GET("users"))
    print(api.POST("users", json.dumps({"name": "Joseph"})))
    print(api.GET("users"))
