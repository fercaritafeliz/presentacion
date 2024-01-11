class Color:
    def __init__(self,color):
        self._color=color

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self):
      return self._color

    def __str__(self) -> str:
        return f'Color [Color: {self._color}]'