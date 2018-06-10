#!/usr/bin/python

import os, datetime, sys, time
from AppKit import NSWorkspace

class TimeTracker:
    
    # Public methods
    def track(self):
        while True:
            self._add_instace(self._get_current_app_name(), int(time.time()))
            if (self._total_time > 0):
                self._pretty_format_app_list(self._app_list, self._total_time)
            else:
                print("Calculating...")
            time.sleep(self._interval)

    # Private methods
    def __init__(self, interval = 1):
        self._interval = interval
        self._app_list = {}
        self._total_time = 0
        self._current_time = int(time.time())

    def _add_instace(self, app, time):
        time_delta = time - self._current_time
        if (app in self._app_list):
            self._app_list[app] += time_delta
        else:
            self._app_list[app] = time_delta
        self._total_time += time_delta
        self._current_time = time
    
    def _get_current_app_name(self):
        current_app = NSWorkspace.sharedWorkspace().activeApplication()
        return current_app['NSApplicationName']

    def _pretty_format_app_list(self, app_list, total_time):
        os.system('cls||clear')
        sorted_app_list = sorted(app_list.items(), key = lambda x: x[1], reverse = True)
        row_print_format = "|{:>2}|{:>20}|{:>15}|{:>8}|"
        sperate_row = '+' + '--' + '+' + '-'*20 + '+' + '-'*15 + '+' + '-'*8 + '+'

        print("Application time tracking")
        print(sperate_row)
        print(row_print_format.format("#", "Application", "Using time", "Percent"))
        print(sperate_row)
        for idx, (app, time) in enumerate(sorted_app_list):
            using_percent = "{:.1f}".format(time*1.0/total_time*100)
            print(row_print_format.format(
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

