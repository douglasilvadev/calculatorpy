from typing import Dict, List
from pytest import raises
from .calculator_4 import Calculator4

class MockRequest:
    def __init__(self, body: Dict):
        self.json = body

class MockDriverHandler:
    def average(self, input_data: List[float]) -> float:
        return sum(input_data) / len(input_data)  # Cálculo da média

def test_calculate_average():
    # Testa a requisição válida para calcular a média
    mock_request = MockRequest({"numbers": [2, 4, 6, 8]})  # Exemplo de lista de números
    calculator_4 = Calculator4(MockDriverHandler())
    
    response = calculator_4.calculate(mock_request)
    
    assert response == {'data': {'Calculator': 4, 'value': 5.0, 'Success': True}}  # Média esperada: 5.0

def test_calculate_with_invalid_format():
    # Testa uma requisição com formato inválido
    mock_request = MockRequest({"nums": [1, 2, 3, 4, 5]})  # Chave errada
    calculator_4 = Calculator4(MockDriverHandler())
    
    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "body mal formatado!"  # Mensagem de erro esperada

def test_calculate_with_non_numeric_values():
    # Testa uma requisição com valores não numéricos
    mock_request = MockRequest({"numbers": [1, "dois", 3]})  # Valores não numéricos
    calculator_4 = Calculator4(MockDriverHandler())

    with raises(Exception) as excinfo:
        calculator_4.calculate(mock_request)
    
    assert str(excinfo.value) == "Lista de números inválida!"  # Mensagem de erro esperada
