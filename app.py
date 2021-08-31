from flask import Flask, request, render_template 

app = Flask(__name__)   

@app.route('/', methods =["GET", "POST"])
def get_details():
    if request.method == "POST":
       username = request.form.get("username")
       email = request.form.get("email") 
       return "Your details are " + username + " " + email
    return render_template("index.html")
  
if __name__=='__main__':
   app.run()