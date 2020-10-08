from urllib import request as req
from FlaskWebProject1 import app,request

@app.route("/get_schools",methods=["post","get"])
def get_schools():
    district=request.args["district"]
    headers={"Origin":"http://211.153.82.39",
                 "Referer":"http://211.153.82.39/usercenter/portalManage/resetPwdAction1.action",
                 "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:81.0) Gecko/20100101 Firefox/81.0"}
    r=req.Request("http://211.153.82.39/usercenter/portalManage/changeSchoolByDistrictAction.action?district="+district,
                  headers=headers)
    r=req.urlopen(r).read().decode()

    return r
