#!/usr/bin/python

import sys, time
from AppKit import NSWorkspace

class TimeTracker:
    
    # API
    def track(self):
        while True:
            print(time.time())
            self.__instances.append((int(time.time()), self.__get_current_app_name()))
            print(self.__instances)
            time.sleep(self.__interval)

    # Private methods
    def __init__(self, interval = 1):
        self.__instances = []
        self.__interval = 1
    
    def __get_current_app_name(self):
        current_app = NSWorkspace.sharedWorkspace().activeApplication()
        return current_app['NSApplicationName']


def main(argv):
    time_tracker = TimeTracker()
    time_tracker.track()

if __name__ == "__main__":
    main(sys.argv)

