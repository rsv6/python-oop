from flask import Flask, request, url_for, render_template
# from flask_cors


app = Flask(__name__)

# url_for('static', filename='style.css')

@app.route("/user/opc/<name>", methods=['GET'])
def home(name=None):
  # return check_request(request)
  return render_template('index.html', name=name)

@app.get("/users")
def users():
  return {
    "nome": "Rafael Santos",
    "email": "rrsv@email.com",
    "cpf": "2134234325423"
  }

@app.get("/user/<int:id>")
def getIdUserName(id):
  return f"<p>Hello Home, id: {id} </p>"

@app.get("/user/<username>")
def getUserName(username):
  return f"<p>Hello Home {username} </p>"

def check_request(request):
  if request.method == 'POST':
    return f'<p>POST Request: {request.method}</p>'
  else:
    return f'<p>GET Request: {request.method}</p>'
  

# with app.test_request_context('/users', method='GET'):
#   assert request.path == '/users'
