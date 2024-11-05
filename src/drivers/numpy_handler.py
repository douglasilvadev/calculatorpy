import numpy as np
from typing import List
from src.drivers.interfaces.driver_handler_interface import DriverHandlerInterface
    
class NumpyHandler(DriverHandlerInterface):
  def __init__(self) -> None:
    self.__np = np
  
  def standard_derivation(self, numbers: List[float]) -> float:
    return self.__np.std(numbers)
  
  def standard_derivation_with_param(self, numbers: List[float]) -> float:
    return self.__np.std(numbers, axis=[])
  
  def variance(self, numbers: List[float]) -> float:
    return self.__np.var(numbers)