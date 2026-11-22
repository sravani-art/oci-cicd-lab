from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to OCI CI/CD Lab!</h1>
    <h2>Application deployed successfully.</h2>
    <p>Deployment through GitHub Actions.</p>
    """

@app.route("/health")
def health():
    return jsonify(status="healthy")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
