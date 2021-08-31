from flask import Flask, request, render_template 
from ghapi.all import GhApi
import yaml

with open('./github.cfg','r') as f:
    cfg = yaml.full_load(f.read())

"""
cfg: 
    owner: String `name`
    token: String `token`
    organization: String `name`
"""

app = Flask(__name__)   
api = GhApi(owner = cfg['owner'], token = cfg['token'])
# Helper funtions

def send_invite(user_email):
    
    try:
        api.orgs.create_invitation(cfg['organization'], email = user_email)
        return True
    except e:
        return False

def check_user(username):
    try:
        user = api.users.get_by_username(username)
        return True
    except:
        return False
    

@app.route('/', methods =["GET", "POST"])
def get_details():
    if request.method == "POST":
        username = request.form.get("username")
        email = request.form.get("email") 
        if check_user:
            if send_invite(email):
            return "Success"
            else: return "invite not sent"
        else: return "User does not exist"
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()