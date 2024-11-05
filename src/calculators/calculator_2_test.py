from typing import Dict, List
from calculator_2 import Calculator2
from  src.drivers.numpy_handler import NumpyHandler
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface

class MockRequest:
  def __init__(self, body: Dict):
    self.json = body
    
class MockDriverHandler(DriverHandlerInterface):
  def standard_derivation(self, input_data: List[float]) -> float:
    return 3

# Teste de Integração entre a classe Calculator2 e o driver NumpyHandler
def test_calculate_integration():
  mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
  
  driver = NumpyHandler()
  calculator_2 = Calculator2(driver)
  formated_response = calculator_2.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {"data": {"Calculator": 2, "result": 0.08} }
  
def test_calculate():
  mock_request = MockRequest({"numbers": [2.12, 4.62, 1.32]})
  
  driver = MockDriverHandler()
  calculator_2 = Calculator2(driver)
  formated_response = calculator_2.calculate(mock_request)

  assert isinstance(formated_response, dict)
  assert formated_response == {"data": {"Calculator": 2, "result": 0.33} }