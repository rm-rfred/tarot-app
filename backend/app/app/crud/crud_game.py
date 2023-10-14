from fastapi import Depends


class CRUDGame():
    def __init__(self, nb_players: int) -> None:
        self.nb_players = nb_players

    def create(self):
        pass
