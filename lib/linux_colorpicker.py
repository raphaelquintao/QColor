#!/usr/bin/env python3

import sys
import gi

gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from gi.repository import Gdk
from pprint import pprint


# print(sys.version)

color_sel = Gtk.ColorChooserDialog("QColor - Color Picker")
color_sel.set_use_alpha(True)
color_sel.show_editor = False


# colors = [Gdk.RGBA(0.5,0.5,0.5,0.5), Gdk.RGBA()]
# color_sel.add_palette(Gtk.Orientation.VERTICAL, 20, colors)


# color_sel.set_default_response(50)
# color_sel.response(50)
# color_sel.set_destroy_with_parent(False)



current_color = Gdk.RGBA()

param = ''

if len(sys.argv) > 1:
    param = sys.argv[1]
    # current_color.parse(param)
    if current_color.parse(param):
        color_sel.set_rgba(current_color)
        # color_sel.rgba = current_color

        

# if color_sel.run() == getattr(Gtk, 'RESPONSE_OK', Gtk.ResponseType.OK):


# btn = color_sel.add_button('None', Gtk.ResponseType.CLOSE)



# print(getattr(Gtk, 'RESPONSE_OK', Gtk.ResponseType.CLOSE))

def parse():
    color = color_sel.get_rgba()
    if param.startswith('rgba') or color.alpha < 1:
        print("rgba(%d, %d, %d, %.2f)" % (color.red * 255, color.green * 255, color.blue * 255, color.alpha))
    elif param.startswith('rgb') :
        print("rgb(%d, %d, %d)" % (color.red * 255, color.green * 255, color.blue * 255))
    else:
        red = int(color.red * 65535 / 256)
        green = int(color.green * 65535 / 256)
        blue = int(color.blue * 65535 / 256)
        str_hex = "%02x%02x%02x" % (red, green, blue)
        # if(color.alpha < 1): str_hex += "%02x" % (color.alpha * 65535 / 256)
        print("#" + str_hex.upper())
    color_sel.destroy()


def main():
    resp = color_sel.run()

    # print(resp)

    if resp == getattr(Gtk, 'RESPONSE_OK', Gtk.ResponseType.OK):
        parse()
    else: color_sel.destroy()


main()
