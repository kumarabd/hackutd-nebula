from flask import Flask, request
from flask_cors import CORS, cross_origin
import info
import recommend
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
    
@app.route("/api/course/plan", methods=['GET'])
@cross_origin()
@cache.cached(timeout=500)
def recommend_degree():
    #school = request.args.get('school')
    #subject_prefix = request.args.get('subject_prefix')
    #class_level = request.args.get('class_level')
    school = 'Naveen Jindal School of Management'
    class_level = 'Undergraduate'
    subject_prefix = 'ACCT'
    obj = recommend.Recommend(school, subject_prefix, class_level)
    course_objs = obj.get_courses()
    return obj.get_options(course_objs.data).toJSON()

if __name__ == "__main__":
    app.run()