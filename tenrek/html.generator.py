import json
from jinja2 import Template

with open("output.json", "r", encoding="utf-8") as f:
    data = json.load(f)

template = Template("""
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Report</title>
    <style>
        table { border-collapse: collapse; width: 100%; }
        td, th { border: 1px solid #ccc; padding: 6px; }
        th { background: #eee; }
    </style>
</head>
<body>
    <h1>Code Metrics Report</h1>
    <table>
        <tr>
            <th>Name</th><th>LOC</th><th>Cyclomatic</th><th>Volume</th><th>Difficulty</th>
        </tr>

        {% for item in data %}
        <tr>
            <td>{{ item.name }}</td>
            <td>{{ item.loc }}</td>
            <td>{{ item.cyclomatic }}</td>
            <td>{{ "%.2f"|format(item.halstead_volume) }}</td>
            <td>{{ "%.2f"|format(item.halstead_difficulty) }}</td>
        </tr>
        {% endfor %}
    </table>
</body>
</html>
""")

html = template.render(data=data)

with open("report.html", "w", encoding="utf-8") as f:
    f.write(html)




# чтобы сам открылся
import webbrowser
import os

webbrowser.open('file://' + os.path.realpath("report.html"))