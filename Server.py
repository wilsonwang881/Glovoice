# for using the flask mini-framework
from flask import Flask, render_template, request

# for defining/calling the function on exit
import atexit

# for using the global variable
import Global_Info

# instantiate the flask framework
app = Flask(__name__)

# function on exit
@atexit.register
def goodbye():

    # exit prompt
    print ("You are now leaving the Glovoice server.")

    # reset the connected boolean variable to false
    Global_Info.CONNECTED = False

# test function
# open browser and enter server_IP:port to test
@app.route('/')
def hello_world():

    # the browser should show the following text
    return ('Hello World!')

# URL handler for initiating the connection
@app.route('/login',methods=['GET', 'POST'])
def login():

    # set the boolean variable for the connection to true
    Global_Info.CONNECTED = True

    # prompt
    print ('Client connected')

    # return the HTML, JavaScript, CSS for polling
    return render_template('index.html',name='Hello from Glovoice',server=Global_Info.CONNECTED)

# terminate the conversation
# 'pause' the server
@app.route('/logout',methods=['GET', 'POST'])
def logout():

    # reset the connected boolean variable to false
    Global_Info.CONNECTED = False

    # prompt
    print ('Client disconnected')

    # echo to the client
    return 'Logout received'

# URL handler for
# the web interface that polls the server
@app.route('/query/poll',methods=['GET', 'POST'])
def query_poll():

    # return the global variable
    # that holds the processed information
    return Global_Info.PROCESSED

# URL handler for
# incoming sensor data from the client
@app.route('/query/client',methods=['GET','POST'])
def query_sub():

    # uncomment to show the incoming data
    print (request.get_data())

    # update the global variable that holds the sensor data
    Global_Info.RAW = request.get_data()

    # function call to proccess the raw dataType
    # #################################################

    # update the global variable that holds the processed data
    # Global_Info.PROCESSED =

    # uncomment to echo the processed data to the client
    return Global_Info.PROCESSED

# run the program
if __name__ == '__main__':

    # accessible from external connection
    # change the port number if necessary
    #app.run(host='0.0.0.0',port=5000)

    # only accessible on local machine
    # debug mode
    # DO NOT USE THIS MODE ON SERVER/OR UNDER PRODUCTION ENVIRONMENT
    app.run(debug=True)
