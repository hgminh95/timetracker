#!/usr/bin/python

import sys, time
from AppKit import NSWorkspace

class TimeTracker:
    
    # Public methods
    def track(self):
        while True:
            print(time.time())
            self.__instances.append((self.__get_current_app_name(), int(time.time())))
            print(self.__create_app_list())
            time.sleep(self.__interval)

    # Private methods
    def __init__(self, interval = 1):
        self.__instances = []
        self.__interval = 1
    
    def __get_current_app_name(self):
        current_app = NSWorkspace.sharedWorkspace().activeApplication()
        return current_app['NSApplicationName']

    def __create_app_list(self):
        if not self.__instances:
            return {}
        else:
            app_list = {}
            cur_time = self.__instances[0][1]
            for (app, time) in self.__instances:
                if (app in app_list):
                    app_list[app] += (time - cur_time)
                else:
                    app_list[app] = 0
                cur_time = time
            return app_list


def main(argv):
    time_tracker = TimeTracker()
    time_tracker.track()

if __name__ == "__main__":
    main(sys.argv)

