from flask import Flask
from flask_cors import CORS, cross_origin
import info
import models


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/info", methods=['GET'])
@cross_origin()
def get_info():
    obj = info.Info()
    return obj.get_courses()

@app.route("/api/health", methods=['GET'])
@cross_origin()
def health():
    return "ok"
    
@app.route("/api/calender/members", methods=['GET'])
@cross_origin()
def list_calender_members():
    obj = info.Info()
    professor_objs = obj.get_professors()
    plist = [{x._id:x.first_name+' '+x.last_name} for x in professor_objs.data]
    professor_objs.data = plist
    return professor_objs.toJSON()

@app.route("/api/calender/members/<id>", methods=['GET'])
@cross_origin()
def list_time_slots(id):
    obj = info.Info()
    return obj.get_calender(id).toJSON()

@app.route("/api/calender/members/<id>", methods=['POST'])
@cross_origin()
def book_time_slots(id):
    obj = info.Info()
    return obj.get_professors().toJSON()
    

if __name__ == "__main__":
    app.run()