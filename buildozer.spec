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

icon.filename = %(source.dir)s/icon.png

# ---------- Android ----------
android.api = 34
android.minapi = 21

android.ndk = 25b
android.sdk_path = /home/runner/android-sdk
android.ndk_path = /home/runner/android-sdk/ndk/25.1.8937393

android.permissions = INTERNET

android.archs = arm64-v8a, armeabi-v7a

android.allow_backup = True
android.gradle_dependencies =

android.enable_androidx = True
android.add_src =

android.private_storage = True

# ---------- Build ----------
log_level = 2
warn_on_root = 0

# ---------- Python ----------
android.copy_libs = True
