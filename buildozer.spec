[app]
title = Fazesh
package.name = fazesh
package.domain = org.fazesh

version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

requirements = python3,kivy,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 0

android.api = 34
android.minapi = 21

# ✅ فقط این NDK
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET
android.allow_backup = True

android.add_src = fonts
