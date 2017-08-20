from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

data_file = "data.csv"
def read_file(data_file):
    datafile = open(data_file, 'r')
    datareader = csv.reader(datafile,delimiter='\n')
    story_byrow = []
    r = [] 
    for row in datareader:
        for i in row:
            print(type(i))
            r = i.split("    ")
        story_byrow.append(r)    
    return story_byrow

@app.route('/') 
def route_list():
    return render_template('storyboard.html', story_byrow =read_file(data_file))

if __name__ == '__main__':
    app.run(
            debug=True,
            port=5000
    )