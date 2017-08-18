from flask import Flask, render_template, request, session, redirect

app = Flask(__name__)

@app.route('/')
def show_form():
    return render_template('form.html')

if __name__ == "__main__":
    app.run(
        debug=True,
        port=5000
    )