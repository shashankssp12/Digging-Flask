from flask import Flask
app = Flask(__name__) # create an app instance and this is the main entry point to the application

@app.route('/') # the site to route to, index/main in this case
def home():
    return "Hello, World!"


if __name__ == '__main__':
    app.run(debug=True) # run the application
    
    
