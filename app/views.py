from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/year/<grade>')
@app.route('/year/<grade>/<branch>')
@app.route('/year/<grade>/<branch>/<subject>')
@app.route('/year/<grade>/<branch>/<subject>/<subfolder>')
def giveContent(grade, branch = None, subject = None, subfolder = None):
    contentDict = dict()

    contentDict["grade"] = grade
    contentDict["branch"] = branch
    contentDict["subject"] = subject
    contentDict["subfolder"] = subfolder

    if(branch != None):
        title = grade + "|" + branch
    else:
        title = grade

    import os

    path = os.getcwd() + "/app/static/papers/" + grade
    if(branch != None):
        path += "/" + branch
        if(subject != None):
            path += "/" + subject
            if(subfolder != None):
                path += "/" + subfolder

    contentDict["contentList"] = []
    dummyContentList = os.listdir(str(path))

    tableView = False
    for item in dummyContentList:
        if(os.path.isfile(path + "/" + item) == True):
            tableView = True
            break

    if(tableView == False):
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

        return render_template('main_content.html', contentDict = contentDict, title = title)
    else:
        contentDict["contentList"] = dummyContentList
        return render_template('table_content.html', contentDict = contentDict, title = title)