from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.user import User
from flask_app.models.recipe import Recipe

@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect('/logout')
    data ={
        'id': session['user_id']
    }
    return render_template("dashboard.html",user=User.get_by_id(data),items=Recipe.get_all())

@app.route('/new')
def new_recipe():
    if 'user_id' not in session:
        return redirect('/login')
    return render_template('create_recipes.html')

@app.route('/create',methods=['POST'])
def create_recipe():
    if not Recipe.validate(request.form):
        return redirect('/new')  
    Recipe.save(request.form)
    return redirect('/dashboard')

@app.route('/update/<id>')
def edit_recipe(id):
    if 'user_id' not in session:
        return redirect('/login')
    print(Recipe.select_one({"id": id}))
    return render_template('edit_recipes.html',user=User.get_by_id({"id":session['user_id']}),item=Recipe.select_one({"id": id}))