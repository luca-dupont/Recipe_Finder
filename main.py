import requests
from flask import Flask, render_template, request, redirect

app = Flask(__name__)
recipes = []
pictures = []
html = ''
ingredient = ''

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def main():
    global recipes
    global pictures
    global html
    global ingredient
    if request.method == 'POST':
        ingredient = request.form.get('ingredient')
        resp = requests.get(f"https://www.themealdb.com/api/json/v1/1/filter.php?i={ingredient}")
        if resp.ok:
            pictures = []
            ingredient = ''
            recipes = []
            html = ''
            r = resp.json()
            if r['meals'] == None:
                html += "<h1 style='color:red;text-align:center;text-transform:underscore;text-align:middle;'>No Meals Found</h1>"
                return render_template("home.html",html=html)
            else :    
                for i in range(len(r['meals'])):
                    html += f'<div class="recipe"><h3 class="RecipeTitle"><a href="/{r["meals"][i]["idMeal"]}" class="link">{r["meals"][i]["strMeal"]}</a></h3><a href="/{r["meals"][i]["idMeal"]}" class="link"><img src="{r["meals"][i]["strMealThumb"]}" class = "picture"></a></div>'
        else :
            print(resp.status_code)
            return redirect('error1')
    return render_template("home.html",html=html)

@app.route('/error1')
def apifull():
    return f'<h1 style="color:red;text-align:center;text-transform:underscore;text-align:middle;">ERROR OCCURED</h1>'

@app.route('/error2')
def unknownIngredient():
    return f'<h1 style="color:red;text-align:center;text-transform:underscore;text-align:middle;">UNKNOWN INGREDIENT</h1>'
@app.route('/<id>/')
def recipe(id):
    html2 = ''
    needed_ingredients = []
    resp = requests.get(f"https://www.themealdb.com/api/json/v1/1/lookup.php?i={id}")
    if resp.ok:
        html2 += f'<p>{resp.json()["meals"][0]["strInstructions"]}</p>'
        html2 = html2.replace("\r\n", "<br />")
        html_ingredients = ''
        for i in range(1,21):
            needed_ingredients.append(resp.json()["meals"][0][f"strIngredient{i}"])
        needed_ingredients = filter(lambda x: x != "", needed_ingredients)
        needed_ingredients = list(set(needed_ingredients))
        for i in range(len(needed_ingredients)):
            html_ingredients += f'<p style="text-size:10px;">- {needed_ingredients[i]}</p>'
        return render_template("recipe.html", html2=html2, meal=resp.json()["meals"][0]["strMeal"], bbcode=resp.json()["meals"][0]["strYoutube"], html_ingredients=html_ingredients)
    else :
        return redirect('error1')
    

if __name__ == "__main__":
    app.run(debug=True)