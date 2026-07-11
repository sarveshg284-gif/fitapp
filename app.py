from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

tasks = []

HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Python To-Do List</title>
    <style>
        body{
            font-family:Arial, sans-serif;
            background:#f4f4f4;
            padding:40px;
        }
        .container{
            max-width:600px;
            margin:auto;
            background:white;
            padding:20px;
            border-radius:10px;
            box-shadow:0 0 10px rgba(0,0,0,0.2);
        }
        h1{
            text-align:center;
            color:#333;
        }
        input[type=text]{
            width:75%;
            padding:10px;
            font-size:16px;
        }
        button{
            padding:10px 15px;
            background:#007BFF;
            color:white;
            border:none;
            cursor:pointer;
        }
        button:hover{
            background:#0056b3;
        }
        ul{
            list-style:none;
            padding:0;
            margin-top:20px;
        }
        li{
            display:flex;
            justify-content:space-between;
            align-items:center;
            padding:10px;
            margin:8px 0;
            background:#eeeeee;
            border-radius:5px;
        }
        a{
            color:red;
            text-decoration:none;
            font-weight:bold;
        }
    </style>
</head>
<body>

<div class="container">
    <h1>To-Do List</h1>

    <form action="/add" method="POST">
        <input type="text" name="task" placeholder="Enter a task" required>
        <button type="submit">Add</button>
    </form>

    <ul>
    {% for task in tasks %}
        <li>
            {{ task }}
            <a href="/delete/{{ loop.index0 }}">Delete</a>
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

# This line is used for local development.
# Vercel imports the "app" object directly.
if __name__ == "__main__":
    app.run(debug=True)
