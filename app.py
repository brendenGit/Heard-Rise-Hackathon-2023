from flask import Flask, redirect, render_template, jsonify, request
from models import db
from data import teams

import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///heard-app'
app.config['SECRET_KEY'] = 'sage123'
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False

db.init_app(app)

# Create the database tables
with app.app_context():
    db.create_all()

with open("prompt.txt", "r") as file:
    prompt_text = file.read()

conversation = [{"role": "system", "content": prompt_text}]


@app.route("/")
def show_index():
    """Homepage"""

    return render_template("submit.html")


##############################################################################
# OpenAI routes

@app.route("/send", methods=['POST'])
def send_submission():
    """Send initial submission to OpenAI"""

    user_submission = {"role": "user",
                       "content": request.json.get('user_submission', '')}

    conversation.append(user_submission)

    completion = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=conversation
    )

    conversation.append(
        {"role": "system", "content": completion.choices[0].message.content})
    print(conversation)

    response = {"message": completion.choices[0].message}

    return jsonify(response)


##############################################################################
# Route to render teams

@app.route("/teams", methods=['GET'])
def show_teams():
    """Render teams with summarized blockers"""

    return render_template("teams.html", teams=teams)


# Route to display specific blockers for a team
@app.route("/teams/<int:team_id>", methods=['GET'])
def show_team_blockers(team_id):
    """Filter blockers for the selected team"""

    selected_team = next(
        (team for team in teams if team["id"] == team_id), None)

    if selected_team:
        team_blockers = selected_team.get("summarized_blockers", "")
        team_submissions = selected_team["submissions"]
        return render_template("team_blockers.html", team_blockers=team_blockers, team_submissions=team_submissions)

    return "Team not found"
