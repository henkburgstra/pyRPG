
from battle2.eventmanager import *
from battle2.model import GameEngine
from battle2.view import GraphicalView
from battle2.controller import HumanInput


def run():
    ev_manager = EventManager()

    model = GameEngine(ev_manager)
    view = GraphicalView(ev_manager, model)
    controller = HumanInput(ev_manager, model)
    model.run()

if __name__ == '__main__':
    run()
