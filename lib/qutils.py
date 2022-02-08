import re

class QColorUtils(object):    
    r = 0
    g = 0
    b = 0
    a = 1
    alpha = False
    in_mode = ""

    hsl_precision = 3
    hex_upper = True
    named_colors = False


    svg_colors = {
        "aliceblue": "F0F8FF",
        "antiquewhite": "FAEBD7",
        "aqua": "00FFFF",
        "aquamarine": "7FFFD4",
        "azure": "F0FFFF",
        "beige": "F5F5DC",
        "bisque": "FFE4C4",
        "black": "000000",
        "blanchedalmond": "FFEBCD",
        "blue": "0000FF",
        "blueviolet": "8A2BE2",
        "brown": "A52A2A",
        "burlywood": "DEB887",
        "cadetblue": "5F9EA0",
        "chartreuse": "7FFF00",
        "chocolate": "D2691E",
        "coral": "FF7F50",
        "cornflowerblue": "6495ED",
        "cornsilk": "FFF8DC",
        "crimson": "DC143C",
        "cyan": "00FFFF",
        "darkblue": "00008B",
        "darkcyan": "008B8B",
        "darkgoldenrod": "B8860B",
        "darkgray": "A9A9A9",
        "darkgreen": "006400",
        "darkgrey": "A9A9A9",
        "darkkhaki": "BDB76B",
        "darkmagenta": "8B008B",
        "darkolivegreen": "556B2F",
        "darkorange": "FF8C00",
        "darkorchid": "9932CC",
        "darkred": "8B0000",
        "darksalmon": "E9967A",
        "darkseagreen": "8FBC8F",
        "darkslateblue": "483D8B",
        "darkslategray": "2F4F4F",
        "darkslategrey": "2F4F4F",
        "darkturquoise": "00CED1",
        "darkviolet": "9400D3",
        "deeppink": "FF1493",
        "deepskyblue": "00BFFF",
        "dimgray": "696969",
        "dimgrey": "696969",
        "dodgerblue": "1E90FF",
        "firebrick": "B22222",
        "floralwhite": "FFFAF0",
        "forestgreen": "228B22",
        "fuchsia": "FF00FF",
        "gainsboro": "DCDCDC",
        "ghostwhite": "F8F8FF",
        "gold": "FFD700",
        "goldenrod": "DAA520",
        "gray": "808080",
        "green": "008000",
        "greenyellow": "ADFF2F",
        "grey": "808080",
        "honeydew": "F0FFF0",
        "hotpink": "FF69B4",
        "indianred": "CD5C5C",
        "indigo": "4B0082",
        "ivory": "FFFFF0",
        "khaki": "F0E68C",
        "lavender": "E6E6FA",
        "lavenderblush": "FFF0F5",
        "lawngreen": "7CFC00",
        "lemonchiffon": "FFFACD",
        "lightblue": "ADD8E6",
        "lightcoral": "F08080",
        "lightcyan": "E0FFFF",
        "lightgoldenrodyellow": "FAFAD2",
        "lightgray": "D3D3D3",
        "lightgreen": "90EE90",
        "lightgrey": "D3D3D3",
        "lightpink": "FFB6C1",
        "lightsalmon": "FFA07A",
        "lightseagreen": "20B2AA",
        "lightskyblue": "87CEFA",
        "lightslategray": "778899",
        "lightslategrey": "778899",
        "lightsteelblue": "B0C4DE",
        "lightyellow": "FFFFE0",
        "lime": "00FF00",
        "limegreen": "32CD32",
        "linen": "FAF0E6",
        "magenta": "FF00FF",
        "maroon": "800000",
        "mediumaquamarine": "66CDAA",
        "mediumblue": "0000CD",
        "mediumorchid": "BA55D3",
        "mediumpurple": "9370DB",
        "mediumseagreen": "3CB371",
        "mediumslateblue": "7B68EE",
        "mediumspringgreen": "00FA9A",
        "mediumturquoise": "48D1CC",
        "mediumvioletred": "C71585",
        "midnightblue": "191970",
        "mintcream": "F5FFFA",
        "mistyrose": "FFE4E1",
        "moccasin": "FFE4B5",
        "navajowhite": "FFDEAD",
        "navy": "000080",
        "oldlace": "FDF5E6",
        "olive": "808000",
        "olivedrab": "6B8E23",
        "orange": "FFA500",
        "orangered": "FF4500",
        "orchid": "DA70D6",
        "palegoldenrod": "EEE8AA",
        "palegreen": "98FB98",
        "paleturquoise": "AFEEEE",
        "palevioletred": "DB7093",
        "papayawhip": "FFEFD5",
        "peachpuff": "FFDAB9",
        "peru": "CD853F",
        "pink": "FFC0CB",
        "plum": "DDA0DD",
        "powderblue": "B0E0E6",
        "purple": "800080",
        "red": "FF0000",
        "rebeccapurple": "663399",
        "rosybrown": "BC8F8F",
        "royalblue": "4169E1",
        "saddlebrown": "8B4513",
        "salmon": "FA8072",
        "sandybrown": "F4A460",
        "seagreen": "2E8B57",
        "seashell": "FFF5EE",
        "sienna": "A0522D",
        "silver": "C0C0C0",
        "skyblue": "87CEEB",
        "slateblue": "6A5ACD",
        "slategray": "708090",
        "slategrey": "708090",
        "snow": "FFFAFA",
        "springgreen": "00FF7F",
        "steelblue": "4682B4",
        "tan": "D2B48C",
        "teal": "008080",
        "thistle": "D8BFD8",
        "tomato": "FF6347",
        "turquoise": "40E0D0",
        "violet": "EE82EE",
        "wheat": "F5DEB3",
        "white": "FFFFFF",
        "whitesmoke": "F5F5F5",
        "yellow": "FFFF00",
        "yellowgreen": "9ACD32"
    }

    regex = {
        "hex": r"\#([a-fA-F0-9]{8}|[a-fA-F0-9]{6}|[a-fA-F0-9]{3})\b",
        "rgb" : r"rgb\s*?\(\s*?(000|0?\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\s*?,\s*?(000|0?\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\s*?,\s*?(000|0?\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\s*?\)",
        "rgba" : r"rgba\s*?\(\s*?(000|0?\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\s*?,\s*?(000|0?\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\s*?,\s*?(000|0?\d{1,2}|1\d\d|2[0-4]\d|25[0-5])\s*?,\s*?(0|0*\.\d+|1|1.0*)\s*?\)",
        "hsl": r"hsl\s*?\(\s*?((?:000|0?\d{1,2}|[1-2]\d\d|3[0-5]\d|360)(?:\.\d*)?)\s*?,\s*?((?:000|100|0?\d{2}|0?0?\d)(?:\.\d*)?)%\s*?,\s*?((?:000|100|0?\d{2}|0?0?\d)(?:\.\d*)?)%\s*?\)",
        "hsla": r"hsla\s*?\(\s*?((?:000|0?\d{1,2}|[1-2]\d\d|3[0-5]\d|360)(?:\.\d*)?)\s*?,\s*?((?:000|100|0?\d{2}|0?0?\d)(?:\.\d*)?)%\s*?,\s*?((?:000|100|0?\d{2}|0?0?\d)(?:\.\d*)?)%\s*?,\s*?(0|0*\.\d+|1|1.0*)\s*?\)",
    }
    


    # Static Functions
    def set_conf(hsl_float = False, hex_upper_case = False, named_color = False):
        QColorUtils.hsl_precision =  3 if hsl_float else 0
        QColorUtils.hex_upper =  True if hex_upper_case else False
        QColorUtils.named_colors =  True if named_color else False
        if QColorUtils.named_colors:
            QColorUtils.regex.update({"named": r"\b(" + "|".join(list(QColorUtils.svg_colors.keys())) + r")\b"})
        
    def rgb_to_hsl(r, g, b, normalized = False):
        if not normalized:
            (r, g, b) = r / 255.0, g / 255.0, b / 255.0

        (r, g, b) = float(r), float(g), float(b)
        high = max(r, g, b)
        low = min(r, g, b)
        h = s = l = (high + low) / 2.0

        if high == low:
            h = s = 0.0
        else:
            d = high - low
            
            s = d / (2.0 - high - low) if l > 0.5 else d / (high + low)
            
            h = {
                r: (g - b) / d + (6.0 if g < b else 0),
                g: (b - r) / d + 2.0,
                b: (r - g) / d + 4.0,
            }[high]
            h /= 6.0

        if not normalized:
            (h, s, l) = h * 360, s * 100, l * 100

        return h, s, l

    def hsl_to_rgb(h, s, l, normalized = False):
        if not normalized:
            (h, s, l) = h / 360.0, s / 100.0, l / 100.0

        def hue_to_rgb(p, q, t):
            if t < 0: t += 1
            if t > 1: t -= 1 
            if t < 1/6.0: return p + (q - p) * 6.0 * t
            if t < 1/2.0: return q
            if t < 2/3.0: return p + (q - p) * (2/3.0 - t) * 6.0
            return p

        if s == 0:
            r, g, b = l, l, l
        else:
            q = l * (1 + s) if l < 0.5 else l + s - l * s
            p = 2 * l - q
            r = hue_to_rgb(p, q, h + 1/3.0)
            g = hue_to_rgb(p, q, h)
            b = hue_to_rgb(p, q, h - 1/3.0)
        
        if not normalized: 
            (r, g, b) = r * 255, g * 255, b * 255

        return r, g, b



    

    def __init__(self):
        pass
            

    # Parse Function

    def parse(self, color):
        regex_hex = self.regex["hex"]
        regex_rgb = self.regex["rgb"]
        regex_rgba = self.regex["rgba"]
        regex_hsl = self.regex["hsl"]
        regex_hsla = self.regex["hsla"]
        
        (self.r, self.g, self.b, self.a) = 0, 0, 0, 1

        color = color.strip().lower()

        if color in self.svg_colors.keys():
            color='#'+ self.svg_colors[color].lower()

        if color.startswith('#'):
            match = re.search(regex_hex, color, re.IGNORECASE)
            if(match):
                value = match.group(1)
                
                if len(value) == 3:
                    (self.r, self.g, self.b) = int(value[0:1] + value[0:1], 16), int(value[1:2] + value[1:2], 16), int(value[2:3] + value[2:3], 16)
                    # self.a = int(value[6:8], 16) / 255

                    self.alpha = True
                elif len(value) == 8:
                    (self.r, self.g, self.b) = int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)
                    self.a = int(value[6:8], 16) / 255
                    self.alpha = True
                else:
                    (self.r, self.g, self.b) = int(value[0:2], 16), int(value[2:4], 16), int(value[4:6], 16)
            self.in_mode = 'hex'
            
        elif color.startswith('rgba'):
            match = re.search(regex_rgba, color, re.IGNORECASE)
            if(match):
                (self.r, self.g, self.b, self.a) = int(match.group(1)), int(match.group(2)), int(match.group(3)), float(match.group(4))
                self.alpha = True
            self.in_mode = 'rgba'
        elif color.startswith('rgb'):
            match = re.search(regex_rgb, color, re.IGNORECASE)
            if(match):
                (self.r, self.g, self.b) = int(match.group(1)), int(match.group(2)), int(match.group(3))
            self.in_mode = 'rgb'
        elif color.startswith('hsla'):
            match = re.search(regex_hsla, color, re.IGNORECASE)
            if(match):
                (self.r, self.g, self.b) = QColorUtils.hsl_to_rgb(float(match.group(1)), float(match.group(2)), float(match.group(3)))
                self.a = float(match.group(4))
                self.alpha = True
            self.in_mode = 'hsla'
        elif color.startswith('hsl'):
            match = re.search(regex_hsl, color, re.IGNORECASE)
            if(match):
                (self.r, self.g, self.b) = QColorUtils.hsl_to_rgb(float(match.group(1)), float(match.group(2)), float(match.group(3)))
            self.in_mode = 'hsl'
        return self

    # Get Functions

    def getHEX(self, alpha = False):
        resp = "#%02x%02x%02x" % (round(self.r), round(self.g), round(self.b))
        if (self.alpha and alpha) or (not self.alpha and alpha):
            resp += "%02x" % round(self.a * 255)
        return resp.upper() if self.hex_upper else resp.lower()

    def getRGBA(self):
        return "rgba({0:g}, {1:g}, {2:g}, {3:g})".format(round(self.r, 0), round(self.g, 0), round(self.b, 0), round(self.a, 3))

    def getRGB(self, alpha = True):        
        if self.alpha and alpha: return self.getRGBA()
        return "rgb({0:g}, {1:g}, {2:g})".format(round(self.r, 0), round(self.g, 0), round(self.b, 0))
    
    def getHSLA(self):
        (r, g, b) = QColorUtils.rgb_to_hsl(self.r, self.g, self.b)
        resp = "hsla({0:g}, {1:g}%, {2:g}%, {3:g})".format(round(r, self.hsl_precision), round(g, self.hsl_precision), round(b, self.hsl_precision), round(self.a, 3))
        return resp

    def getHSL(self, alpha = True):
        if self.alpha and alpha: return self.getHSLA()
        (r, g, b) = QColorUtils.rgb_to_hsl(self.r, self.g, self.b)
        resp = "hsl({0:g}, {1:g}%, {2:g}%)".format(round(r, self.hsl_precision), round(g, self.hsl_precision), round(b, self.hsl_precision))
        return resp

    def getNamed(self):
        hex = self.getHEX(False).upper().strip('#')
        for name, value in self.svg_colors.items():
            if value == hex: return name
        return ''

    def get(self, mode, alpha = False):
        if mode.lower() == 'hex': return self.getHEX(alpha)
        elif mode.lower() == 'rgb': return self.getRGB(alpha)
        elif mode.lower() == 'hsl': return self.getHSL(alpha)
        elif mode.lower() == 'hexa': return self.getHEX(alpha)
        elif mode.lower() == 'rgba': return self.getRGBA()
        elif mode.lower() == 'hsla': return self.getHSLA()
        else: return self.get(self.in_mode, alpha)

    def getAll(self):
        colors = [self.getHEX(False), self.getHEX(True), self.getRGB(False), self.getRGBA(), self.getHSL(False), self.getHSLA()]
        
        name = self.getNamed()
        if name: colors.insert(0, name)

        return colors

    def getAllNamed(self):
        colors = {}
        colors["hex"] =  self.getHEX(False)
        colors["hexa"] =  self.getHEX(True)
        colors["rgb"] =  self.getRGB(False)
        colors["rgba"] =  self.getRGBA()
        colors["hsl"] =  self.getHSL(False)
        colors["hsla"] =  self.getHSLA()

        name = self.getNamed()
        if name: colors["name"] =  name

        return colors




