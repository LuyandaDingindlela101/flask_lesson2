#   IMPORT Flask AND THE render_template FUNCTION
from flask import Flask, redirect, url_for

app = Flask(__name__)
admin_users = ["luyanda", "bruce"]


# ADD A ROUTE DECORATOR TO TELL FLASK WHICH URL TO TRIGGER


@app.route("/admin/<name>")
def admin_page(name):
    return f'''
                <body style="background: linear-gradient(to bottom right, #50a3a2 0%, #53e3a6 100%); display: grid; place-content: center">
                    <div style="text-align: center;  color: white">
                        <h1>"Welcome back, {name}. This is the admin page</h1> <br>
                        <a href="http://127.0.0.1:5000/guest/notLuyanda">
                            <button style='outline: 0; background-color: white; border: 0; padding: 10px 15px; color: #53e3a6; border-radius: 3px; width: 250px; cursor: pointer; font-size: 18px; transition-duration: 0.25s; border: 2px solid #53e3a6'>GO TO GUEST</button>
                        </a>
                    </div>
                </body>
            '''


@app.route("/guest/<name>")
def guest_page(name):
    return f'''
                <body style="background: linear-gradient(to bottom right, #50a3a2 0%, #53e3a6 100%); display: grid; place-content: center">
                    <div style="text-align: center; color: white">
                        <h1>"Welcome back, {name}. This is the guest page</h1> <br>
                        <a href="http://127.0.0.1:5000/admin/Luyanda">
                            <button style='outline: 0; background-color: white; border: 0; padding: 10px 15px; color: #53e3a6; border-radius: 3px; width: 250px; cursor: pointer; font-size: 18px; transition-duration: 0.25s; border: 2px solid #53e3a6'>GO TO ADMIN</button>
                        </a>
                    </div>
                </body>
            '''


if __name__ == "__main__":
    app.run(debug=True)
