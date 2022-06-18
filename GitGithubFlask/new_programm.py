import json


def load_json(json_file):
    with open("candidates.json", "r", encoding="utf-8") as file:
        return json.load(file)


def format_person(candidates):
    """Форматирование списка кандидатов"""
    result = "<pre>"

    for candidate in candidates:
        result += f"""
                {candidate["name"]}
                {candidate["position"]}
                {candidate["skills"]}
            """
    result += '</pre>'
    return result


def get_all_person():
    return load_json('candidates.json')


def get_person_by_id(uid: int):
    candidates = get_all_person()
    for candidate in candidates:
        if candidate["id"] == uid:
            return candidate
    return None


def get_person_by_skill(skill: str):
    candidates = get_all_person()
    result = []
    for candidate in candidates:
        if skill in candidate["skills"].lower().split(', '):
            result.append(candidate)
    return result
