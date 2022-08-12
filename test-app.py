from flask import Flask
from rate_limitter import limit




app = Flask(__name__)


@app.route("/")
@limit()
def func():
  return "hello"

  
if __name__ == "__main__":
  app.run(host="localhost", debug=True, port=3001)
