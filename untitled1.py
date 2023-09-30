# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 12:22:23 2023

@author: Rishab
"""

import glassdoor_scraper as gs
import pandas as pd

path = "C:/Users/Rishab/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',15, False, path, 15)