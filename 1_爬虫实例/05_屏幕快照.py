#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
通过pywin32库，通过调用本地windows API的方式实现抓取功能
屏幕抓取器利用windows图形设备接口（GDI）获取抓取屏幕时必须的参数，如屏幕大小分辨率等信息。
"""
import selenium
import win32gui
import win32ui
import win32con
import win32api
