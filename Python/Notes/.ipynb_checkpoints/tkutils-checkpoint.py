
'''
this module includes some utils for tkinter scripts
'''


class mycolor:
    mycolors = ["#559999", "#ccffcc", "#ff99ff", "#33ccff"] 
    
    @staticmethod
    def hex_to_decimal(hex):
        '''
        hex: a string containing the hex repreresentation of a number
        return: a int which the decimal representation of the number
        '''
        value = 0;
        for hexdigit in hex:
            v = 0
            if ord(hexdigit) < 58:
                v = ord(hexdigit) - 48
            elif ord(hexdigit) < 96:
                v = ord(hexdigit) - 55
            else:
                v = ord(hexdigit) - 87
            value = value * 16 + v
        return value
    @staticmethod
    def hex_from_decimal(d):
        '''
        d: an int which the decimal representation of a number
        return: a string which is the hex representation of the number
        '''
        hex = ""
        while True:
            r = d % 16
            if r < 10:
                hex = str(r) + hex
            else:
                hex = chr(r + 87) + hex
            d = d // 16
            if d == 0:
                break
        return hex
                
    @staticmethod
    def get_rgb_from_hexstring(hexstring):
        '''
        hexstring: string which represents the color in the #rrggbb format
        return: r,g,b where r,g,b are the integer representation of the r,g,b values
        '''
        red, green, blue = mycolor.hex_to_decimal(hexstring[1:3]), mycolor.hex_to_decimal(hexstring[3:5]), mycolor.hex_to_decimal(hexstring[5:])
        return red, green, blue
    @staticmethod
    def get_hexstring_from_rgb(r, g, b):
        '''
        r,g,b: are integers that are the r,g,b values of a color
        return: a string which the #rrggbb repn of the color
        '''
        return "#" + ("0" if r < 16 else "") + mycolor.hex_from_decimal(r) + ("0" if g < 16 else "") + mycolor.hex_from_decimal(g) + ("0" if b < 16 else "") + mycolor.hex_from_decimal(b)
        
        
        
    @staticmethod
    def lighten(colorstring, factor = 0.5):
        '''
        colorstring: a string represents the base color in #rrggbb format
        factor: the factor by which to lighten
        return: string reprsenting the lightened color in #rrggbb format
        '''
        r, g, b = mycolor.get_rgb_from_hexstring(colorstring)
        r = int(factor * r + (1 - factor) * 255) % 256
        g = int(factor * g + (1 - factor) * 255) % 256
        b = int(factor * b + (1 - factor) * 255) % 256
        return mycolor.get_hexstring_from_rgb(r,g,b)
    
    @staticmethod
    def darken(colorstring, factor = 0.5):
        '''
        colorstring: a string represents the base color in #rrggbb format
        factor: the factor by which to darken
        return: string reprsenting the darkened color in #rrggbb format
        '''       
        r, g, b = mycolor.get_rgb_from_hexstring(colorstring)
        r = int(factor * r + (1 - factor) * 0) % 256
        g = int(factor * g + (1 - factor) * 0) % 256
        b = int(factor * b + (1 - factor) * 0) % 256
        return mycolor.get_hexstring_from_rgb(r,g,b)
        
class myfont:
    myfonts = [("Iosevka Comfy Motion", 40), ("Iosevka Comfy Motion", 25)]



    