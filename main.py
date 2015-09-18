from flask import Flask
from flask import url_for, render_template, redirect
app = Flask(__name__)

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Restaurant, MenuItem

engine = create_engine('sqlite:///restaurantmenu.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# this is how to serve static files:
with app.test_request_context():
    url_for('static', filename='style.css')

# learn more about decorators here: 
# https://realpython.com/blog/python/primer-on-python-decorators/
# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/
# http://thecodeship.com/patterns/guide-to-python-function-decorators/

@app.route('/')
def root():
    return redirect("/restaurants", code=302)

@app.route('/echo/<dest>')
def echo(dest=None):
    return render_template('echo.html', dest=dest)

@app.route('/restaurants/')
def restaurants():
    restaurants = session.query(Restaurant).all()

    return render_template('restaurants.html')

# flask syntax: <type:var> allowed: int, float, path or omit for string (e.g. /<username>/)
@app.route('/restaurant/<int:restaurant_id>/')
def restaurant(restaurant_id):
    r = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
    output = '<h1>%s Menu:</h1>' % r.name
    for i in items:
        output += '<h3>' 
        output += i.name + 'for %s' % i.price
        output += '<a href="/restaurant/%s/%s/edit"> Edit </a>' % (r.id, i.id)
        output += '<a href="/restaurant/%s/%s/delete"> Delete </a>' % (r.id, i.id)
        output += '</h3>'

        output += i.description

    output += '<br><br><button><a href="/restaurant/%s/create"> Create a new menu item </a></button>' % r.id

    return output

@app.route('/restaurant/<int:restaurant_id>/create')
def create_item(restaurant_id):
    r = session.query(Restaurant).filter_by(id=restaurant_id).one()
    items = session.query(MenuItem).filter_by(restaurant_id=restaurant_id)
#    session.commit()

    if session.query(MenuItem).filter_by(restaurant_id=restaurant_id):
        return redirect('/restaurant/%s' % r.id)

    return "create menu item"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/edit')
def edit_item(restaurant_id, menu_id):
    return "edit menu item"

@app.route('/restaurant/<int:restaurant_id>/<int:menu_id>/delete')
def delete_item(restaurant_id, menu_id):
    return "delete menu item"


# let's make sure the server runs only when the script is invoked directly,
# not when run as a module(imported by another python file):
if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
    # notice response codes are taken care of by Flask now!

