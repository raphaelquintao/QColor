import sublime
import sublime_plugin
import os
import subprocess
from datetime import datetime
from .lib.qutils import QColorUtils

# GLOBALS
APPNAME = "QColor"
VERSION = "1.0.9"
SETTINGSFILE = "QColor.sublime-settings"
CONF_KEY = "q_color"
FOUND_WEBVIEW = False
SETTINGS = lambda: sublime.load_settings(SETTINGSFILE)
DEBUG = lambda: sublime.load_settings(SETTINGSFILE).get("_debug", False)
ENABLED = lambda: sublime.load_settings(SETTINGSFILE).get("_enabled", False)

# LIBS
directory = os.path.dirname(os.path.realpath(__file__))
libdir = os.path.join(directory, 'lib')
if sublime.platform() == 'osx':
    binpath = os.path.join(libdir, 'picker.py')
elif sublime.platform() == 'linux':
    binpath = os.path.join(libdir, 'picker.py')
elif sublime.platform() == 'windows':
    binpath = os.path.join(libdir, 'picker.py')
else:
    binpath = os.path.join(libdir, 'picker.py')

# WARN IF DEBUG ENABLED
if DEBUG():
    print("DEBUG MODE!")


def check_deps():
    test_bin = os.path.join(libdir, 'test.py')
    # if sublime.platform() == 'osx' or sublime.platform() == 'linux':
    #     if not os.access(test_bin, os.X_OK):
    #         os.chmod(test_bin, 0o755)
    args = [os.path.join(sublime.packages_path(), test_bin)]
    if sublime.platform() == 'windows':
        args = ['pythonw', args[0]]
    elif sublime.platform() == 'osx' or sublime.platform() == 'linux':
        args = ['python3', args[0]]
    if DEBUG(): print("Args:", args)
    proc = subprocess.Popen(args, stdout=subprocess.PIPE)
    msg = proc.communicate()[0].strip()
    msg = msg.decode('utf-8')
    # print(msg == "true")
    if msg == "true": return True
    else: return False


def plugin_loaded():
    global FOUND_WEBVIEW
    if sublime.platform() == 'osx' or sublime.platform() == 'linux':
        binfile = os.path.join(sublime.packages_path(), binpath)
        if os.path.isfile(binfile):
            # print("BINFILE:", binfile)
            # if not os.access(binfile, os.X_OK):
            #     os.chmod(binfile, 0o755)
            pass
        else:
            print("BINFILE Not Found:", binfile)
        # print(check_deps())
    if check_deps():
        FOUND_WEBVIEW = True
    else:
        FOUND_WEBVIEW = False
    if not FOUND_WEBVIEW:
        print("WEBVIEW NOT FOUND: please run pip3 install pywebview")


# -----------------------
# HTML for Phantom
# -----------------------

def GenPhantomHTML(color, href, phantom_shape='circle'):
    style = """
        *       {{ background-color:transparent; border-width:0; margin:0; padding:0; }}
        html    {{ background-color:transparent;  }}
        body    {{ font-size: inherit; border-color: inherit; display:block; line-height: 1em; }}
        .circle {{ border-radius: 0.5em; }}
        a       {{ border: 0.05rem solid; border-color: color({0} l(+90%) s(0%) a(0.15));
                     border-radius: 0.0em; display:block; text-decoration:none; padding:-0px;
                     width: 0.95rem; height:0.95rem; margin-top: 0.01rem; background-color:{0}; }}
        img     {{ width: inherit; height: inherit; display:inline; position: relative; }}
    """
    content = '<a class="{1}" href="{0}"><img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="></a>'  # noqa
    html = '<body id="qcolor_phantom"><style>{0}</style>{1}</body>'
    clsname = phantom_shape.lower()
    return html.format(style.format(color), content.format(href, clsname))


