
import redis

"""
an open source rate-limiter for flask app
"""

def limit(redis_host="localhost", redis_port=6379, amount=5):
  def inner(func):
    def wrapper(*args, **kwargs):
      pool = redis.ConnectionPool(
        host=redis_host,
        port=redis_port
        )
      rd = redis.Redis(connection_pool=pool)
      if rd.get("visited") is None:
        rd.set("visited", 0)
      if(int(rd.get("visited")) < amount):
        current = int(rd.get("visited"))
        rd.set("visited", current+1)
        #print("requested",rd.get("visited"))
        return func(*args, **kwargs)
      else:
        #print(rd.get("visited"))
        #print("too much request")
        raise Exception("you sent too much request")
        #return func(*args, **kwargs)
    return wrapper
  return inner

"""
@addsix(a=5, b=4)
def sayhi():
  return "hello"
  

print(sayhi())
"""