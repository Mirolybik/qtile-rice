from os import path
from subprocess import Popen, check_output
from libqtile import bar, layout, widget, hook
from libqtile.config import Click, Drag, Group, Key, Match, Screen
from libqtile.lazy import lazy
from libqtile.utils import guess_terminal
import wdg.kblwd

home = path.expanduser('~')
qconf = home + "/.config/qtile/"
scripts = qconf + "/scripts/"
pictures = qconf + "/pictures/"

mod = "mod4"

file_manager = "thunar"
browser = "firefox"
terminal = guess_terminal()
rr = scripts + "recordrofi"
volmute = scripts + "vol.sh mute"
volup = scripts + "vol.sh up"
voldown = scripts + "vol.sh down"
sstool = "flameshot gui"
rofi= home + "/.config/rofi/launchers/type-7/launcher.sh"

col_selected="#75bd75"
col_unselected="#333333"

city="Moscow"

autostart_sh = scripts + "autostart.sh"
getlayout = scripts + "getlayout.sh"

# Custom keyboard widget

#kbl = KbWidget()

@hook.subscribe.startup_once
def autostart():
    Popen([autostart_sh])

keys = [
    Key([mod], "h", lazy.layout.left(), desc="Move focus to left"),
    Key([mod], "l", lazy.layout.right(), desc="Move focus to right"),
    Key([mod], "j", lazy.layout.down(), desc="Move focus down"),
    Key([mod], "k", lazy.layout.up(), desc="Move focus up"),
    Key([mod], "space", lazy.layout.next(), desc="Move window focus to other window"),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left(), desc="Move window to the left"),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right(), desc="Move window to the right"),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down(), desc="Move window down"),
    Key([mod, "shift"], "k", lazy.layout.shuffle_up(), desc="Move window up"),
    Key([mod, "control"], "h", lazy.layout.grow_left(), desc="Grow window to the left"),
    Key([mod, "control"], "l", lazy.layout.grow_right(), desc="Grow window to the right"),
    Key([mod, "control"], "j", lazy.layout.grow_down(), desc="Grow window down"),
    Key([mod, "control"], "k", lazy.layout.grow_up(), desc="Grow window up"),
    Key([mod], "n", lazy.layout.normalize(), desc="Reset all window sizes"),
    Key([mod, "shift"], "Return", lazy.layout.toggle_split(),desc="Toggle between split and unsplit sides of stack"),
    Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
    Key([mod], "b", lazy.spawn(browser), desc="Launch browser"),
    Key([mod], "t", lazy.spawn(file_manager), desc="Launch file manager"),
    Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
    Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
    Key([mod, "shift"], "r", lazy.reload_config(), desc="Reload the config"),
    Key([mod, "shift"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
    Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
    Key([mod], "f", lazy.window.toggle_fullscreen(), desc="Toggle fullscreen"),
    Key([mod], "d", lazy.spawn(rofi), desc="Launch Rofi"),
    Key([mod], "r", lazy.spawn(rr), desc="Launch Rofi recording script"),
    Key([], "XF86AudioMute", lazy.spawn(volmute), desc="Toggle mute"),
    Key([], "XF86AudioLowerVolume", lazy.spawn(voldown), desc="Lower volume"),
    Key([], "XF86AudioRaiseVolume", lazy.spawn(volup), desc="Raise volume"),
    Key([], "ISO_Next_Group", lazy.function(lambda q: q.current_screen.top.widgets[kbindex].update_self()), desc="Next keyboard layout."),
    Key([], "Print", lazy.spawn(sstool), desc="Take screenshot"),
]

groups = [Group(i) for i in "123456789"]

for i in groups:
    keys.extend(
        [
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            Key([mod, "shift"], i.name, lazy.window.togroup(i.name),
                 desc="move focused window to group {}".format(i.name)),
        ]
    )

layouts = [
    layout.Columns(
        border_width=1,
        border_focus=col_selected,
        border_normal=col_unselected,
    ),
    layout.Max(),
]

widget_defaults = dict(
    font="JetBrains Mono, Bold",
    fontsize=18,
    foreground="#ebdbb2",
    fontshadow=None,
    padding=4,
)
extension_defaults = widget_defaults.copy()

separator="┇" 
block="[ {} ]"

screens = [
    Screen(
        top=bar.Bar(
            [
                widget.Image(filename=pictures + "arch-linux.png", margin=3),
                widget.GroupBox(
                    highlight_method="block",
                    borderwidth=4,
                    this_current_screen_border=col_selected,
                    inactive="#505050"
                ),
                widget.TextBox(separator),
                widget.Prompt(),
                #widget.Spacer(),
                widget.WindowName(),
                widget.Chord(
                    chords_colors={
                        "launch": ("#ff0000", "#ffffff"),
                    },
                    name_transform=lambda name: name.upper(),
                ),
                widget.Wttr(
                    location={city: "Home"}, 
                    fmt=block
                    ),
                widget.TextBox(separator),
               #kbl,
               #widget.TextBox(separator),
                widget.CPU(
                    fmt=block,
                    format = "CPU: {freq_current}%"
                    ),
                widget.TextBox(separator),
                widget.MemoryGraph(

                    border_width = 0,
                    graph_color = '505050',
                    fill_color = '75bd75'

                    ),
                widget.TextBox(separator),
                #widget.Memory(
                 #   fmt = block,
                  #  measure_mem='G',
                   # format="MEM: {MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}"
                    #),
                widget.Battery(
                    fmt=block,
                    format="{percent:2.0%}"
                ),
                widget.TextBox(separator),
                widget.Clock(format="%H:%M", 
                             fmt=block
                             ),
                #widget.TextBox(" "),
                #widget.Systray(),
                #widget.TextBox(separator),
                #widget.QuickExit(),
                widget.TextBox(" "),
                widget.Systray(),
            ],
            32,
            background="#1d2021",
            border_width=[2, 0, 2, 0],  # Draw top and bottom borders
            border_color=["3c3836", "000000", "3c3836", "000000"]  # Borders are grey 
        ),
    ),
]

#kbindex = next((index for index, obj in enumerate(screens[0].top.widgets) if obj == kbl), None)

mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(), start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []
follow_mouse_focus = True
bring_front_click = True 
cursor_warp = False
floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
        Match(title="mpv"),
        Match(title="feh"),
    ],
    border_focus=col_selected,
    border_normal=col_unselected,
    border_width=3
)
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

auto_minimize = True

wl_input_rules = None

wmname = "Qtile Mirolybik"
