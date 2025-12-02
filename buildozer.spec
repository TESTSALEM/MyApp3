[app]

# (str) Title of your application
title = Clicker Game

# (str) Package name (يجب أن يكون فريداً)
package.name = clickergame

# (str) Package domain (مطلوب لـ Android/iOS)
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include 
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements (تم تحديد إصدار Kivy)
requirements = python3,kivy==2.3.1,android

# (str) Application version
version = 1.0

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API (موصى به لـ Kivy)
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license 
# (مهم جداً للتشغيل التلقائي)
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a

# 🛑 الحل لخطأ التراخيص 36.1.0: تثبيت نسخة مستقرة 🛑
android.build_tools_version = 34.0.0

[buildozer]

# (int) Log level (2 = debug with command output)
log_level = 2

# (int) Display warning if buildozer is run as root (1 = True)
warn_on_root = 1
