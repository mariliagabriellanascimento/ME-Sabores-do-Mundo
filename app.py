from flask import Flask, render_template
from routes.estoque_routes import estoque_bp
from routes.funcionarios_routes import funcionarios_bp

app = Flask(__name__)

# Rota para a página inicial
@app.route('/')
def index():
    return render_template('index.html') 

# Registra as rotas
app.register_blueprint(estoque_bp, url_prefix='/estoque')
app.register_blueprint(funcionarios_bp, url_prefix='/funcionarios')

if __name__ == '__main__':
    app.run(debug=True, port=5004)