def GenPopupHTML(color, colors, reg):
    global FOUND_WEBVIEW
    lines = ""
    for c in colors:
        lines += '<div class="line"><a class="color" href="r:{1}:{0}">{0}</a> <a class="copy" href="copy:{1}:{0}">Copy</a></div>'.format(c, reg)  # noqa
    png_trans = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="  # noqa
    png_green = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAYAAAAfFcSJAAAADUlEQVR42mNk+M9QDwADhgGAWjR9awAAAABJRU5ErkJggg=="  # noqa
    title = '<div class="title">QColor</div>'
    if FOUND_WEBVIEW:
        picker = '<a class="picker" href="{0}:{1}:">Customize</a>'.format('pick', reg)
    else:
        picker = '<span class="error">please run pip3 install pywebview</span>'
    preview = '<div class="preview"><img src="{0}"></div>'.format(png_trans)
    header = '<div class="header hl">{0} {1} {2}</div>'.format(preview, title, picker)
    stitle = '<div class="stitle">Convert to:</div>'
    content = '<div class="content">{0}{1}</div>'.format(stitle, lines)
    style = """
        html     { --margin:0.5em;
                   --background: hsla(210, 4%, 13%, 1);
                   --background: hsla(220, 13%, 14%, 1);
                   --foreground: hsla(215, 7%, 55%, 1);
                   --border: color(var(--background) l(50%) a(0.18));
                   --border-link: color(var(--foreground) a(0.5));
                   --bg-hl: color(var(--background) l(-50%) a(0.3));
                   color:var(--foreground); background-color: var(--background);
                   border: 1px solid var(--border); border-radius: 0px; }
        body     { font-family: monospace; font-size: 1rem; padding: 0; margin:0;  border-radius: inherit; }
        a        { text-decoration:none; font-size: 1em; background-color: color(red a(0.0)); color:var(--foreground); }
        img      { display: inline; position: relative; width: 1em; height: 0.8em;  line-height: 1em; }
        .title   { display: inline; position: relative; font-size: 1.2em; font-weight: bold;
                   background-color: color(cyan a(0.0)); line-height: 1em;
                   bottom: 0.15em; }
        .picker  { display: inline; position: relative; font-size: 1em;
                   background-color: color(black a(0.0)); padding: 0.0em;
                   bottom: 0.25em; line-height: 1em; border-bottom: 1px solid var(--border-link); }
        .preview { display: inline; position: relative; font-size: 1.8em; font-family: Helvetica;
                   padding: 0em 0 0 0; margin: 0 0 0 0; line-height: 1em;
                   background-color: color(red a(0.5));
                   border: 1px solid var(--border); }
        .error   { display: inline; position: relative; padding: 0.0em; bottom: 0.25em;
                   font-size: 1.0em; line-height: 1em; font-weight: bold; color:red; }
        .stitle  { font-size: 1.0em; line-height: 1em; font-weight: bold; margin-bottom: 0.4em; }
        .line    { font-size: 1.0em; line-height: 1em; margin: 0.3em var(--margin); }
        .color   { background-color: color(black a(0.0)); padding: 0.0em; border-bottom: 1px solid var(--border-link); }
        .copy    { position: relative; font-size: 0.7em; bottom:0.15em; color: color(var(--foreground) a(0.7));
                   background-color: var(--bg-hl); padding: 0.1em 0.2em; }
        .header  { display: block; padding: var(--margin); margin: 0.0em 0.0em 0.0em 0.0em;
                   border-top-left-radius: inherit; border-top-right-radius: inherit; }
        .content { display: block; padding: var(--margin); margin: 0.0em 0.0em 0.0em;
                   background-color: color(hotpink a(0.00));
                   border-bottom-left-radius: inherit; border-bottom-right-radius: inherit; }
        .hl      { background-color: var(--bg-hl); }
    """
    style2 = '.preview {{ background-color: {0};}}'.format(color)
    html = '<body id="qcolor_popup"><style>{0}</style>{1}{2}</body>'.format(style + style2, header, content)
    return html


def popup_navigate(view, arg):
    (cmd, reg, value) = arg.split(':')
    if DEBUG(): print(cmd, reg, value)
    if cmd == 'r':
        view.run_command("q_color_converter", {"reg": reg, "mode": "r", "value": value})
    elif cmd == 'pick':
        view.run_command("q_color_picker", {"reg": reg})
    elif cmd == 'copy':
        sublime.set_clipboard(value)
        sublime.status_message('Color copied to clipboard')


