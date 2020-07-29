"""
    _    _   _
   / \  | \ | | Anant Narayan
  / _ \ |  \| |
 / ___ \| |\  |
/_/   \_\_| \_|

My own customized config for Qtile, which is a tiling window manager written
in Python.

"""
# Copyright (c) 2010 Aldo Cortesi
# Copyright (c) 2010, 2014 dequis
# Copyright (c) 2012 Randall Ma
# Copyright (c) 2012-2014 Tycho Andersen
# Copyright (c) 2012 Craig Barnes
# Copyright (c) 2013 horsik
# Copyright (c) 2013 Tao Sauvage
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from libqtile.config import Key, Screen, Group, Drag, Click, Match
from libqtile.command import lazy
from libqtile import layout, bar, widget
from libqtile import hook
from libqtile.dgroups import simple_key_binder
from typing import List  # noqa: F401
import os
import subprocess


mod = "mod4"

# My variables

term = "kitty --config /home/anant/.kitty.conf --title Terminal" # Terminal
# term = "alacritty" # Terminal
browser = "vivaldi-stable" # Browser
config = "/home/anant/.config/qtile/config.py" # My config
fm = "Thunar" # File manager
mpd = "celluloid" # Media player

keys = [
    # Essential Key Bindings
    Key([mod], "Return", lazy.spawn(term)), # Terminal
    Key([mod], "p", lazy.spawn("rofi -show drun")), # Rofi
    Key([mod, "shift"], "c", lazy.window.kill()), # Kill current window
    Key([mod], "e", lazy.spawn("emacs")), # Doom Emacs
    Key([mod], "w", lazy.spawn("vivaldi-stable")), # Vivaldi Browser
    Key([mod, "shift"], "e", lazy.spawn("emacsclient -c -a emacs /home/anant/.config/qtile/config.py")), # Open my config easily
    Key([mod], "m", lazy.spawn(mpd)),
    # Layout and Window Stuff
    Key([mod], "k", lazy.layout.down()),
    Key([mod], "j", lazy.layout.up()),

    # Move windows up or down in current stack
    Key([mod, "control"], "k", lazy.layout.shuffle_down()),
    Key([mod, "control"], "j", lazy.layout.shuffle_up()),

    # Switch window focus to other pane(s) of stack
    Key([mod], "space", lazy.layout.next()),

    # Swap panes of split stack
    Key([mod, "shift"], "space", lazy.layout.rotate()),

    Key([mod, "shift"], "r", lazy.restart()),
    Key([mod, "shift"], "q", lazy.shutdown()),
]

group_names = [("  ", {'layout': 'monadtall'}),
               ("  ", {'layout': 'monadtall'}),
               ("  ", {'layout': 'monadtall'}),
               ("  ", {'layout': 'monadtall'}),
               ("  ", {'layout': 'monadtall'}),
               ("   ", {'layout': 'floating'})]

groups = [Group(name, **kwargs) for name, kwargs in group_names]

for i, (name, kwargs) in enumerate(group_names, 1):
    keys.append(Key([mod], str(i), lazy.group[name].toscreen()))        # Switch to another group
    keys.append(Key([mod, "shift"], str(i), lazy.window.togroup(name))) # Send current window to another group


layout_theme = { "border_width" : 2,
               "margin" : 14,
               "border_focus" : "b115bf",
               "border_normal" : "7d00fa"
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Floating(**layout_theme),
    layout.Max(**layout_theme)
]

# Solarized Color Scheme
colors = [["#002b36", "#002b36"],
          ["#839496", "#839496"],
          ["#dc322f", "#dc322f"],
          ["#859900", "#859900"],
          ["#b58900", "#b58900"],
          ["#268bd2", "#268bd2"],
          ["#d33682", "#d33682"],
          ["#eee8d5", "#eee8d5"],
# Non Solarized Color Scheme
          ["#282a36", "#282a36"],
          ["#7d00fa", "#7d00fa"],
          ["#ff5c57", "#ff5c57"],
          ["#5af78e", "#5af78e"],
          ["#f3f99d", "#f3f99d"],
          ["#57c7ff", "#57c7ff"],
          ["#ff6ac1", "#ff6ac1"],
          ["#9aedfe", "#9aedfe"],
          ["#f1f1f0", "#f1f1f0"]
]

