from repository import app, db
from flask import render_template, url_for, redirect, request
from repository.models import Estoque_Movimento, Produto


@app.route('/')
def index():
    estoque = db.session.execute(db.select(Estoque_Movimento).order_by(Estoque_Movimento.id_produto)).scalars()
    # estoque = Estoque_Movimento.query.all()
    return render_template('index.html', estoque=estoque)

@app.route('/add', methods=['GET', 'POST'])
def add():
    produtos = db.session.execute(db.select(Produto).order_by(Produto.id_produto)).scalars()
    if request.method == "POST":
        estoque = Estoque_Movimento(
            id_produto = request.form['id_produto'],
            quantidade_produto=request.form['quantidade_produto'],
            # valor_unitario=request.form['valor_unitario'],
            data_movimento=request.form['data_movimento'],
            numero_nf=request.form['numero_nf'],
            tipo_movimento=request.form['tipo_movimento'],
            status_movimento=request.form['status_movimento']
        )
        db.session.add(estoque)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html', produtos=produtos)

@app.route('/delete/<int:id_produto>/<string:data_movimento>/<int:numero_nf>/<string:tipo_movimento>/')
def delete(id_produto, data_movimento, numero_nf, tipo_movimento):
    id_produto = Estoque_Movimento.query.get(id_produto)
    data_movimento = Estoque_Movimento.query.get(data_movimento)
    numero_nf = Estoque_Movimento.query.get(numero_nf)
    tipo_movimento = Estoque_Movimento.query.get(tipo_movimento)
    db.session.delete(id_produto, data_movimento, numero_nf, tipo_movimento)
    db.session.commit()
    return redirect(url_for('index'))

@app.route('/edit/<int:id_produto>', methods=['GET', 'POST'])
def edit(id_produto):
    estoque = Estoque_Movimento.query.get(id_produto)
    if request.method == "POST":
        estoque.id_produto = request.form['id_produto'],
        estoque.quantidade_produto = request.form['quantidade_produto'],
        estoque.valor = request.form['valor'],
        estoque.data_p = request.form['data_p']
        estoque.numero_nf = request.form['numero_nf']
        estoque.tipo_movimento = request.form['tipo_movimento']
        return redirect(url_for('index'))
    return render_template('edit.html')