def popup_show(view, reg):
    if not isinstance(reg, sublime.Region):
        reg = (lambda t: sublime.Region(t[0], t[1]))(eval(reg))
    color = view.substr(reg).strip()
    colors = QColorUtils().parse(color).getAll()
    view.show_popup(GenPopupHTML(color, colors, reg),
        sublime.COOPERATE_WITH_AUTO_COMPLETE,
        # sublime.HIDE_ON_MOUSE_MOVE |
        # sublime.HIDE_ON_MOUSE_MOVE_AWAY,
        location=reg.end(),
        max_width=1024,
        max_height=1024,
        # on_hide = lambda: print("HIDE POPUP"),
        on_navigate=lambda x: popup_navigate(view, x))
    

class QPicker(object):

    def pick(self, window, start_color):
        if DEBUG(): print("STARTCOLOR", start_color)
        ncolor = ''
        if sublime.platform() == 'osx' or sublime.platform() == 'linux' or sublime.platform() == 'windows':
            args = [os.path.join(sublime.packages_path(), binpath)]
            if sublime.platform() == 'windows':
                args = ['pythonw', args[0]]
            elif sublime.platform() == 'osx' or sublime.platform() == 'linux':
                args = ['python3', args[0]]
            if start_color: args.append(start_color)
            proc = subprocess.Popen(args, stdout=subprocess.PIPE)
            color = proc.communicate()[0].strip()
            if DEBUG(): print("RAW", color)
            ncolor = color.decode('utf-8')
        else:
            print("PLATAFORM NOT SUPPORTED")
        return ncolor

        
