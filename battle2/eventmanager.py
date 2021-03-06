

class Event(object):
    """
    A superclass for any events that might be generated by an
    object and sent to the EventManager.
    """
    def __init__(self):
        self.name = "Generic event"

    def __str__(self):
        return self.name


class QuitEvent(Event):
    """
    Quit event.
    """
    def __init__(self):
        super().__init__()
        self.name = "Quit event"


class TickEvent(Event):
    """
    Tick event.
    """
    def __init__(self):
        super().__init__()
        self.name = "Tick event"


class InputEvent(Event):
    """
    Keyboard or mouse input event.
    """
    def __init__(self, key=None, clickpos=None, button=None):
        super().__init__()
        self.name = "Input event"
        self.key = key
        self.clickpos = clickpos
        self.button = button

    def __str__(self):
        return "{}, key={}, clickpos={}, button={}".format(self.name, self.key, self.clickpos, self.button)


class CharUpdateEvent(Event):
    """
    Character update event.
    """
    def __init__(self, last_dir=None, move_dir=None, movespeed=None):
        super().__init__()
        self.name = "Character update event"
        self.last_dir = last_dir
        self.move_dir = move_dir
        self.movespeed = movespeed


class InitializeEvent(Event):
    """
    Tells all listeners to initialize themselves.
    This includes loading libraries and resources.

    Avoid initializing such things within listener __init__ calls
    to minimize snafus (if some rely on others being yet created.)
    """
    def __init__(self):
        super().__init__()
        self.name = "Initialize event"


class InitMapEvent(Event):
    """
    Initialize map event.
    """
    def __init__(self):
        super().__init__()
        self.name = "Initialize map event"


class DrawMapEvent(Event):
    """
    Draw map event.
    """
    def __init__(self):
        super().__init__()
        self.name = "Draw map event"


class ChangeStateEvent(Event):
    """
    Change the model state machine.
    Given a None state will pop() instead of push.
    """
    def __init__(self, pushed_state, popped_state=""):
        super().__init__()
        self.name = "Change state event"
        self.new_state = pushed_state
        self.old_state = popped_state

    def __str__(self):
        if self.new_state:
            return "{} pushed {}".format(self.name, self.new_state)
        else:
            return "{} popped {}".format(self.name, self.old_state)


class EventManager(object):
    """
    We coordinate communication between the Model, View, and Controller.
    """
    def __init__(self):
        from weakref import WeakKeyDictionary
        self.listeners = WeakKeyDictionary()

    def register_listener(self, listener):
        """
        Adds a listener to our spam list.
        It will receive post()ed events through it's notify(event) call.
        """
        self.listeners[listener] = 1

    def unregister_listener(self, listener):
        """
        Remove a listener from our spam list.
        This is implemented but hardly used.
        Our weak ref spam list will auto remove any listeners who stop existing.
        """
        if listener in self.listeners.keys():
            del self.listeners[listener]

    def post(self, event):
        """
        Post a new event to the message queue.
        It will be broadcast to all listeners.
        """
        if not isinstance(event, TickEvent) and \
           not isinstance(event, CharUpdateEvent):
            print(str(event))                   # print the event (unless it is TickEvent)
        for listener in self.listeners.keys():
            listener.notify(event)
