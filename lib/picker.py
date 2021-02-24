#!/usr/bin/env python3

import threading
import time
import sys
import random
import webview


resp = ""
color = "#ff9900"
toprint = False

param = ''

if len(sys.argv) > 1:
    param = sys.argv[1]
    # current_color.parse(param)

resp = param
color = param

class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def init(self):
        response = {
            'message': 'Hello from Python {0}'.format(sys.version)
        }
        return response

    def getRandomNumber(self):
        response = {
            'message': 'Here is a random number courtesy of randint: {0}'.format(random.randint(0, 100000000))
        }
        return response

    def doHeavyStuff(self):
        time.sleep(0.1)  # sleep to prevent from the ui thread from freezing for a moment
        now = time.time()
        self.cancel_heavy_stuff_flag = False
        for i in range(0, 1000000):
            _ = i * random.randint(0, 1000)
            if self.cancel_heavy_stuff_flag:
                response = {'message': 'Operation cancelled'}
                break
        else:
            then = time.time()
            response = {
                'message': 'Operation took {0:.1f} seconds on the thread {1}'.format((then - now), threading.current_thread())
            }
        return response

    def cancelHeavyStuff(self):
        time.sleep(0.1)
        self.cancel_heavy_stuff_flag = True

    def showColor(self, name):
        global resp

        response = {
            'message': '{0}'.format(name)
        }
        resp = name
        # print(name)
        return response

    def getTitle(self, name):
        global resp, color

        response = {
            'message': '{0}'.format(color)
        }
        return response

    def closeWindow(self, to_print = False):
        global toprint, color, resp
        # print("close")
        toprint = to_print;
        
        if to_print:
           print(resp)

        window.destroy()

    def error(self):
        raise Exception('This is a Python exception')


def on_closing():
    # global toprint, color, resp
    # if (not (resp == color)) and toprint:
    #    print(resp)
    pass

def change_url(window):
    # wait a few seconds before changing url:
    # time.sleep(10)

    # change url:
    window.load_url('web/picker.html')
    pass

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('QPicker', 
                                   url="web/picker.html", 
                                   js_api=api, 
                                   frameless= False,
                                   background_color='#FF9900',
                                   width=338,
                                   height=420,
                                   easy_drag = False,
                                   )
    # window = webview.create_window('QPicker', html=html, js_api=api)
    # window.load_url('web/picker.html')
    window.closing += on_closing
    # webview.start(change_url, window)    
    webview.start()
