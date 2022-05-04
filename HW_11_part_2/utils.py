import json

    

def load_candidates_from_json(path):
    """ Загрузка кандидатов из файла """

    with open(path, 'r', encoding='utf-8') as candidates:
        return json.load(candidates)


def get_candidate(candidate_id):
    """ Поиск кандидатов по id """

    for candidate in load_candidates_from_json("candidates.json"):
       if candidate['id'] == candidate_id:
        return candidate


def get_candidates_by_name(candidate_name):
    """ Поиск кандидатов по имени """

    result = []

    for candidate in load_candidates_from_json("candidates.json"):
       if candidate_name in candidate['name']:
         result.append(candidate)

    return result

def get_candidates_by_skill(skill_name):
    """ Поиск кандидатов по скиллу """

    result = []

    for candidate in load_candidates_from_json("candidates.json"):
        candidate_skills = candidate['skills'].lower()
        if skill_name in candidate_skills:
            result.append(candidate)

    return result