class QColor(sublime_plugin.ViewEventListener):
    enabled = False
    key_conf = CONF_KEY
    key_ctrl = 'phantoms_enabled'

    def __init__(self, view):
        self.view = view
        self.view.QColor = self
        self.set_conf_change()
        self.on_conf_change()

    def settings(self):
        return sublime.load_settings(SETTINGSFILE)

    def isEnabled(self):
        """ Returns True if the full plugin is enabled. """
        if not ENABLED(): return False
        return self.settings().get(self.key_ctrl, False)
    
    def start(self):
        # Load Settings
        self.enabled = SETTINGS().get('enabled', False)
        self.phantom_shape = self.settings().get('phantom_shape', 'circle')
        self.show_on_minimap = self.settings().get('show_on_minimap', True)
        self.underline_style = self.settings().get('underline_style', 'stippled')
        self.underline_color = self.settings().get('underline_color', 'purple')
        self.hover_preview = self.settings().get('hover_preview', False)
        # Util settings
        named_colors = self.settings().get('named_colors', False)
        hsl_precision = self.settings().get('hsl_precision', True)
        hex_upper = self.settings().get('hex_upper_case', False)
        QColorUtils.set_conf(hsl_precision, hex_upper, named_colors)
        # Restart Binds
        self.pset = sublime.PhantomSet(self.view, self.key_conf)
        self.set_view_change()
        self.on_view_change()

    # File Conf Handlers

    def on_conf_change(self):
        # print("QColor", "on_conf_change")
        self.start()

    def set_conf_change(self):
        # print("QColor", "set_conf_change")
        self.clear_conf_change()
        key_id = "{0}_{1}".format(self.key_conf, self.view.id())
        self.settings().add_on_change(key_id, self.on_conf_change)

    def clear_conf_change(self):
        # print("QColor", "clear_conf_change")
        key_id = "{0}_{1}".format(self.key_conf, self.view.id())
        self.settings().clear_on_change(key_id)

    # View Conf Handlers

    def on_view_change(self):
        # print("QColor", "on_view_change")
        self.show_phantoms()

    def set_view_change(self):
        self.clear_view_change()
        key_id = "{0}_{1}".format(self.key_conf, self.view.id())
        self.view.settings().add_on_change(key_id, self.on_view_change)

    def clear_view_change(self):
        key_id = "{0}_{1}".format(self.key_conf, self.view.id())
        self.view.settings().clear_on_change(key_id)

    # Functions

    def getColorRegions(view):
        c_regions = []
        for key, value in QColorUtils.regex.items():
            c_regions += view.find_all(value, sublime.IGNORECASE)
        return c_regions

    def phantom_navigate(view, reg):
        popup_show(view, reg)

    def phantom_show(self, view, reg):
        selected = view.substr(reg).strip()
        view.add_phantom(self.key_conf,
            sublime.Region(reg.b, reg.b),
            GenPhantomHTML(selected, reg, self.phantom_shape),
            sublime.LAYOUT_INLINE,
            on_navigate=lambda x: QColor.phantom_navigate(self.view, x))

    def show_phantoms(self, only_regions=False):
        self.view.erase_regions(self.key_conf)
        self.view.erase_phantoms(self.key_conf)
        if not self.isEnabled():
            return False
        c_regions = QColor.getColorRegions(self.view)
        underline_color = self.get_region_underline_color()
        flags = self.get_region_flags()
        self.view.add_regions(self.key_conf, c_regions, underline_color, '', flags)
        if not only_regions:
            for reg in c_regions:
                self.phantom_show(self.view, reg)

    def get_region_underline_color(self):
        if self.underline_color == 'red': return 'region.redish'
        if self.underline_color == 'orange': return 'region.orangish'
        if self.underline_color == 'yellow': return 'region.yellowish'
        if self.underline_color == 'green': return 'region.greenish'
        if self.underline_color == 'blue': return 'region.bluish'
        if self.underline_color == 'pink': return 'region.pinkish'
        if self.underline_color == 'black': return 'region.blackish'
        return 'region.purplish'  # Defualt purple

    def get_region_flags(self):
        # Make sure the underline style is one we understand
        style = self.underline_style.lower()
        flags = sublime.DRAW_NO_FILL      # Disable filling the regions, leaving only the outline.
        flags |= sublime.DRAW_NO_OUTLINE  # Disable drawing the outline of the regions.
        # flags |= sublime.PERSISTENT       # Save the regions in the session.
        flags |= sublime.DRAW_SOLID_UNDERLINE if style == 'solid' else 0
        flags |= sublime.DRAW_STIPPLED_UNDERLINE if style == 'stippled' else 0
        flags |= sublime.HIDE_ON_MINIMAP if not self.show_on_minimap else 0
        return flags

    def find_region(self, position):
        regions = self.view.get_regions(self.key_conf)
        for creg in regions:
            if creg.contains(position):
                return True, creg
        return False, None

    # Events

    def on_modified(self):
        if DEBUG():
            print('on_modified')
        self.show_phantoms(self.hover_preview)

    def on_load(self):
        if DEBUG():
            print('on_load')
        self.show_phantoms(self.hover_preview)

    def on_hover(self, point, hover_zone):
        if self.hover_preview:
            in_region, region = self.find_region(point)
            if in_region:
                # print(point, hover_zone)
                # popup_show(self.view, region)
                self.view.erase_phantoms(self.key_conf)
                self.phantom_show(self.view, region)
            else: self.view.erase_phantoms(self.key_conf)

    def on_text_command(self, p1, cmd):
        # if self.isEnabled():
        #     print("text cmd", p1, cmd)
        pass


# -----------------------
# Commands
# -----------------------

class QColorVersion(sublime_plugin.ApplicationCommand):
    
    def time(self):
        return datetime.now().strftime("%H:%M:%S")

    def get_msg(self):
        return "{0} {1}".format(APPNAME,VERSION)

    def run(self):
        for win in sublime.windows():
            win.status_message(self.get_msg())

    def description(self):
        return self.get_msg()

    def is_enabled(self):
        return False


