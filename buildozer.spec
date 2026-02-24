[app]

title = LectorApp
package.name = lectorapp
package.domain = org.carlos

source.dir = .
source.include_exts = py,png,jpg,kv,atlas
source.exclude_exts = spec

version = 1.0

requirements = python3,kivy==2.3.0,requests,pillow,pyjnius

orientation = portrait
fullscreen = 0

android.permissions = CAMERA, INTERNET

android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.sdk_build_tools = 33.0.2
android.archs = arm64-v8a, armeabi-v7a

android.enable_androidx = True
android.copy_libs = 1

p4a.bootstrap = sdl2
android.ndk = 25b
android.sdk_build_tools = 33.0.2

log_level = 2
debug = 1


[buildozer]
log_level = 2

warn_on_root = 0

