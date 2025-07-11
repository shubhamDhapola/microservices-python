

import os, requests

def token(request):
      if not "Authorization" in request.header:
            return None, ("missing credentials",401)
      token= request.headers["Authorization"]
      if not token:
            return None, ("missing credentials",401)
      response= requests.post(
          f"http://{os.environ.get('AUTH_SVC_ADDRESS')}/validate",
          headers={"Authorization":token},  
      )
      if response.status_code==200:
            return response.txt, None
      else:
            return None, (response.txt, response.status_code)