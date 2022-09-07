def name():
    return "Raster"

def author
return "Hector Solares Hernandez"

def authorName():
    return author()

def email():
    return"solarez.hec@gmail.com"

def description():
    return "raster"

def about():
    return "Raster"

def category():
    return "Raster"

def version():
    return "0.0.1"

def qgisMinimumVersion():
    return "3.0"

def icon():
    return"icons/logo.png"

def classFactory(iface):
    from .main import mainMenu
    return mainMenu(iface)
