# IKEA_Assessment
Android test automation framework

# Tools/SW used to develop test cases
* Appium
* Appium Inspector
* Python 3.10+
* pytest
* pytest plugin `pytest-html`
* Plant UML pluggin

## Installations steps
* Install appium following [this](https://appium.io/docs/en/latest/quickstart/install/)
  * Next install `UiAutomator2 Driver` following [this](https://appium.io/docs/en/latest/quickstart/uiauto2-driver/)
* Install python
* Install pytest `pip install pytest`

## How to run the test cases
### Configurations
Add next lines to your `.bashrc` or `.bash_aliases` file to be able to execute android tools and pytest directly in console. 
```
# android tools
export ANDROID_HOME=~/Android/Sdk
export ANDROID_TOOLS=$ANDROID_HOME/platform-tools
bin:$ANDROID_HOME/platform-tools
export PATH=$PATH:$ANDROID_HOME/platform-tools
##############################################
# pytest settings
export PATH=$PATH:$HOME/.local/bin
```
Install IKEA app in your android device, it can be downloaded [here](https://play.google.com/store/apps/details?id=com.ikea.inter.homesmart.system2&pcampaignid=web_share).

* Configure on-device developer options, instructions [here](https://developer.android.com/studio/debug/dev-options).

* Connect your android device trought USB.
    * Verify that your device is connected runing `adb devices` it should show your device.

* Clone this repository `git clone git@github.com:Monse0051/IKEA_Assessment.git`

* Execute `cd <your_repo_path>/tests/`

* Execute `pytest tests.py` This will run all the test cases if you want to run each one separetly execute `pytest test.py -k <test_case_name>` 


# Test Cases documentation
See [Test Cases](./docs/test_cases.md)

## Test Cases Report

See [report.html](./tests/logs/report.html) to see report html source.
See [report](https://github.com/Monse0051/IKEA_Assessment/blob/main/tests/logs/report.html) To see the rendered html page
