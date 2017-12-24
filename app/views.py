from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/year/<grade>')
@app.route('/year/<grade>/<branch>')
def giveContent(grade, branch = None, isCollapse = False):
    contentDict = dict()

    contentDict["grade"] = grade

    if(grade == "FY"):
        contentDict["isMore"] = False
    elif(branch == None):
        contentDict["isMore"] = True
    else:
        contentDict["isMore"] = False

    import os

    path = os.getcwd() + "/app/static/papers/" + grade
    if(branch != None):
        path += "/" + branch

    contentDict["contentList"] = []
    dummyContentList = os.listdir(str(path))
    count = 0
    helperList = []
    for item in dummyContentList:
        helperList.append(item)
        count += 1
        if(count == 2):
            contentDict["contentList"].append(helperList)
            helperList = []
            count = 0

    if(len(helperList) != 0):
        contentDict["contentList"].append(helperList)

    if(isCollapse == False):
        return render_template('main_content.html', contentDict = contentDict, title = "Test")
