#!/usr/bin/env python
# -*- coding: utf-8 -*-

import logging
import os
import time

class LogGen(object):
    def __init__(self, logger):
        self.logger = logging.getLogger(logger)
        self.logger.setLevel(logging.INFO)

        lt = time.strftime('%Y%m%d%H%m',time.localtime(time.time()))
        logname = os.path.dirname(os.path.abspath('.')) + '\\logs\\' +lt + '.log'

        fileh = logging.FileHandler(logname)
        fileh.setLevel(logging.INFO)

        consoleh = logging.StreamHandler()
        consoleh.setFormatter(logging.INFO)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fileh.setFormatter(formatter)
        consoleh.setFormatter(formatter)
        self.logger.addHandler(fileh)
        self.logger.addHandler(consoleh)
    def getlog(self):
        return self.logger