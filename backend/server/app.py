from flask import Flask
from flask_cors import CORS, cross_origin
import info


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/api/info", methods=['GET'])
@cross_origin()
def get_info():
    obj = info.Info()
    obj.Do()
    return obj.toJSON()

@app.route("/api/health", methods=['GET'])
@cross_origin()
def health():
    return "ok"
    

if __name__ == "__main__":
    app.run()