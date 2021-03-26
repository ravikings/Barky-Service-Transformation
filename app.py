from sqlalchemy import MetaData
from flask import Flask, jsonify, request, redirect, url_for, render_template
from http import HTTPStatus
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, BigInteger, desc
import sqlite3 as sql
from datetime import datetime


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///./Barky/bookmarks.db'
db = SQLAlchemy(app)

# Sql connection to enable sqlalcehmy
engine = create_engine('sqlite:///./Barky/bookmarks.db', connect_args={'check_same_thread': False}, echo = True)
meta = MetaData()

bookmarks = Table(
                    'bookmarks', meta, 
                    Column('id', Integer, primary_key = True), 
                    Column('title', String), 
                    Column('url', String), 
                    Column('notes', String), 
                    Column('date_added', String), 
                    )

conn = engine.connect()


class boookmarks(db.Model):

    __tablename__ = 'bookmarks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80), unique=True, nullable=False)
    url = db.Column(db.String(120), unique=True, nullable=False)
    notes = db.Column(db.String(120), unique=True, nullable=False)
    date_added = db.Column(db.String(120), unique=True, nullable=False)


@app.route('/', methods = ['POST', 'GET'])
def home():
   return render_template("base.html")


@app.route('/addnew', methods = ['POST', 'GET'])
def new_bookmark():
   return render_template("new.html")


@app.route('/addfilter', methods = ['POST', 'GET'])
def new_filter():
   return render_template("filter.html")

@app.route('/updates', methods = ['POST', 'GET'])
def update():
   return render_template("update.html")

@app.route('/record_delete', methods = ['POST', 'GET'])
def delete():
   return render_template("delete.html")

# Add new bookmark
@app.route('/new', methods = ['POST', 'GET'])
def addnew():
    if request.method == 'POST':
        try:
            
            id = request.form['id']
            title = request.form['title']
            url = request.form['url']
            notes = request.form['notes']
            date_add = datetime.utcnow().isoformat()
            ins = bookmarks.insert().values(id = id, title = title, url = url, notes = notes, date_added = date_add)
            result = conn.execute(ins)

            msg = " Record successfully added"

        except:
            msg = "error in insert operation"

        finally:
            return render_template("result_up.html",msg = msg)

# Selecting bookmark
@app.route('/filter', methods = ['POST', 'GET'])
def bk_filter():
    if request.method == 'POST':
        try:
            id = request.form['id']
            ins = bookmarks.select().where(bookmarks.c.id==id)
            result = conn.execute(ins)
            msg = f'result of Id: {id}'
        except:
            
            msg = "error!!! No Id found"

        finally:
            return render_template("success.html",result=result, msg = msg)
        
# Bookmark recent
@app.route('/recent', methods = ['GET'])
def bk_recent():

        ins = bookmarks.select().order_by(desc(bookmarks.c.title))
        result = conn.execute(ins)
        return render_template("recent.html",result=result)


# list entire bookmanrk
@app.route('/list')
def list():
    bookmark = boookmarks.query.all()
   
    return render_template("list.html",bookmark=bookmark)


@app.route('/new_update', methods = ['POST', 'GET'])
def list_update():
    if request.method == 'POST':
        try:
            
            id = request.form['id']
            title = request.form['title']
            url = request.form['url']
            notes = request.form['notes']
            ins=bookmarks.update().where(bookmarks.c.id==id).values(id = id, title = title, url = url, notes = notes)
            result = conn.execute(ins)

            msg = "Record successfully updated"

        except:
            msg = "error in insert operation, please try again!"

        finally:

            return render_template("result_up.html",msg = msg)


@app.route('/bkdelete', methods = ['POST', 'GET'])
def bk_delete():
    if request.method == 'POST':
        try:
            
            id = request.form['id']
            ins=bookmarks.delete().where(bookmarks.c.id==id)
            result = conn.execute(ins)

            msg = "Record deleted successfully!"

        except:
            msg = "error in deleting record"

        finally:

            return render_template("result_up.html",msg = msg)



if __name__ == '__main__':
    app.run(debug=True)