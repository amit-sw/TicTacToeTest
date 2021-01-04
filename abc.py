import requests
import json

def get_prediction(data={"num_countries":8,"years_school":1,"height":4.165}):
  url = 'https://923rstg27g.execute-api.us-east-1.amazonaws.com/Predict/4e38cc07-261f-4a53-87dd-795979fe28d2'
  r = requests.post(url, data=json.dumps(data))
  response = getattr(r,'_content').decode("utf-8")
  print(response)
  return response
