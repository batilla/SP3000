from flask import Flask, render_template, redirect, request
import csv

app = Flask(__name__)

data_file = "data.csv"

def read_file(data_file):
    datafile = open(data_file, 'r')
    datareader = csv.reader(datafile, delimiter='\n')
    story_byrow = []
    r = [] 
    for row in datareader:
        for i in row:
            r = i.split(";")
        story_byrow.append(r)    
    return story_byrow

def write_file(data_file, result):
   with open(data_file, "a") as file:
       row = ';'.join(result)
       print(row)
       file.write(row + '\n')


def update(id_, updated_story):
    #dict->list
    pass

def find_index_by_id(id_):
    pass

def delete(id_):
    #id_ != index
    pass

def save_new_story(new_story):
    #dict->list
    pass

@app.route('/') 
def route_list():
    return render_template('list.html', story_byrow =read_file(data_file))

@app.route('/story', methods=['GET'])
def route_create():
    return render_template('form.html')

@app.route("/story/<int:id_>", methods=["GET"])
def edit(id_):
    return render_template('form.html')

@app.route('/save-toform', methods=["POST"])
def route_save():
    dictform = {}
    result = []
    formdata = request.form
    for item in formdata.items():
        dictform[item[0]] = item[1]
    result = list(dictform.values())
    write_file(data_file, result)
    print(result)
    return redirect('/')


if __name__ == '__main__':
    app.run(
            debug=True,
            port=5000
    )