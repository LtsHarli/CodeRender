import logging
from flask import render_template, request
from flask import current_app as app
from urllib.parse import parse_qs

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def register_routes(app):
    @app.route("/")
    def home_route():
        query_string = request.query_string.decode('utf-8')
        params = parse_qs(query_string)

        html_code = extract_code(params.get('html', [''])[0], 'html')
        css_code = extract_code(params.get('css', [''])[0], 'css')
        js_code = extract_code(params.get('js', [''])[0], 'js')
        output_display = extract_dimensions(params.get('OutputDisplay', [''])[0])
        code_boxes = extract_dimensions(params.get('CodeBoxes', [''])[0])

        return render_template("home.html", html_code=html_code, css_code=css_code, js_code=js_code,
                               output_display=output_display, code_boxes=code_boxes)

    @app.route("/api")
    def api_route():
        return render_template("api.html")

def extract_code(param, code_type):
    delimiters = f'|{code_type}|'
    if param.startswith(delimiters) and param.endswith(delimiters):
        return param[len(delimiters):-len(delimiters)]  # Remove the delimiters
    return param

def extract_dimensions(param):
    if param.startswith('|OutputDisplay|') and param.endswith('|OutputDisplay|'):
        content = param[len('|OutputDisplay|'):-len('|OutputDisplay|')]
        dimensions = {}
        for item in content.split('?'):
            key, value = item.split('=')
            dimensions[key] = value
        return dimensions
    elif param.startswith('|CodeBoxes|') and param.endswith('|CodeBoxes|'):
        content = param[len('|CodeBoxes|'):-len('|CodeBoxes|')]
        dimensions = {}
        for item in content.split('?'):
            key, value = item.split('=')
            dimensions[key] = value
        return dimensions
    return {}