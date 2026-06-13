from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load portfolio content
with open("data.txt", "r", encoding="utf-8") as f:
    portfolio_text = f.read().lower()

def extract_section(keyword):
    # Convert to lowercase for consistent matching
    keyword = keyword.lower()
    lines = portfolio_text.splitlines()

    capture = False
    content = ""

    for line in lines:
        if keyword in line:
            capture = True
            content += line + "\n"
        elif capture:
            if line.strip() == "" or line.strip().startswith("here is") or line.strip().startswith("about"):
                break  # end of section
            content += line + "\n"

    return content.strip() if content else "No information found."

@app.route("/ask", methods=["POST"])
def ask():
    user_question = request.json.get("question", "").lower()

    # Keyword-based detection
    if "project" in user_question:
        response = extract_section("here is my reply for projects")
    elif "skill" in user_question:
        response = extract_section("here is my reply regarding skills")
    elif "education" in user_question:
        response = extract_section("here is my reply regarding education")
    elif "creator" in user_question or "gulzar" in user_question:
        response = extract_section("about my creator")
    else:
        response = "Sorry, I couldn’t understand. Try asking about projects, skills, education, or my creator."

    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(debug=True)
