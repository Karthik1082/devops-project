from flask import Flask
app = Flask(__app__)
@app.route('/')
def home():
    return "Karthik Devops Project"

@app.route('/skills')
def skills():
    return "Docker,Kubernetes,GitHub Actions"

app.run(host:'0.0.0.0', port=5000)
