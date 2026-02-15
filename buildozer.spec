[app]
title = دستگاه فازش
package.name = fazesh
package.domain = org.fazesh

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

version = 0.1

requirements = python3,kivy,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 1

android.api = 34
android.minapi = 21
android.ndk = 25b

android.permissions = INTERNET
android.allow_backup = True

android.archs = arm64-v8a,armeabi-v7a

icon.filename = icon.png

[buildozer]
log_level = 2
warn_on_root = 1
