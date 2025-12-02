[app]

# (str) Title of your application
title = Clicker Game

# (str) Package name 
package.name = clickergame

# (str) Package domain
package.domain = org.test

# (str) Source code where the main.py live
source.dir = .

# (list) Source files to include 
source.include_exts = py,png,jpg,kv,atlas,json

# (list) Application requirements 
requirements = python3,kivy==2.3.1,android

# (str) Application version
version = 1.0

# (list) Supported orientations
orientation = portrait

# (bool) Indicate if the application should be fullscreen or not
fullscreen = 1

# (list) Permissions
android.permissions = INTERNET, WRITE_EXTERNAL_STORAGE, READ_EXTERNAL_STORAGE

# (int) Target Android API
android.api = 34

# (int) Minimum API your APK will support.
android.minapi = 21

# (str) Android NDK version to use
android.ndk = 25b

# (bool) If True, then automatically accept SDK license 
android.accept_sdk_license = True

# (str) The Android arch to build for
android.archs = arm64-v8a

# 🛑 الحل لخطأ التراخيص (License not accepted) 🛑
android.build_tools_version = 34.0.0

[buildozer]

# (int) Log level (2 = debug with command output)
log_level = 2

# 🛑 الحل لخطأ EOFError (منع طلب المدخلات اليدوية) 🛑
warn_on_root = 0
