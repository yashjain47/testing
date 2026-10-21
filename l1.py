"""

Mobile Testing  - Appium


************************ Installation ************************

1. Android Studio
https://developer.android.com/studio

2. Gradle
https://docs.gradle.org/current/userguide/installation.html#ex-installing-manually

3. Appium Inspector
https://github.com/appium/appium-inspector/releases

4. Java11
https://www.oracle.com/in/java/technologies/javase/jdk11-archive-downloads.html

5. Node.js
https://nodejs.org/en/download

6. Appium
npm install -g appium@next
npm install -g appium-doctor
npm cache clean --force

appium --version
appium-doctor --version

npm config set legacy-peer-deps true
appium driver install uiautomator2
appium driver install chromium

7. Python
pip install Appium-Python-Client


8. Pycharm






************************ Emulator Setup ************************
2 ways to setup the Emulators in Android Studio

1. Directly in Android Studio

>> Go to Tools > Device Manager
>> Add New Device [Virtual Emulator]
>> Install the Desired Mobile/device and install its whole package.
>> Run it.

2. Using Appium



Install APK using ADB inside Emulator

1. By Dropping driectly into Emulator
2. Using ADB [Bypass for bypassing any restrictions]
adb install --bypass-low-target-sdk-block "API+Demos_4.0_apkcombo.com.apk"




Android Studio      >>  Creating/starting a virtual/real device, to perform actions like opening setting app, others.
Appium Inspector    >>  For Validating App elements Like selectors hub.
cmd                 >>  opening the Appium server for Appium inspector to connect [command : appium --port 4724]



Appium Inspector:
{
  "platformName": "Android",
  "appium:platformVersion": "17",
  "appium:deviceName": "emulator-5554",
  "appium:automationName": "UIAutomator2",
  "appium:ensureWebViewHavePages": "true"
}

CMD : appium --port 4724



When device/emulator is connected, we can check via adb as well.
like:
adb devices     >>  shows emulator or real device here.
adb shell       >>  Go into device.

adb shell dumpsys window | grep -E 'mCurrentFocus|mFocusedApp'
adb shell dumpsys window | findstr mCurrentFocus
adb shell dumpsys window | Select-String "mCurrentFocus"










"""





# import time
#
# import pytest
# from typing import Any, Dict
# from appium import webdriver
# from appium.options.common import AppiumOptions
# from appium.webdriver.common.appiumby import AppiumBy
#
#
# cap: Dict[str, Any] = {
#     'platformName': 'Android',
#     'automationName': 'UIAutomator2',
#     'deviceName': 'Android',
#     'appPackage': 'com.android.settings',
#     'appActivity': '.Settings',
#     'language' : 'en',
#     'locale' : 'US'
# }
#
# url = "http://localhost:4724"
#
# driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
#
# time.sleep(10)
# el = driver.find_element(by=AppiumBy.XPATH, value='//*[contains(@text, "Battery")]')
# el.click()
#
# driver.quit()


from typing import Any, Dict
from appium import webdriver
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'UIAutomator2',
    'deviceName': 'Pixel_9',
    'appPackage': 'com.android.settings',
    'appActivity': '.Settings',
    'language': 'en',
    'locale': 'US'
}

url = "http://localhost:4724"
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

try:
    # 1. Define a generous wait time for system rendering lag
    wait = WebDriverWait(driver, 15)

    # 2. STEP 1: Wait for the main scroll container to load completely
    print("Waiting for Settings dashboard to load...")
    wait.until(EC.presence_of_element_located((AppiumBy.CLASS_NAME, "android.widget.ScrollView")))

    # 3. STEP 2: Use UIAutomator textContains to scroll and find the Battery item safely
    # This matches "Battery", "Battery & device care", or "Battery - 80%" automatically
    scroll_expression = (
        'new UiScrollable(new UiSelector().scrollable(true)).scrollIntoView('
        'new UiSelector().textContains("Battery"));'
    )

    print("Scrolling to find the Battery section...")
    battery_element = wait.until(
        EC.element_to_be_clickable((AppiumBy.ANDROID_UIAUTOMATOR, scroll_expression))
    )

    # 4. Click it
    battery_element.click()
    print("Successfully opened Battery settings!")

except Exception as e:
    print(f"Execution failed: {e}")
    # Print a wider snapshot of the screen structure if it fails
    print("\n--- Current Page Source Structure - --")
    print(driver.page_source[:5000])

finally:
    driver.quit()












