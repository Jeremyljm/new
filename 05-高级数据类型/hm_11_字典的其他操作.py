#!/usr/bin/env python
# -*- coding: utf-8 -*-

xiaoming_dictg = {"name": "小明",
                  "age": 18}

# 1. 统计键值对数量
print(len(xiaoming_dictg))

# 2. 合并字典
temp_dict = {"height": 1.75}


#注意：如果被合并的字典中包含已经存在的键值时，会覆盖原有的键值
xiaoming_dictg.update(temp_dict)

# 3. 清空字典

xiaoming_dictg.clear()


print(xiaoming_dictg)