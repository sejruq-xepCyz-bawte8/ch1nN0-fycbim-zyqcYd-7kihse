import anvil.server
import anvil.users
from .generic import HtmlElement

class Icon(HtmlElement):
  def __init__(self, icon: str = 'icons') -> None:
    classlist = ["test"]
    super().__init__(tag = 'i', classlist = classlist)


if __name__ == "__main__":
  i = Icon(icon="test")
  print(i)