class QColorDebug(sublime_plugin.ApplicationCommand):
    key_conf = CONF_KEY
    key_ctrl = '_debug'

    def settings(self):
        return sublime.load_settings(SETTINGSFILE)

    def run(self, toggle=True):
        if toggle:
            value = self.settings().get(self.key_ctrl, False)
            self.settings().set(self.key_ctrl, not value)
            sublime.save_settings(SETTINGSFILE)

    def is_checked(self):
        return self.settings().get(self.key_ctrl, False)


class QColorEnabled(sublime_plugin.ApplicationCommand):
    key_conf = CONF_KEY
    key_ctrl = '_enabled'

    def settings(self):
        return sublime.load_settings(SETTINGSFILE)

    def run(self, toggle=True):
        if toggle:
            value = self.settings().get(self.key_ctrl, False)
            self.settings().set(self.key_ctrl, not value)
            sublime.save_settings(SETTINGSFILE)

    def description(self):
        return ""

    def is_checked(self):
        return self.settings().get(self.key_ctrl, False)


class QColorShow(sublime_plugin.ApplicationCommand):
    key_conf = CONF_KEY
    key_ctrl = 'phantoms_enabled'

    def settings(self):
        return sublime.load_settings(SETTINGSFILE)

    def active_view(self):
        return sublime.active_window().active_view()

    def run(self, show=None):
        value = self.settings().get(self.key_ctrl, False)
        newvalue = show if show is not None else not value
        self.settings().set(self.key_ctrl, newvalue)
        sublime.save_settings(SETTINGSFILE)

    def description(self):
        return ""
        
    def is_checked(self):
        return self.settings().get(self.key_ctrl, False)

    def is_enabled(self):
        return ENABLED()

    def is_visible(self):
        return True


class QColorConverter(sublime_plugin.TextCommand):

    def in_region(self, reg = None):
        sel = self.view.sel()
        if reg:
            reg = (lambda t: sublime.Region(t[0], t[1]))(eval(reg))
        else: reg = sel[0]
        return self.find_region(reg)

    def find_region(self, position):
        # regions = QColor.getColorRegions(self.view)
        regions = self.view.get_regions(CONF_KEY)
        for creg in regions:
            if creg.contains(position):
                return True, creg
        return False, None

    def run(self, edit, reg = None, mode = None, value = None):
        if DEBUG(): print("QColor Converter")
        (in_region, region) = self.in_region(reg)
        if not in_region: return
        if DEBUG(): print("in region")
        if mode in [None, "open", "hex"]:
            popup_show(self.view, region)
        elif mode == 'r':
            self.view.replace(edit, region, value)
            # if self.view.is_popup_visible():
            #     tmp=sublime.Region(region.begin())
            (in_reg, nreg) = self.find_region(sublime.Region(region.begin()))
            if(in_reg):
                if DEBUG(): print("nreg", nreg)
                popup_show(self.view, nreg)

    def description(self):
        return ""

    def is_enabled(self, reg = None, mode = None, value = None):
        (in_region, region) = self.in_region(reg)
        return ENABLED() and in_region

    def is_visible(self):
        return True


class QColorPicker(sublime_plugin.TextCommand):

    def run(self, edit, reg = None):
        # print("QColor Picker")
        sel = self.view.sel()
        region = sel[0]
        if reg:
            tmp = eval(reg)
            region = sublime.Region(tmp[0], tmp[1])
            
        else:
            regions = QColor.getColorRegions(self.view)
            for creg in regions:
                if creg.contains(sel[0]):
                    region = creg
                    break
        if region is not None:
            color = self.view.substr(region).strip()
            converter = QColorUtils().parse(color)
            in_mode = converter.in_mode or "rgba"
            color = converter.getRGB()
            # print(color, in_mode)
            # return
            ncolor = QPicker().pick(self.view.window(), color)
            if ncolor:
                sel.clear()
                sel.add(region)
                ncolor = converter.parse(ncolor).get(in_mode)
                # print("NEW COLOR", ncolor)
                self.view.replace(edit, region, ncolor)

    def is_enabled(self):
        binfile = os.path.join(sublime.packages_path(), binpath)
        return ENABLED() and os.path.isfile(binfile)

    def is_visible(self):
        return True
