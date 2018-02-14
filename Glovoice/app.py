from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def my_form():

    out_status = "52.89.41.142:8080"
    data = "/login"

    return render_template('page.html', out_status=out_status)

@app.route('/', methods=['POST'])
def my_form_post():

    #Pass something like "Connected to:"/"Not connected"/"Pending Connection to:"
    status = "Pending Connection to: "

    #Pulls ip address from the form
    ip_data = request.form['ip-address']

    data = request.form['data-in']

    #Pass the recognized word here or something like "Unidentified"
    out_word = "Apples"

    out_status = status + "  " + ip_data

    return render_template("page.html", out_word=out_word, out_status=out_status)

if __name__ == "__main__":
   app.run()
