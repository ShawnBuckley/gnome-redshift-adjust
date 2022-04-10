#!/usr/bin/python3

import sys
from gi.repository import Gio
from gi.repository import GLib

amount = int(sys.argv[1])


settings = Gio.Settings.new('org.gnome.settings-daemon.plugins.color')


def get():
    return settings.get_value('night-light-temperature').get_uint32()


def set(value):
    return settings.set_value('night-light-temperature', GLib.Variant.new_uint32(value))


current = get()
next = current + amount

if next < 1000:
    next = 1000

if next > 6500:
    next = 6500

print(current)
set(next)
print(get())
