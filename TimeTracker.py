#!/usr/bin/python

import os, datetime, sys, time
from AppKit import NSWorkspace

class TimeTracker:
    
    # Public methods
    def track(self):
        while True:
            self.__add_instace(self.__get_current_app_name(), int(time.time()))
            if (self.__total_time > 0):
                self.__pretty_format_app_list(self.__app_list, self.__total_time)
            else:
                print("Calculating...")
            time.sleep(self.__interval)

    # Private methods
    def __init__(self, interval = 1):
        self.__interval = interval
        self.__app_list = {}
        self.__total_time = 0
        self.__current_time = int(time.time())

    def __add_instace(self, app, time):
        time_delta = time - self.__current_time
        if (app in self.__app_list):
            self.__app_list[app] += time_delta
        else:
            self.__app_list[app] = time_delta
        self.__total_time += time_delta
        self.__current_time = time
    
    def __get_current_app_name(self):
        current_app = NSWorkspace.sharedWorkspace().activeApplication()
        return current_app['NSApplicationName']

    def __pretty_format_app_list(self, app_list, total_time):
        os.system('cls||clear')
        sorted_app_list = sorted(app_list.items(), key = lambda x: x[1], reverse = True)
        row_print_format = "|%2s|%20s|%15s|%8s|"
        sperate_row = '+' + '--' + '+' + '-'*20 + '+' + '-'*15 + '+' + '-'*8 + '+'

        print("Application time tracking")
        print(sperate_row)
        print(row_print_format % ("#", "Application", "Using time", "Percent"))
        print(sperate_row)
        for idx, (app, time) in enumerate(sorted_app_list):
            using_percent = "%.1f" % (time/total_time*100)
            print(row_print_format % (
                idx+1,
                app,
                str(datetime.timedelta(seconds = time)),
                using_percent
                ))
        print(sperate_row)


def main(argv):
    time_tracker = TimeTracker()
    time_tracker.track()

if __name__ == "__main__":
    main(sys.argv)

