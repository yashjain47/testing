"""
Appium + Python SDET Interview — 70 Questions & Answers
PART 1 — Appium Fundamentals


-------------------------------------------------------------------------------------------------------
1. What is Appium?

Answer:

Appium is an open-source automation framework used to automate:

Android applications
iOS applications
Mobile browsers
Hybrid applications

It supports multiple programming languages, including:

Python
Java
JavaScript
C#
Ruby

For Python automation, we commonly use the Appium Python Client.


-------------------------------------------------------------------------------------------------------
2. What types of applications can Appium automate?

Answer:

Appium can automate:

Native apps
Hybrid apps
Mobile web applications

Example:

Native:
Settings
Calculator

Hybrid:
Shopping application containing native screens + WebView

Mobile Web:
Chrome / Safari

-------------------------------------------------------------------------------------------------------
3. What is a native application?

A native application is developed specifically for a particular operating system.

Examples:

Android → Kotlin/Java
iOS     → Swift/Objective-C

The UI is primarily composed of native mobile controls.

-------------------------------------------------------------------------------------------------------
4. What is a hybrid application?

A hybrid application combines:

Native UI
+
Web content

For example:

Login screen → Native

Payment page → WebView

Appium can switch between contexts to automate both.


-------------------------------------------------------------------------------------------------------
5. What is mobile web testing?

Mobile web testing means testing websites through mobile browsers.

Example:

Android → Chrome
iOS → Safari

The application itself isn't installed as a native application.

-------------------------------------------------------------------------------------------------------
6. What is Appium Server?

Appium Server acts as a communication layer between your automation code and the mobile device.

Conceptually:

Python Test
     ↓
Appium Python Client
     ↓
Appium Server
     ↓
Android/iOS Driver
     ↓
Mobile Device


-------------------------------------------------------------------------------------------------------
7. What is Appium 2?

Appium 2 uses a more modular architecture.

Drivers are installed separately rather than being bundled into the Appium server.

For example:

appium driver install uiautomator2

For Android automation, UiAutomator2 is commonly used.

For iOS, XCUITest is commonly used.


-------------------------------------------------------------------------------------------------------
8. What is UiAutomator2?

UiAutomator2 is an Android automation driver used by Appium.

It allows Appium to interact with Android UI elements.

Example:

from appium import webdriver

with the Android driver configured appropriately.


-------------------------------------------------------------------------------------------------------
9. What is XCUITest?

XCUITest is Apple's UI automation framework.

Appium uses the XCUITest driver to automate iOS applications.

Architecture:

Python
 ↓
Appium
 ↓
XCUITest Driver
 ↓
iOS


-------------------------------------------------------------------------------------------------------
10. What is Appium Inspector?

Appium Inspector is used to inspect mobile application UI elements.

You can inspect:

resource-id
accessibility ID
class name
XPath
text
content description
hierarchy

It is similar in purpose to browser developer tools for web automation.





-------------------------------------------------------------------------------------------------------
PART 2 — Desired Capabilities / Options
-------------------------------------------------------------------------------------------------------
11. What are capabilities in Appium?

Capabilities/options tell Appium how the session should be created.

For example:

from appium.options.android import UiAutomator2Options

options = UiAutomator2Options()

options.platform_name = "Android"
options.device_name = "Android"
options.automation_name = "UiAutomator2"
options.app_package = "com.example.app"
options.app_activity = ".MainActivity"


-------------------------------------------------------------------------------------------------------
12. What is platformName?

It specifies the operating system.

Example:

options.platform_name = "Android"

or:

options.platform_name = "iOS"


-------------------------------------------------------------------------------------------------------
13. What is automationName?

It tells Appium which automation engine/driver to use.

Android:

UiAutomator2

iOS:

XCUITest

Example:

options.automation_name = "UiAutomator2"


-------------------------------------------------------------------------------------------------------
14. What is deviceName?

It identifies the target device/emulator.

Example:

options.device_name = "Pixel_7"

For a real device, the configuration may use the connected device identifier.



-------------------------------------------------------------------------------------------------------
15. What are appPackage and appActivity?

They identify an Android application's package and starting activity.

Example:

appPackage = com.example.shopping

appActivity = .MainActivity

They are useful when launching an already-installed Android application.


-------------------------------------------------------------------------------------------------------
16. How do you find Android package/activity?

You can use Android debugging tools such as:

adb shell dumpsys window

or inspect the currently focused activity.

You can also use:

adb shell dumpsys activity activities


-------------------------------------------------------------------------------------------------------
17. What is noReset?

It controls whether Appium resets application data between sessions.

Example:

options.no_reset = True

Useful when you don't want to clear:

login state
application data
preferences



-------------------------------------------------------------------------------------------------------
18. What is fullReset?

It requests a more complete reset of the application/device state depending on the driver/platform.

In practical test frameworks, you should choose reset behavior carefully because full resets can increase execution time significantly.



-------------------------------------------------------------------------------------------------------
19. What is autoGrantPermissions?

It can automatically grant requested Android permissions during application setup.

Example:

options.auto_grant_permissions = True

This can be useful for test environments where the application requests permissions such as:

Camera
Location
Storage
Notifications



-------------------------------------------------------------------------------------------------------
20. noReset=True vs noReset=False?
Setting	Behavior
True	Preserve app data
False	Allow reset behavior
Useful for	State-dependent testing
Risk	Tests may become dependent on previous state

For independent tests, controlling application state explicitly is generally safer.








-------------------------------------------------------------------------------------------------------
PART 3 — Locators
-------------------------------------------------------------------------------------------------------
21. What locators can you use in Appium?

Common strategies include:

Accessibility ID
ID / resource-id
Class name
XPath
Android UIAutomator
iOS predicate/class chain


-------------------------------------------------------------------------------------------------------
22. Which locator should you prefer?

Generally:

Accessibility ID
     ↓
resource-id / ID
     ↓
platform-specific locator
     ↓
XPath

XPath should generally not be your first choice when a stable ID/accessibility identifier exists.


-------------------------------------------------------------------------------------------------------
23. Why is XPath often slower?

XPath may require traversing the UI hierarchy.

For example:

driver.find_element(
    AppiumBy.XPATH,
    "//android.widget.TextView[@text='Login']"
)

A stable identifier is generally preferable:

driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "login_button"
)



-------------------------------------------------------------------------------------------------------
24. What is Accessibility ID?

It identifies an element through its accessibility identifier/content description.

Example:

driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Login"
)

This is often a very good locator because it can be stable and meaningful.


-------------------------------------------------------------------------------------------------------
25. How do you find an element by text?

Example:

driver.find_element(
    AppiumBy.XPATH,
    "//*[@text='Login']"
)

But if an accessibility ID or resource ID exists, prefer that instead.


-------------------------------------------------------------------------------------------------------
PART 4 — Element Operations
-------------------------------------------------------------------------------------------------------
26. How do you tap an element?
element = driver.find_element(
    AppiumBy.ACCESSIBILITY_ID,
    "Login"
)

element.click()


-------------------------------------------------------------------------------------------------------
27. How do you enter text?
element = driver.find_element(
    AppiumBy.ID,
    "username"
)

element.send_keys("yash")
28. How do you clear text?
element.clear()

Then:

element.send_keys("new value")


-------------------------------------------------------------------------------------------------------
29. How do you get element text?
text = element.text

print(text)



-------------------------------------------------------------------------------------------------------
30. How do you check whether an element exists?

You can use a controlled lookup:

elements = driver.find_elements(
    AppiumBy.ID,
    "login_button"
)

assert len(elements) > 0

Using find_elements() avoids an immediate exception when nothing is found.



-------------------------------------------------------------------------------------------------------
31. How do you verify an element is displayed?
element = driver.find_element(
    AppiumBy.ID,
    "login_button"
)

assert element.is_displayed()


-------------------------------------------------------------------------------------------------------
32. How do you verify an element is enabled?
assert element.is_enabled()


-------------------------------------------------------------------------------------------------------
PART 5 — Waits & Synchronization
-------------------------------------------------------------------------------------------------------
33. Why are waits important in Appium?

Mobile applications are asynchronous.

For example:

Tap Login
   ↓
API request
   ↓
Loading
   ↓
Server response
   ↓
Dashboard appears

Immediately searching for the dashboard can cause flaky tests.


-------------------------------------------------------------------------------------------------------
34. What is implicit wait?

Example:

driver.implicitly_wait(10)

It tells the driver to wait when locating elements.

However, avoid mixing excessive implicit waits with explicit waits because debugging timing issues becomes harder.


-------------------------------------------------------------------------------------------------------
35. What is explicit wait?

Example:

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

element = WebDriverWait(driver, 20).until(
    EC.visibility_of_element_located(
        (AppiumBy.ID, "dashboard")
    )
)


-------------------------------------------------------------------------------------------------------
36. Which wait do you prefer?

For production frameworks:

Explicit waits are generally preferable because they wait for a specific condition.

Example:

element visible
element clickable
element present
specific text displayed


-------------------------------------------------------------------------------------------------------
PART 6 — Gestures
-------------------------------------------------------------------------------------------------------
37. How do you perform a swipe?

Modern Appium code commonly uses W3C actions or Appium gesture commands depending on the driver/client version.

Conceptually:

Start point
   ↓
Move
   ↓
End point

You should understand both the API you're using and the underlying W3C/Appium gesture model.


-------------------------------------------------------------------------------------------------------
38. How do you scroll?

For Android, one approach is:

driver.find_element(
    AppiumBy.ANDROID_UIAUTOMATOR,
    'new UiScrollable(new UiSelector()).scrollIntoView('
    'new UiSelector().text("Settings"));'
)

This is useful when you know the target text.


-------------------------------------------------------------------------------------------------------
39. Write a reusable scroll function.
def scroll_to_text(driver, text):
    return driver.find_element(
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector()).scrollIntoView('
        f'new UiSelector().text("{text}"));'
    )

Usage:

scroll_to_text(driver, "Settings").click()


-------------------------------------------------------------------------------------------------------
40. How do you perform long press?

A common W3C action approach is:

from selenium.webdriver.common.action_chains import ActionChains

or Appium's supported gesture APIs for your client/driver version.

The important interview point is:

A long press is a pointer interaction where the pointer remains pressed for a specified duration before release.


-------------------------------------------------------------------------------------------------------
41. Difference between tap and long press?

Tap:

Press → Release quickly

Long press:

Press → Hold → Release

Long press is commonly used for:

context menus
selecting items
drag initiation
special actions


-------------------------------------------------------------------------------------------------------
PART 7 — Context / Hybrid Applications
-------------------------------------------------------------------------------------------------------
42. What is context in Appium?

A context represents the automation environment currently being controlled.

For example:

NATIVE_APP
WEBVIEW_com.example


-------------------------------------------------------------------------------------------------------
43. How do you get available contexts?
contexts = driver.contexts

print(contexts)

Example:

['NATIVE_APP', 'WEBVIEW_com.example']


-------------------------------------------------------------------------------------------------------
44. How do you switch to WebView?
driver.switch_to.context("WEBVIEW_com.example")

Then web elements can be automated.


-------------------------------------------------------------------------------------------------------
45. How do you switch back to native?
driver.switch_to.context("NATIVE_APP")



-------------------------------------------------------------------------------------------------------
46. Scenario: WebView is visible but WEBVIEW doesn't appear. What do you check?

Strong interview answer:

I would check:

WebView is actually loaded.
Debugging is enabled where required.
Correct Appium/driver version.
Android WebView/Chrome compatibility.
Device configuration.
Context list after waiting for WebView initialization.
Application's WebView implementation.
Logs from Appium and Android.

I would avoid blindly adding sleeps and instead diagnose the context initialization problem.


-------------------------------------------------------------------------------------------------------
PART 8 — Android / ADB
-------------------------------------------------------------------------------------------------------
47. What is ADB?

ADB means:

Android Debug Bridge

It allows communication between a computer and Android devices.

Example:

adb devices


-------------------------------------------------------------------------------------------------------
48. How do you check connected devices?
adb devices

Output may look like:

List of devices attached
emulator-5554    device

-------------------------------------------------------------------------------------------------------
49. How do you install an APK?
adb install app.apk

-------------------------------------------------------------------------------------------------------
50. How do you uninstall an application?
adb uninstall com.example.app

-------------------------------------------------------------------------------------------------------
51. How do you capture Android logs?
adb logcat

This is extremely useful when debugging crashes and automation failures.


-------------------------------------------------------------------------------------------------------
PART 9 — Pytest + Appium
-------------------------------------------------------------------------------------------------------
52. How would you integrate Appium with pytest?

Example:

import pytest

@pytest.fixture
def driver():
    driver = create_driver()

    yield driver

    driver.quit()

Test:

def test_login(driver):
    driver.find_element(
        AppiumBy.ID,
        "username"
    ).send_keys("testuser")


-------------------------------------------------------------------------------------------------------
53. Why use pytest fixtures?

Fixtures allow you to manage:

driver creation
setup
teardown
test data
authentication
device configuration

This avoids duplicating setup code across tests.


-------------------------------------------------------------------------------------------------------
54. How would you design an Appium framework?

A simple structure:

mobile_automation/
│
├── tests/
│   ├── test_login.py
│   ├── test_home.py
│
├── pages/
│   ├── login_page.py
│   ├── home_page.py
│
├── utils/
│   ├── driver_factory.py
│   ├── wait_utils.py
│   ├── gesture_utils.py
│
├── config/
│   └── config.yaml
│
├── conftest.py
│
├── testdata/
│
└── reports/

This is a very good interview topic for an SDET.


-------------------------------------------------------------------------------------------------------
55. What should go inside conftest.py?

Typically:

Driver fixture
Environment configuration
Hooks
Screenshot handling
Common fixtures

Example:

@pytest.fixture
def driver():
    driver = create_driver()

    yield driver

    driver.quit()


-------------------------------------------------------------------------------------------------------
PART 10 — Coding Questions
-------------------------------------------------------------------------------------------------------
56. Coding: Create an Appium driver.
Question

Write Python code to create an Android Appium driver.

Answer
from appium import webdriver
from appium.options.android import UiAutomator2Options

def create_driver():

    options = UiAutomator2Options()

    options.platform_name = "Android"
    options.device_name = "Android"
    options.automation_name = "UiAutomator2"

    options.app_package = "com.example.app"
    options.app_activity = ".MainActivity"

    driver = webdriver.Remote(
        "http://127.0.0.1:4723",
        options=options
    )

    return driver


-------------------------------------------------------------------------------------------------------
57. Coding: Create a reusable login function.
def login(driver, username, password):

    driver.find_element(
        AppiumBy.ID,
        "username"
    ).send_keys(username)

    driver.find_element(
        AppiumBy.ID,
        "password"
    ).send_keys(password)

    driver.find_element(
        AppiumBy.ID,
        "login"
    ).click()

Interview follow-up:

Why create this function?

Because login is a reusable business action and should not be duplicated across test cases.


-------------------------------------------------------------------------------------------------------
58. Coding: Write a reusable explicit wait.
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def wait_for_element(driver, locator, timeout=20):

    return WebDriverWait(
        driver,
        timeout
    ).until(
        EC.visibility_of_element_located(locator)
    )

Usage:

login_button = wait_for_element(
    driver,
    (AppiumBy.ID, "login")
)

login_button.click()


-------------------------------------------------------------------------------------------------------
59. Coding: Create a screenshot on failure.
def take_screenshot(driver, name):

    path = f"reports/{name}.png"

    driver.save_screenshot(path)

    return path

Then integrate this with pytest hooks such as pytest_runtest_makereport to capture screenshots only when a test fails.


-------------------------------------------------------------------------------------------------------
60. Coding: Write a function to switch to WebView.
def switch_to_webview(driver):

    for context in driver.contexts:

        if "WEBVIEW" in context:
            driver.switch_to.context(context)
            return True

    return False

Usage:

assert switch_to_webview(driver)


-------------------------------------------------------------------------------------------------------
61. Coding: Switch back to native.
def switch_to_native(driver):

    driver.switch_to.context("NATIVE_APP")


-------------------------------------------------------------------------------------------------------
62. Coding: Scroll until an element is found.
def scroll_to_element(driver, text):

    locator = (
        AppiumBy.ANDROID_UIAUTOMATOR,
        f'new UiScrollable(new UiSelector()).scrollIntoView('
        f'new UiSelector().text("{text}"));'
    )

    return driver.find_element(*locator)

Usage:

element = scroll_to_element(
    driver,
    "Settings"
)

element.click()


-------------------------------------------------------------------------------------------------------
63. Coding: Write a generic click function.
def click_element(driver, locator, timeout=20):

    element = WebDriverWait(
        driver,
        timeout
    ).until(
        EC.element_to_be_clickable(locator)
    )

    element.click()

Usage:

click_element(
    driver,
    (AppiumBy.ID, "login")
)


-------------------------------------------------------------------------------------------------------
PART 11 — Scenario Questions
-------------------------------------------------------------------------------------------------------
64. Your test passes locally but fails randomly on CI. What do you do?

This is a very important SDET question.

I would investigate:

1. Device/emulator performance
2. Appium server logs
3. Timing issues
4. Missing waits
5. Network dependency
6. Application state
7. Parallel execution conflicts
8. Test-data dependency
9. Device availability
10. Screenshots/logcat

Then determine whether the failure is:

Application bug
Automation bug
Environment issue
Synchronization issue
Infrastructure issue

I would not simply increase all sleeps.



-------------------------------------------------------------------------------------------------------
65. Element is visible but click fails. What do you check?

I would check:

Element actually enabled?
Another element covering it?
Correct context?
Element stale?
Scroll position?
Animation still running?
Locator identifying correct element?
Is it inside another container?
Is native/WebView context correct?

Then I would use appropriate synchronization and, where needed, platform-specific interaction.


-------------------------------------------------------------------------------------------------------
66. App crashes during test. How would you investigate?

I would collect:

Appium logs
ADB logcat
Screenshot
Test step
Device information
App version
OS version
Stack trace

Example:

adb logcat

Then determine whether it is:

Application crash
Device problem
Automation problem
Environment problem


-------------------------------------------------------------------------------------------------------
67. How would you handle Android and iOS with one framework?

I would separate:

Common business logic
        ↓
Platform-specific implementation

For example:

pages/
    login_page.py

platform/
    android/
    ios/

utils/
    waits.py
    gestures.py

config/
    android.yaml
    ios.yaml

The test should ideally remain:

def test_login(driver):

    login_page.login(
        "user",
        "password"
    )

while platform-specific details remain inside the page/component layer.


-------------------------------------------------------------------------------------------------------
PART 12 — Advanced SDET Questions
-------------------------------------------------------------------------------------------------------
68. How would you run Appium tests in parallel?

Possible architecture:

pytest
   ↓
pytest-xdist / parallel orchestration
   ↓
Multiple Appium sessions
   ↓
Multiple devices/emulators

Each session needs unique device/session configuration.

For example:

Device 1 → Appium session 1
Device 2 → Appium session 2
Device 3 → Appium session 3

A common mistake is trying to run multiple tests against the same device/session without proper isolation.


-------------------------------------------------------------------------------------------------------
69. How would you integrate Appium into Jenkins?

Pipeline:

Git
 ↓
Jenkins
 ↓
Create environment
 ↓
Start Appium
 ↓
Connect device/emulator
 ↓
Run pytest
 ↓
Generate report
 ↓
Archive screenshots/logs

Example:

pytest tests/ \
    --html=reports/mobile_report.html \
    --self-contained-html

Then Jenkins can archive:

HTML report
Screenshots
Appium logs
ADB logs
Test artifacts


-------------------------------------------------------------------------------------------------------
70. Design an enterprise-level mobile automation framework.

This is one of the strongest questions you can prepare.

I would design:

                    CI/CD
                      │
                    pytest
                      │
              ┌───────┴────────┐
              │                │
          Test Cases       Test Data
              │
          Page Objects
              │
      Business Components
              │
       ┌──────┴──────┐
       │             │
   Android          iOS
       │             │
   UiAutomator2    XCUITest
       │             │
    Device Farm / Real Devices

Framework layers:

tests/
pages/
components/
utils/
drivers/
config/
testdata/
listeners/
reports/
logs/

Important framework capabilities:

Driver factory
Android/iOS support
Explicit waits
Gesture utilities
Screenshot on failure
Logging
HTML/Allure reporting
Test data management
Parallel execution
Environment configuration
CI/CD
Device selection
Retry strategy
Failure diagnostics









-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
⭐ 10 High-Value Coding Problems You Should Practice
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------

Don't just memorize the 15 coding snippets above. For an SDET interview, actually implement these yourself.
-------------------------------------------------------------------------------------------------------
Coding 1 — Generic wait

Create:

wait_for_element(driver, locator, timeout)

Requirements:

element present
element visible
element clickable


-------------------------------------------------------------------------------------------------------
Coding 2 — Generic scroll

Create:

scroll_until_visible(driver, text)

It should:

search
↓
if not found
↓
scroll
↓
search again
↓
stop when found

-------------------------------------------------------------------------------------------------------
Coding 3 — Login Page Object

Create:

LoginPage

username
password
login button

login()

-------------------------------------------------------------------------------------------------------
Coding 4 — Screenshot on failure

Implement a pytest hook:

pytest_runtest_makereport

Requirement:

Test FAIL
   ↓
Screenshot
   ↓
reports/screenshots/


-------------------------------------------------------------------------------------------------------
Coding 5 — Context switcher

Implement:

switch_to_context(driver, "WEBVIEW")

It should:

get contexts
↓
find matching context
↓
switch
↓
return True

-------------------------------------------------------------------------------------------------------
Coding 6 — Generic gesture utility

Create:

tap()
long_press()
swipe()
scroll()

inside:

utils/gesture_utils.py

-------------------------------------------------------------------------------------------------------
Coding 7 — Driver Factory

Create:

create_driver(platform)

Expected:

create_driver("android")
create_driver("ios")

The same test suite should be able to use the appropriate driver.


-------------------------------------------------------------------------------------------------------
Coding 8 — Retry failed tests

Implement pytest retry behavior.

But be prepared for the interview question:

Should every failed test be retried?

Correct answer:

No.

Retries can hide genuine application defects. They should be used carefully for known transient/environment failures.


-------------------------------------------------------------------------------------------------------
Coding 9 — Parallel execution

Create two configurations:

Android device 1
Android device 2

Then run tests independently.

Understand:

pytest -n 2

but more importantly understand session/device isolation.


-------------------------------------------------------------------------------------------------------
Coding 10 — Failure diagnostic framework

When a test fails:

FAIL
 ↓
Screenshot
 ↓
Appium log
 ↓
ADB logcat
 ↓
Current test step
 ↓
Device information
 ↓
HTML report

This is the kind of problem that differentiates an SDET from someone who only knows Appium commands.








-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
🔥 What Interviewers Will Actually Test
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------
-------------------------------------------------------------------------------------------------------

Since you're already an SDET, I wouldn't stop at:

"How do you scroll?"

They'll increasingly ask:

Beginner
What is Appium?
What is UiAutomator2?
What are capabilities?
How do you locate elements?
How do you perform gestures?
Intermediate
How do you handle synchronization?
How do you automate hybrid apps?
How do you handle WebView?
How do you integrate Appium with pytest?
How do you generate reports?

Advanced
How do you design a framework?
How do you run Android + iOS?
How do you run tests in parallel?
How do you handle flaky tests?
How do you debug CI failures?
How do you capture device logs?
How do you manage multiple devices?

SDET-level

The interviewer may give you a situation:

"You have 100 mobile tests. 20% randomly fail. Your manager says the automation is unreliable. What will you do?"

Your answer should go beyond:

"I'll add waits."

You should discuss:

Failure classification
        ↓
Flaky test identification
        ↓
Appium logs
        ↓
Device logs
        ↓
Screenshots/video
        ↓
Synchronization
        ↓
Test isolation
        ↓
Network dependency
        ↓
Parallel conflicts
        ↓
Environment stability
        ↓
Root-cause analysis

That's the level I'd target for your Appium SDET preparation.
 

"""












