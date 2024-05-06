from simple_event_handler.simple_event_handler import SimpleEventHandler


def on_click():
    print("Button clicked!")


def on_click2():
    print("Button clicked again!")


event_handler = SimpleEventHandler()
event_handler.add_event("click", on_click)
event_handler.add_event("click", on_click2)
event_handler.add_event("click2", on_click2)

event_handler.trigger_event("click")
event_handler.trigger_event("click2")
