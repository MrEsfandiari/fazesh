[app]
title = Fazesh
package.name = fazesh
package.domain = org.fazesh

# ✅ الزامی – بدون این خط Build متوقف می‌شود
version = 0.1

source.dir = .
source.include_exts = py,png,jpg,kv,ttf

# ✅ وابستگی‌ها (پشتیبانی کامل فارسی)
requirements = python3,kivy,arabic-reshaper,python-bidi

# ✅ تنظیمات نمایش
orientation = portrait
fullscreen = 0

# ✅ تنظیمات اندروید (سازگار با Android جدید)
android.api = 34
android.minapi = 21

# ✅ NDK پایدار و سازگار با python-for-android
android.ndk = 25b

android.archs = arm64-v8a,armeabi-v7a

# ✅ مجوزها
android.permissions = INTERNET
android.allow_backup = True

# ✅ فونت فارسی
android.add_src = fonts
