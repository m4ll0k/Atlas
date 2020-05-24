#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import random
from lib.file import *

def ragent():
	path = os.path.join(os.path.abspath('.'),'db/user_agents.txt')
	user_agents = [x for x in readfile(path)]
	return user_agents[random.randint(0,len(user_agents))]