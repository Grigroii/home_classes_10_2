from flask import Flask
from new_programm import load_json, get_all_person, format_person, get_person_by_id, get_person_by_skill

app = Flask(__name__)


@app.route('/')
def page():
    candidates = get_all_person()
    result = format_person(candidates)
    return result


@app.route('/candidate/<int:uid>')
def page_person(uid):
    candidate = get_person_by_id(uid)
    result = f'<img src= {candidate["picture"]}>'
    result += format_person([candidate])

    return result

@app.route('/skills/<skill>')
def page_skills(skill):
    candidates = get_person_by_skill(skill.lower())
    result = format_person(candidates)
    return result


app.run()
