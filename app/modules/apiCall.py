from flask import request
from app.modules import getBovespa, getEmpresa
from app.models.dbmodel import db, Empresa


def add_empresa():
    empresa_form = request.form['empresas']
    empresa_nome = getEmpresa.nome(empresa_form)
    cotacao = getEmpresa.cotacao(empresa_form)
    empresa_valor = cotacao[0]
    empresa = Empresa(empresa_nome, empresa_valor)
    return empresa


def delete_by_id(id):
    empresa = Empresa.query.get(id)
    db.session.delete(empresa)
    db.session.commit()

def delete_all():
    todas_empresas = Empresa.query.all()
    for empresa in todas_empresas:
        db.session.delete(empresa)
    db.session.commit()