widget_defaults = dict(
    font='Hack',
    fontsize=12,
    padding=3,
    background=colors[0]
)
extension_defaults = widget_defaults.copy()

screens = [
   Screen(
        top=bar.Bar(
          [
                widget.Sep(
                    linewidth = 0,
                    padding = 10,
                    foreground = colors[7],
                    background = colors[0]
                ),
                widget.TextBox(
                    text = 'Qtile',
                    font = 'Ubuntu Mono Bold',
                    fontsize = 14,
                    background = colors[14],
                    foreground = colors[7]
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    foreground = colors[0],
                    background = colors[0]
                ),
                widget.GroupBox(
                    font = "Hack",
                    fontsize = 12,
                    margin_y = 3,
                    margin_x = 0,
                    padding_y = 5,
                    padding_x = 3,
                    boderwidth = 3,
                    active = colors[8],
                    inactive = colors[7],
                    rounded = True,
                    highlight_color = colors[13],
                    highlight_method = "line",
                    this_current_screen_border = colors[6],
                    this_screen_border = colors[7],
                    foreground = colors[4],
                    background = colors[13]
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 140,
                    foreground = colors[0],
                    background = colors[0]
                ),
                widget.TaskList(
                    foreground = colors[10],
                    background = colors[0],
                    font = 'Ubuntu Mono Bold',
                    fontsize = 13,
                    padding = 2,
                    rounded = False,
                    highlight_method = 'block'
                ),
                widget.ThermalSensor(
                    background = colors[12],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold',
                    fontsize = 12
                    ),
                widget.Sep(
                    background = colors[0],
                    foreground = colors[0],
                    padding =8
                ),
                widget.Memory(
                    format = '{MemUsed}Mb of total {MemTotal}Mb',
                    background = colors[13],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold',
                    fontsize = 12,
                    update_interval = 1.0
                ),
                widget.Sep(
                    padding = 8,
                    background = colors[0],
                    foreground = colors[0]
                ),
                widget.Pacman(
                    background = colors[14],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold',
                    fontsize = 12
                ),
                widget.TextBox(
                    text = 'Updates',
                    background = colors[14],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold',
                    fontsize = 12
                ),
                widget.Sep(
                    padding = 8,
                    background = colors[0],
                    foreground = colors[0]
                ),
                widget.CurrentLayoutIcon(
                    background = colors[11],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold',
                    custom_icon_paths = [os.path.expanduser("~/.config/qtile/icons")],
                    fontsize = 12
                ),
                widget.CurrentLayout(
                    background = colors[11],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold ',
                    fontsize = 12
                ),
                widget.Sep(
                    padding = 8,
                    background = colors[0],
                    foreground = colors[0]
                ),
                widget.Clock(
                    background = colors[10],
                    foreground = colors[8],
                    font = 'Ubuntu Mono Bold',
                    fontsize = 12,
                    format='%I:%M %p %A, %d of %B.',
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    background = colors[0],
                    foreground = colors[0]
                ),

                widget.Systray(
                    background = colors[13],
                    foregorund = colors[10],
                    icon_size = 20,
                    padding = 5
                ),
                widget.Sep(
                    linewidth = 0,
                    padding = 8,
                    background = colors[0],
                    foreground = colors[0]
                ),
            ],
            26,
        ),
    ),
]
# Drag floating layouts.
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
         start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
         start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

# Startup Apps

@hook.subscribe.startup_once
def autostart():
    home = os.path.expanduser('~/.config/qtile/autostart.sh')
    subprocess.call([home])

dgroups_key_binder = None
dgroups_app_rules = []  # type: List
main = None
follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},  # gitk
    {'wmclass': 'makebranch'},  # gitk
    {'wmclass': 'maketag'},  # gitk
    {'wname': 'branchdialog'},  # gitk
    {'wname': 'pinentry'},  # GPG key password entry
    {'wmclass': 'ssh-askpass'},  # ssh-askpass
])
auto_fullscreen = True
focus_on_window_activation = "smart"

wmname = "Qtile"
