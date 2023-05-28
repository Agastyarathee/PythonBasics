import sys
import time
import random
import os
import shutil
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from_dir = "C:/Users/AgasMsi/Downloads"

class FindEventHandler(FileSystemEventHandler):
    def on_created(self, event):
        return super().on_created(event)
    def on_modified(self, event):
        return super().on_modified(event)
    def on_deleted(self, event):
        print(f"hey")
    def on_moved(self, event):
        return super().on_moved(event)

event_handler = FindEventHandler()

# Initialize Observer
observer = Observer()

# Schedule the Observer
observer.schedule(event_handler, from_dir, recursive=True)

# Start the Observer
observer.start()

try:
    while True:
        time.sleep(2)
        print("running...")
except KeyboardInterrupt:
    print("stopped!")
    observer.stop()
