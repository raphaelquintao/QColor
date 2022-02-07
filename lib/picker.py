#!/usr/bin/env python3

import threading
import time
import sys
import random
import webview


resp = ""
color = "#ff0000"
toprint = False

param = ''

if len(sys.argv) > 1:
    param = sys.argv[1]
    # current_color.parse(param)

resp = param
color = param

# print("Start: ", color)

class Api:
    def __init__(self):
        self.cancel_heavy_stuff_flag = False

    def start(self):
        global color

        # print(color)
        response = {
            'data': '{0}'.format(color)
        }
        return response

    def showColor(self, color):
        global resp

        response = {
            'data': '{0}'.format(color)
        }
        resp = color
        return response


    def closeWindow(self, to_print = False):
        global toprint, color, resp
        toprint = to_print;
        
        if to_print: print(resp)

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

def get_file():
    f = open("web/picker.html", "r")
    return f.read()

if __name__ == '__main__':
    api = Api()
    window = webview.create_window('QPicker', 
                                   url="web/picker.html",
                                   js_api=api, 
                                   frameless=False,
                                   background_color='#333333',
                                   width=350,
                                   height=450,
                                   easy_drag = False,
                                   resizable=False
                                   )
    window.closing += on_closing
    webview.start(http_server=True)
