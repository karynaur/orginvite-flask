from flask import Flask, request, render_template 
from ghapi.all import GhApi
import os

token = os.environ['TOKEN']
owner = os.environ['OWNER']
organization = os.environ['ORG']


app = Flask(__name__)   
api = GhApi(owner, token)


# Helper funtions

def send_invite(user_email):
    
    try:
        api.orgs.
        api.orgs.create_invitation(organization, email = user_email)
        return True
    except:
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
        if check_user(username):
            if send_invite(email):
                message = f"Invitation sent to {email}!"
                return render_template("index.html", message = message)
            else: 
                error = "Invitation failed! Email does not exist" 
                return render_template("index.html", error = error)
        else: 
            error = "Could not find user"
            return render_template("index.html", error = error)
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()