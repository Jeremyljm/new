#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json

# 将对象转换成json字符串

persons = [
    {
        "username":"zhiliao",
        "age":"18",
        "country":"china"
    },
    {
        "username":"hello",
        "age":"18",
        "country":"china"
    }
]

#json_str = json.dumps(persons)
with open("persons.json","w") as fp:
   # fp.write(json_str)
    json.dump(persons,fp)

