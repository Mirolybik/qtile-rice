from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from os import path

home = path.expanduser('~')
qconf = home + "/.config/qtile/"
getlayout = qconf + "/scripts/getlayout.sh"

class KbWidget(widget.TextBox):
    
    def update_self(self):
        layout = check_output([getlayout]).decode().strip()
        self.text = str(layout)
        self.draw()
    
    def __init__(self, **config):
        super().__init__("", **config)
        self.update_self()


