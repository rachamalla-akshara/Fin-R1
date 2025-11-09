from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import subprocess
import os

# Import database models and router
from models import db, User, Chat
from router import route_message

# ---------------------------
# Flask App Configuration
# ---------------------------
app = Flask(__name__)
app.secret_key = "finchatgpt_secret_key"

# ✅ Database setup
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DB_DIR = os.path.join(BASE_DIR, "instance")
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "users.db")

app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{DB_PATH}"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# ✅ Initialize DB and Login
db.init_app(app)
login_manager = LoginManager(app)
login_manager.login_view = "login"

# ---------------------------
# User Loader
# ---------------------------
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# ---------------------------
# Routes: Register / Login / Logout
# ---------------------------
@app.route("/")
def home():
    return redirect("/login")

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        if User.query.filter_by(username=username).first():
            return "⚠️ Username already exists."

        hashed_pw = generate_password_hash(password)
        new_user = User(username=username, password=hashed_pw)
        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for("login"))
    return render_template("register.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"]
        password = request.form["password"]

        user = User.query.filter_by(username=username).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for("chat"))
        else:
            return "Invalid username or password."
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# ---------------------------
# Chat Route
# ---------------------------
@app.route("/chat", methods=["GET", "POST"])
@login_required
def chat():
    if request.method == "POST":
        data = request.get_json()
        user_input = data.get("message", "").strip()

        result = route_message(user_input)

        new_chat = Chat(
            user_input=user_input,
            bot_response=result["answer"],
            user_id=current_user.id
        )
        db.session.add(new_chat)
        db.session.commit()

        return jsonify({
            "user": current_user.username,
            "question": user_input,
            "think": result["think"],
            "answer": result["answer"]
        })

    user_chats = Chat.query.filter_by(user_id=current_user.id).all()
    return render_template("chat.html", chats=user_chats, user=current_user)

# ---------------------------
# Run Flask App
# ---------------------------
if __name__ == "__main__":
    with app.app_context():
        db.create_all()

    print("🚀 FinChatGPT is running at http://127.0.0.1:5000/")
    app.run(debug=True)
