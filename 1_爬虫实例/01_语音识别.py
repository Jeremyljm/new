#!/usr/bin/env python
# -*- coding: utf-8 -*-

from aip import AipSpeech

app_id = "14975947"
api_key = "X9f3qewZCohppMHxlunznUbi"
secret_key = "LupWgIIFzZ9kTVNZSH5GOguNGZIqqTom"

client = AipSpeech(app_id, api_key, secret_key)
result = client.synthesis("哈哈，你好！", "zh", 1,{
    "vol": 9,
    "spd": 6,
    "pit": 7,
    "per": 4,
} )

with open("audio.mp3", "wb") as f:
    f.write(result)