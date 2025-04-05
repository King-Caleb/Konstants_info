buildozer
# Buildozer settings

# (str) Name of the application
app_name = MoneySim - p

# (str) Package name
package.name = money_sim

# (str) Package domain (used for internal app namespace)
package.domain = com.ABI

# (int) Application version number (used for versioning the app)
version = 1.0.0

# (list) Application requirements
requirements = kivy,tkinter,threading,random

App

# (str) Package organization
# This should be unique for your app

# (str) Buildozer app directory
# Set this to the location of your app's source code
# app_directory = /path/to/your/app

# (str) Application entry point
# This should be the main file in your project
# You may want to specify the name of your main game file here
# For example:
# main.py = money_sim.py

# (str) Platform target
# Uncomment the platform you're targeting, use android for Android or ios for iOS
target = android

# (str) Kivy version
# Set the kivy version you want to use for the build
kivy.version = 2.1.0

# (bool) Enable or disable fullscreen mode
# Set to true if you want fullscreen mode
fullscreen = True

# (str) Additional Python requirements
# This is useful for custom modules you might need to install
# e.g. numpy or custom libraries
# Additional Python modules
# additional_modules = module1,module2

# (list) Additional Kivy modules
# Specify any Kivy modules required for your app (e.g., kivy_garden)
# kivy_modules = module1,module2

# (str) Path to the application icon
# You can specify an icon for your app here
# This will be used for the Android app icon, for instance
# icon.filename = path/to/your/icon.png

# (str) Path to the app's splash screen
# You can specify a splash screen here
# splash.filename = path/to/your/splashscreen.png

# (list) Application environment variables
# Any environment variables your app needs can go here
# env_variables = ENV_VAR=value

# (str) Android application version code
# The version code used by Android
version_code = 1

# (str) Android application version name
version_name = 1.0.0

# (str) Path to the Keystore file (for signing the APK)
# You can leave this blank if you don’t need a custom keystore
# keystore = /path/to/your/keystore

# (str) Keystore password
# keystore.password = your_keystore_password

# (str) Keystore alias
# keystore.alias = your_keystore_alias

# (str) Keystore alias password
# keystore.alias_password = your_keystore_alias_password

# (bool) Whether to build in debug mode
# If set to false, the app will be built in release mode
debug = true

# (list) Android permissions
# Specify permissions your app will need on Android (e.g. INTERNET, ACCESS_FINE_LOCATION)
# permissions = INTERNET,ACCESS_FINE_LOCATION

# (bool) Set this to true to use a virtual environment for the build
# venv = true

# (str) Set the app title on the Android home screen
app_title = Money Sim Game

# (str) Additional build tools
# You can specify additional tools you want to use for the build
# build_tools = tool1, tool2

# (bool) Enable or disable audio features
# Enable this if your game has audio
audio_enabled = true

# (bool) Enable or disable camera access
# Enable this if your game uses the camera
camera_enabled = false
