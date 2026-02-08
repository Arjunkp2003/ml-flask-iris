from flask import Flask, redirect, url_for
from routes.predict_routes import predict_bp
from routes.auth_routes import auth_bp
from db.database import create_users_table
from config import SECRET_KEY

app = Flask(__name__)
app.secret_key = SECRET_KEY

# Initialize DB table
create_users_table()

# Register blueprints
app.register_blueprint(auth_bp)
app.register_blueprint(predict_bp)

@app.route("/")
def index():
    return redirect(url_for("auth.login"))

if __name__ == "__main__":
    app.run(debug=True)
