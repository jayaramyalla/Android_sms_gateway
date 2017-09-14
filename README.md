# Android_sms_gateway

Here is my new code that make your android smart phone as sms gateway

STEP 1:
1.Install qpython3 from playstore
https://play.google.com/store/apps/details?id=org.qpython.qpy3&hl=en

2.Open Qpython3 and goto "Programs" tab

3.Search pip_console.py and run the program

4.Now here you will be in terminal so install below module by typing
pip install bottle
pip install sl4a

STEP 2:
clone the "android-smartphone-sms-gatway.py" file into your android storage

STEP 3:
Go back to Qpython3 app 
Goto editor and browse to "android-smartphone-sms-gatway.py" and click play button which is located at below on same screen to run the code

STEP 4:
Find your device IP address 
if you dont know how to find you IP address follow below article
http://ccm.net/faq/33725-how-to-check-your-android-ip-address


Now open the url on any other device on same network and it will present you back with web interface

url: http://YOUR_SMARTPHONE_IP_ADDRESS:8080/login
api: http://YOUR_SMARTPHONE_IP_ADDRESS:8080/<your target mobile number>/<message to target number>
