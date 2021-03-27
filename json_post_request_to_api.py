# -*- coding: utf-8 -*-
"""
Makes a post request to the jaipur API
"""

import requests

param_dict = {"interview_score3":20,
              "experience":20,
              "test_score":20,
              "interview_score5":20,
              "interview_score6":20
              }


req = requests.post(url=r'https://jaipur-destiny.oa.r.appspot.com/predict_api', json=param_dict)
print(req.json())