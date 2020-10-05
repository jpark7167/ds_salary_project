# -*- coding: utf-8 -*-
"""
Created on Sun Oct  4 19:58:06 2020

@author: jpark
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/jpark/Documents/ds_salary_project/chromedriver"

df = gs.get_jobs('data scientist', 15, False, path, 15)
