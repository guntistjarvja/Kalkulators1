#from flask import Flask, render_template
#app = Flask(__name__)
from flask import Flask, render_template
app = Flask('app')
@app.route('/')
def root():
  return render_template('index.html')
#  return render_template('index.html')



#app.run(host='0.0.0.0', port=8020)
if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    app.run(threaded=True, port=5000)

