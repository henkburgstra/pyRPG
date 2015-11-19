
from battle2.eventmanager import *
from battle2.model import GameEngine
from battle2.view import GraphicalView
from battle2.controller import HumanInput


def run():
    ev_manager = EventManager()
    gamemodel = GameEngine(ev_manager)
    h_input = HumanInput(ev_manager, gamemodel)
    graphics = GraphicalView(ev_manager, gamemodel)
    gamemodel.run()

if __name__ == '__main__':
    run()
