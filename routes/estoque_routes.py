from flask import Blueprint, render_template, request, redirect, url_for
from models.estoque_model import listar_estoque, cadastrar_produto

estoque_bp = Blueprint('estoque', __name__)

# Rota para listar produtos do estoque
@estoque_bp.route('', methods=['GET'])
def listar_estoque_view():
    produtos = listar_estoque() 
    return render_template('estoque.html', produtos=produtos)

# Rota para cadastrar um novo produto
@estoque_bp.route('/cadastro', methods=['GET', 'POST'])
def cadastro_produto_view():
    if request.method == 'POST':
        nome = request.form['nome']
        quantidade = int(request.form['quantidade'])
        limite_minimo = int(request.form['limite_minimo'])
        
        cadastrar_produto(nome, quantidade, limite_minimo)
        return redirect(url_for('estoque.listar_estoque_view'))
    
    return render_template('cadastro_produto.html')
