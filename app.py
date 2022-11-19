import base64, json

from flask import Flask, render_template, request, make_response, jsonify,Response, url_for,redirect
import localisation as loc
from func import get_dataSignal
import io
import func as f
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template("landingPage.html.twig")

@app.route("/temp")
def temp():
    o = get_dataSignal()
    routers = []
    for val in o.keys():
        routers.append(val.strip())
    return render_template('Home.html.twig', title='home Page', routers=routers)

@app.route("/graph")
def graph():

    plt = loc.get_graph()
    data = io.BytesIO()

    plt.savefig(data, format="png")
    data.seek(0)
    data = data.read()

    print("size:", len(data))
    return json.dumps({"img": base64.b64encode(data).decode()})


@app.route("/calculDist", methods=["POST"])
def calculDist():
    ssid=request.get_json()
    for i in ssid :
        s=ssid[i]
    distance=f.get_distance(s.strip())
    print(s.strip())
    print(distance)
    distance=loc.truncate(distance,2)
    return json.dumps({"distance":distance})