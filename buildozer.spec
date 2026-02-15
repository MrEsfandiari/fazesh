[app]
title = Fazesh
package.name = fazesh
package.domain = org.fazesh

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

requirements = python3,kivy,arabic-reshaper,python-bidi

orientation = portrait
fullscreen = 0

icon.filename = %(source.dir)s/icon.png

# ---------------- Android ----------------
android.api = 34
android.minapi = 21
android.ndk = 25b
android.archs = arm64-v8a,armeabi-v7a

android.permissions = INTERNET
android.allow_backup = True

# Performance
android.enable_androidx = True
android.gradle_dependencies = androidx.appcompat:appcompat:1.6.1

# Logcat (debug)
android.logcat_filters = *:S python:D

# ---------------- Build ----------------
log_level = 2
warn_on_root = 1
