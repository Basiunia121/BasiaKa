from poimanager import POIManager
from flask import Flask
from flask import request
app = Flask(__name__)

poimanager = POIManager()

@app.route('/')
def index():
  return "["+",".join([str(x) for x in poimanager.get_all_poi()])+"]"

@app.route('/add')
def add_poi():
  x = request.args.get('x')
  y = request.args.get('y')
  name = request.args.get('name')
  return ""
  
@app.route('/find')
def find_poi():
  x = request.args.get('x')
  y = request.args.get('y')
  r = request.args.get('r')
  return "Punkty znajdujace sie w zadanym obszarze:"+"["+",".join([str(x) for x in poimanager.get_poi_near(x,y,r)])+"]"

if __name__ == "__main__":
  app.run(debug=True)
