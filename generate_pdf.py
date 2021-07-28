# https://pbpython.com/pdf-reports.html
# https://cloudstack.ninja/erik/weasyprint-and-css-header-footer-pagebreak-and-positioning/
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

env = Environment(loader=FileSystemLoader('.'))
template = env.get_template("templates/report.html") 

data = [{"name": "Axel García", "age": 12}, {"name": "Guadalupe", "age": 5}]

template_vars = {"title" : "un ejemplo", "pipols": data}

html_out = template.render(template_vars)

HTML(string=html_out).write_pdf("report.pdf", stylesheets=["static/styles.css"])


