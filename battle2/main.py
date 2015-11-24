

from battle2.model import GameEngine
from battle2.view import GraphicalView
from battle2.controller import HumanInput
import battle2.eventmanager as evm


def run():
    ev_manager = evm.EventManager()

    model = GameEngine(ev_manager)
    controller = HumanInput(ev_manager, model)
    view = GraphicalView(ev_manager, model)
    model.run()

if __name__ == '__main__':
    run()
