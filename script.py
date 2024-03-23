'''
  Problem: Evented-Thing
'''

import unittest

# Source Code of Evented-Thing

class EventedThing:
  def __init__(self) -> None:
    self.events = {} # storage hashmap for events

  def on(self, event: str, callback: callable) -> None:
    if event in self.events: # Check if event already exists
      self.events[event].append(callback) # Append callback to the event
    else:
      self.events[event] = [callback] # Create a new event with the callback

  def trigger(self, event: str, *args) -> None:
    if event in self.events: # Check if event exists
      for callback in self.events[event]: # Loop through all callbacks
        callback(*args) # Call the callback with arguments
  

# Test Cases

class TestEventedThing(unittest.TestCase):
  def test_on(self) -> None:
    event = EventedThing()
    def callback():
      print("Event Triggered!")
    event.on("click", callback)
    self.assertEqual(event.events, {"click": [callback]})

  def test_trigger(self) -> None:
    event = EventedThing()
    count = 0
    def callback():
      nonlocal count
      count += 1
    event.on("click", callback)
    event.trigger("click")
    print(count)
    self.assertEqual(count, 1)

  def test_meet_event(self):
    passed_args = []
    event = EventedThing()
        
    def callback(*args):
        nonlocal passed_args
        passed_args = list(args)
        
    event.on('meet', callback)
        
    # Triggering 'meet' event with one argument
    event.trigger('meet', 'arg1')
    self.assertEqual(passed_args, ['arg1'])
        
    # Triggering 'meet' event with two arguments
    event.trigger('meet', 'arg1', 'arg2')
    self.assertEqual(passed_args, ['arg1', 'arg2'])


if __name__ == "__main__":
  unittest.main()
