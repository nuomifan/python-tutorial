# -*- coding: utf-8 -*-
"""
Created on Wed Apr 22 20:10:10 2020

@author: demon
"""

import win32com.client
speaker = win32com.client.Dispatch("SAPI.SPVOICE")
speaker.Speak('庭庭是猪')

