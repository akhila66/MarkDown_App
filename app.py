from types import MethodDescriptorType
from typing import Text
import flask
# from flask_cors import CORS
from flask_cors import CORS, cross_origin
import re

app = flask.Flask(__name__)
cors = CORS(app)

@app.route("/", methods = ["GET"])
def home():
    return "lets convert markdown to html"

@app.route("/convert", methods = ["POST"])
def convert():
    source = flask.request.get_json()['text']
    """
    Input: Markdown string
    Output: HTML formated string
    
    Funtion Operation: Converts few simple markdown string to html format
    ---------------------------------------------------------------------
    check for each line
        if its not new line and has some text performs below modifications
            - check and convert [.*](.*) to hyperlink tag format
            - check header levels from '#' and convert to respective tags
                - if not header convert to paragraph tag (Assuming all rest of them gonna be in <p> tag)
    join all and return with new lines
    
    """
    lines = source.split('\n')
    modified = []
    for s in lines:
        if s:
            # repalce links
            for i in re.finditer('\[(.*)\]\((.*)\)', s):
                s = s.replace(i.group(0), '<a href="'+(i.group(2))+'">'+(i.group(1))+'</a>')
                
            # replace headers only 
            header = re.match('(^[#]+)(.*)', s)
            if(header):
                length = str(len(header.group(1)))
                s = s.replace(header.group(0), "<h"+length+">"+header.group(2)+"</h"+length+">")
            else:
                s = "<p>"+s+"</p>"

        modified.append(s)

    source = '\n'.join(modified)
    return source
