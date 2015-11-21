

from battle2.model import GameEngine
from battle2.view import GraphicalView
from battle2.controller import HumanInput
from battle2.eventmanager import *


def run():
    ev_manager = EventManager()

    model = GameEngine(ev_manager)
    controller = HumanInput(ev_manager, model)
    view = GraphicalView(ev_manager, model)
    model.run()

if __name__ == '__main__':
    run()
