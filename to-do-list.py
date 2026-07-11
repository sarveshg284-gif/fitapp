from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>To-Do List</title>
    <style>
        body{
            font-family:Arial,sans-serif;
            background:#f4f4f4;
            margin:40px;
        }
        .container{
            max-width:600px;
            margin:auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0 0 10px rgba(0,0,0,.2);
        }
        h1{
            text-align:center;
        }
        input{
            width:75%;
            padding:10px;
        }
        button{
            padding:10px 15px;
            background:#007BFF;
            color:white;
            border:none;
            cursor:pointer;
        }
        ul{
            list-style:none;
            padding:0;
        }
        li{
            background:#eee;
            margin:10px 0;
            padding:10px;
            border-radius:5px;
            display:flex;
            justify-content:space-between;
        }
        a{
            text-decoration:none;
            color:red;
        }
    </style>
</head>
<body>

<div class="container">

<h1>To-Do List</h1>

<form action="/add" method="POST">
<input
type="text"
name="task"
placeholder="Enter task"
required>

<button>Add</button>
</form>

<ul>

{% for task in tasks %}

<li>

{{task}}

<a href="/delete/{{loop.index0}}">Delete</a>

</li>

{% endfor %}

</ul>

</div>

</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HTML, tasks=tasks)

@app.route("/add", methods=["POST"])
def add():
    task = request.form.get("task")
    if task:
        tasks.append(task)
    return redirect("/")

@app.route("/delete/<int:index>")
def delete(index):
    if 0 <= index < len(tasks):
        tasks.pop(index)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)
