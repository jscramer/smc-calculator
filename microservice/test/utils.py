from typing import TypeVar, Callable

from conftest import app

class MockUtils:
  FuncReturnType = TypeVar("FuncReturnType")
  FuncSignature = Callable[..., FuncReturnType]

  @classmethod
  def add_mock(cls, original_func: FuncSignature, mock_func: FuncSignature):
    app.dependency_overrides[original_func] = mock_func

  @classmethod
  def remove_mock(cls, original_func: FuncSignature):
    app.dependency_overrides.pop(original_func)