"""
Function	            Use

driver.back()	        Press Android back button
driver.forward()	    Navigate forward
driver.refresh()	    Refresh/reload current page
driver.close()	        Close current window/context
driver.quit()	        End Appium session


Find one element
driver.find_element("id", "username")

Find multiple elements
driver.find_elements("class name", "android.widget.TextView")

Common locator strategies:
driver.find_element("id", "com.app:id/login")
driver.find_element("xpath", "//android.widget.Button")
driver.find_element("accessibility id", "Login")
driver.find_element("class name", "android.widget.Button")
driver.find_element("android uiautomator", 'new UiSelector().text("Login")')




click               >>      element.click()
Clear               >>      element.clear()
Enter Text          >>      element.send_keys("Yash")
Text                >>      print(element.text)
check_displayed     >>      element.is_displayed()
check_selected      >>      element.is_selected()
check_enabled       >>      element.is_enabled()
Hode_keyboard       >>      driver.hide_keyboard()


Launch App          >>      driver.activate_app("com.example.app")
terminate App       >>      driver.terminate_app("com.example.app") 
Is _Installed       >>      driver.is_app_installed("com.example.app")
Install App         >>      driver.install_app("/path/to/app.apk")
UnInstall App       >>      driver.remove_app("com.example.app")

Current Package     >>      print(driver.current_package)
Current Activity    >>      print(driver.current_activity)
Take screenshot     >>      driver.save_screenshot("login.png")
Take screenshot     >>      driver.get_screenshot_as_file("login.png")

UI heirarchy        >>      print(driver.page_source)
screen_size         >>      driver.get_window_size()
width               >>      driver.get_window_size()["width"]
height              >>      driver.get_window_size()["height"]

get_orientation     >>      print(driver.orientation)
change_orientation  >>      driver.orientation = "LANDSCAPE"
change_orientation  >>      driver.orientation = "PORTRAIT"

Current_context     >>      print(driver.current_context)
All_context         >>      print(driver.current_contexts)
switch_context      >>      driver.switch_to.context("WEBVIEW_com.example.app")
Alerts Accept       >>      driver.switch_to.alert.accept()
Alerts dismiss      >>      driver.switch_to.alert.dismiss()
Alerts with text    >>      driver.switch_to.alert.send_keys("Yash")
alerts text         >>      driver.switch_to.alert.text




:::::::::::::::::: Execute Mobile Command ::::::::::::::::::

Like: 

driver.execute_script(
    "mobile: scrollGesture",
    {
        "left": 100,
        "top": 500,
        "width": 800,
        "height": 1000,
        "direction": "down",
        "percent": 0.75
    }
)


mobile: swipeGesture
mobile: scrollGesture
mobile: dragGesture
mobile: clickGesture
mobile: longClickGesture
mobile: pinchOpenGesture
mobile: pinchCloseGesture




:::::::::::::::::: Window / Web Functions ::::::::::::::::::

driver.get("https://example.com")
driver.current_url
driver.title



"""