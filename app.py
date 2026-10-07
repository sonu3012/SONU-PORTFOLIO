import json
import re
import time
from pathlib import Path

from flask import Flask, abort, jsonify, render_template, request, send_from_directory

import data

BASE = Path(__file__).parent
app = Flask(__name__)

MESSAGES_FILE = BASE / "messages.jsonl"
_last_post = {}  # ip -> timestamp, tiny rate limiter
EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


@app.route("/")
def home():
    has_photo = (BASE / "static" / "img" / "profile.png").exists()
    return render_template(
        "index.html",
        p=data.PROFILE,
        stats=data.STATS,
        skills=data.SKILLS,
        process=data.PROCESS,
        projects=data.PROJECTS,
        experience=data.EXPERIENCE,
        education=data.EDUCATION,
        certs=data.CERTIFICATIONS,
        has_photo=has_photo,
    )


@app.route("/resume")
def resume():
    name = data.PROFILE["resume_file"]
    if not (BASE / "static" / name).exists():
        abort(404, description="Add your resume PDF to the static/ folder first.")
    return send_from_directory(BASE / "static", name, as_attachment=True)


@app.post("/api/contact")
def contact():
    payload = request.get_json(silent=True) or {}
    if payload.get("website"):  # honeypot field, bots fill it
        return jsonify(ok=True)

    name = str(payload.get("name", "")).strip()[:100]
    email = str(payload.get("email", "")).strip()[:150]
    message = str(payload.get("message", "")).strip()[:2000]

    if not name or not message or not EMAIL_RE.match(email):
        return jsonify(ok=False, error="Please fill name, a valid email and a message."), 400

    ip = request.remote_addr or "?"
    now = time.time()
    if now - _last_post.get(ip, 0) < 20:
        return jsonify(ok=False, error="Please wait a few seconds before sending again."), 429
    _last_post[ip] = now

    with MESSAGES_FILE.open("a", encoding="utf-8") as f:
        f.write(json.dumps({"time": time.strftime("%Y-%m-%d %H:%M:%S"), "name": name,
                            "email": email, "message": message}, ensure_ascii=False) + "\n")
    return jsonify(ok=True)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
