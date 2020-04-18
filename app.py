from flask import Flask, render_template, request,  make_response
import Compre
import os
import json
import page
app = Flask(__name__)
comp = Compre.Compre()
print(comp.thumbPath)
# picLs = comp.readPage(10)
# comp.cleanThumb()

pics = os.listdir("./static/images/thumb")
pages = page.Pages(comp)
pages.loadPages(10,5)


@app.route("/")
def index():
    return render_template("index.html", pics = pics)

@app.route("/images/<name>")
def find(name):
    org = comp.database.findOrg(name)
    return org[0]

@app.route("/submit/tags", methods = ["GET"])
def submitTag():
    res = make_response(json.dumps(request.args.to_dict()["tags"]))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return  res, 201

@app.route("/get/tags", methods = ["GET"])
def getTags():
    # res = make_response(json.dumps(request.args.to_dict()["tags"]))
    tags = ["tags"]
    res = make_response(json.dumps(tags))
    res.headers["Access-Control-Allow-Origin"] = "*"
    return  res, 201
@app.route("/get/page", methods = ["GET"])
def getPics():
    pageNo = int(request.args.to_dict()["pageNo"])
    if pageNo < len(pages.pages) and pageNo > 0:
        res = make_response(pages.pages[int(pageNo)-1])
        print(pages.pages[int(pageNo)-1])
    else:
        res = make_response(pages.pages[0])
    res.headers["Access-Control-Allow-Origin"] = "*"
    
    return  res
    # data:JSON.parse()


if __name__ == "__main__":
    app.run()
