[app]
title = Fazesh
package.name = fazesh
package.domain = org.fazesh
source.dir = .
source.include_exts = py,png,jpg,kv,ttf
version = 0.1

requirements = python3,kivy,arabic-reshaper,python-bidi

orientation = portrait

fullscreen = 0

android.add_src = fonts

[buildozer]
log_level = 2

[android]
android.api = 34
android.minapi = 21

android.ndk = 25b
android.sdk_path = /home/runner/android-sdk

android.archs = arm64-v8a,armeabi-v7a
android.allow_backup = True
android.permissions = INTERNET
