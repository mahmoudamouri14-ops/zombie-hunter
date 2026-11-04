[app]

# (str) Title of your application
title = Zombie Hunter

# (str) Package name
package.name = zombiehunter

# (str) Package domain (needed for android packaging)
package.domain = org.zombie.game

# (list) Source files to include (let it include py)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application requirements
# (charset and python3 are essential)
requirements = python3,pygame

# (str) Supported orientations
orientation = portrait

# (int) Target Android API, should be as high as possible.
android.api = 33

# (int) Minimum API your APK / AAB will support.
android.minapi = 21

# (str) Android SDK version to use
android.sdk = 20

# (str) Supported architectures
android.archs = arm64-v8a

# (bool) Enable fullscreen
fullscreen = 1
