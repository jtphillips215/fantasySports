class Player:
  def __init__(self, first_name: str, last_name: str, avg_score: float, races: int):
    self.first_name = first_name
    self.last_name = last_name
    self.avg_score = avg_score
    self.races = races


  def __str__(self) -> str:
    return f'{self.first_name} {self.last_name} average-{self.avg_score} races{self.races}'
  
  