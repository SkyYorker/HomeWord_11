import utils


from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    """ Выводит всех кандидатов из файла """
    candidate_list = utils.load_candidates_from_json("candidates.json")
    return render_template("list.html", candidate_list=candidate_list)


@app.route('/candidate/<int:candidate_id>')
def page_candidate(candidate_id):
    """ Выводит кандидата по id и показывает его страничку """
    candidate = utils.get_candidate(candidate_id)
    return render_template("single.html", candidate=candidate)


@app.route('/search/<candidate_name>')
def page_candidate_name(candidate_name):
    """ Выводит кандидатов, если в имени содержится такой символ """
    candidates = utils.get_candidates_by_name(candidate_name)
    return render_template("search.html", candidates=candidates, candidates_count=len(candidates))


@app.route('/skill/<string:skill_name>')
def get_candidates_by_skill(skill_name):
    """ Выводит кандидатов, если у них есть это умение """
    candidates = utils.get_candidates_by_skill(skill_name)
    return render_template("skill.html", candidates=candidates, candidates_count=len(candidates))
app.run()