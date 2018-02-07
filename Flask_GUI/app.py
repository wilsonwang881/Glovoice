from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def my_form():
    return render_template('page.html')

@app.route('/', methods=['POST'])
def my_form_post():

    ip_data = request.form['ip-address']
    ip_target = open('data/ip.txt', 'w')
    ip_target.truncate()
    ip_target.write(ip_data)
    ip_target.close()

    out_file = open('data/word-out.txt', 'r')
    out_word = out_file.read()
    out_file = open('data/word-out.txt', 'w')
    out_file.truncate()
    out_file.close()

    return render_template("page.html", out_word=out_word)

if __name__ == "__main__":
   app.run()
