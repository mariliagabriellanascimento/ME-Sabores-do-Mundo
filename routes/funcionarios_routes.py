from flask import Blueprint

funcionarios_bp = Blueprint('funcionarios', __name__)

# Rota para listar funcionários
@funcionarios_bp.route('', methods=['GET'])
def listar_funcionarios():
    return "Lista de Funcionários"
