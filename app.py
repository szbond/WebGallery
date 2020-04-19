from flask import Flask, render_template, request,  make_response, redirect, url_for, send_from_directory
import Compre
import os
import json
import page
app = Flask(__name__)
comp = Compre.Compre()
print(comp.thumbPath)
pics = os.listdir("./static/images/thumb")
pages = page.Pages(comp)
pages.cleanPages()
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
    reqDict = request.args.to_dict()
    picName = reqDict["pic"]
    picTags = json.loads(reqDict["tags"])
    
    comp.subTags(picName, picTags)
    pages.pages[pages.currentPage][picName].extend(picTags)

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
    if pageNo in pages.pages.keys():
        res = make_response(pages.pages[pageNo])
        pages.currentPage = pageNo
    else:
        pages.loadMore(pageNo)
        
        if pageNo in pages.pages.keys():
            pages.currentPage = pageNo
            res = make_response(pages.pages[pageNo])
        else:
            # 重定向主页
            res = make_response(pages.pages[1])
    res.headers["Access-Control-Allow-Origin"] = "*"
    
    return  res
    # data:JSON.parse()

@app.route("/get/realPic/<picName>", methods = ["GET"])
def sendRealPic(picName):
    if picName in pages.pagePicOrg.keys():
        imgFile = open(pages.pagePicOrg[picName], "rb")
        img = imgFile.read()
        imgFile.close()
        res = make_response(img)
        
        res.headers["Content-Type"] = "image/jpeg"
        # res.headers["Access-Control-Allow-Origin"] = "*"
        # return send_from_directory(pages.pagePicOrg[picName], picName)
        return res
    else:
        return redirect("/")



if __name__ == "__main__":
    app.run()
