from flask import Flask, request
from flask_cors import CORS, cross_origin
import info
import models
from flask_caching import Cache

app = Flask(__name__)
cors = CORS(app)
config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300,
    "CORS_HEADERS":'Content-Type'
}
app.config.from_mapping(config)
cache = Cache(app)

@app.route("/api/info", methods=['GET'])
@cross_origin()
@cache.cached(timeout=500)
def get_info():
    obj = info.Info()
    return obj.get_courses()

@app.route("/api/health", methods=['GET'])
@cache.cached(timeout=500)
@cross_origin()
def health():
    return "ok"
    
@app.route("/api/calender/members", methods=['GET'])
@cross_origin()
@cache.cached(timeout=500)
def list_calender_members():
    obj = info.Info()
    professor_objs = obj.get_professors()
    cache.set('professors', professor_objs.data)
    plist = [{x._id:x.first_name+' '+x.last_name} for x in professor_objs.data]
    professor_objs.data = plist
    return professor_objs.toJSON()

@app.route("/api/calender/members/<id>", methods=['GET'])
@cross_origin()
@cache.cached(timeout=500)
def list_time_slots(id):
    obj = info.Info()
    return obj.get_calender(cache.get('professors'), id).toJSON()

@app.route("/api/calender/members/<id>", methods=['POST'])
@cross_origin()
@cache.cached(timeout=500)
def book_time_slots(id):
    obj = info.Info()
    print(request.data)
    return models.Result('ok', '')
    

if __name__ == "__main__":
    app.run()