import os 

from flask import Flask 
from flask import request
from jinja2 import Template

app = Flask(__name__)



def process(target_file, start, end):
    with open('templates/contents.html') as file_:
        template = Template(file_.read())
    try:
        start = int(start) or None
        end = int(end) or None

        file_path = os.path.join("files",target_file)

        try:
            data = open(file_path,"r",encoding="utf-8").readlines()
        except UnicodeError:
            data = open(file_path,"r",encoding="utf-16").readlines()

        output = template.render(title="Contents",contents=data[start:end])

        return output
    except Exception as exc:
        return template.render(title="ERROR",contents=[exc])
        







@app.route('/', defaults={'target_file': "file1.txt"})
@app.route('/<target_file>')
def index(target_file):
    if target_file == "favicon.ico":
        target_file = "file1.txt"

    return process(
        target_file,
        request.args.get("start",0),
        request.args.get("end",0)
    )

if __name__ == '__main__':
    app.run()
       