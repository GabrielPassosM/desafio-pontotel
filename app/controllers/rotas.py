from flask import render_template, request, redirect, url_for
from app import app
from app.modules import getBovespa, apiCall
from app.models.dbmodel import db, Empresa
import requests


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/bovespa')
def bovespa():
    valor = getBovespa.pontuacao()
    data = getBovespa.data()
    return render_template('bovespa.html', valor=valor, data=data)

@app.route('/empresas')
def empresas():
    empresa_db = Empresa.query.all()
    return render_template('empresas.html', empresa_db=empresa_db)

@app.route('/api_call', methods=['GET', 'POST'])
def api_call():
    empresa = apiCall.add_empresa()
    try:
        db.session.add(empresa)
        db.session.commit()
    except:
        return redirect(url_for('empresas'))
    
    return redirect(url_for('empresas'))

@app.route('/delete/<int:id>')
def delete(id):
    apiCall.delete_by_id(id)
    return redirect(url_for('empresas'))

@app.route('/delete_all')
def delete_all():
    apiCall.delete_all()
    return redirect(url_for('empresas'))