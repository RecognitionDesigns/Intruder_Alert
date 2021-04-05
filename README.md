# Intruder_Alert
Vector will alert you if an unknown person is detected!

To get notifications on your phone, you will need to sign up to this app, 

https://pushover.net *

You can get a 30 day free trial to try out this script.

When you create a Pushover account, create a new APP and give it a name 9This will pop up on the phone notification), then get the App token and user details and enter them into the 'keys.py' script.

In the 'Intruder_Alert.py' script, change where it says 'name1' and 'name2' (if required) to the name of faces known faces saved on Vector, make sure to write them exactly as shown in the app.
(Line 57, 64 and 71)

BONUS:
This script also contains some code that will detect if Vector is stuck on a ledge and will send an alert with picture after 10 seconds!

Please note:
Vector sometimes has trouble recognising known faces straight away, this depends on the lighting and how the original face was first enrolled. To overcome this, try enrolling your face in different lighting conditions and angles. Vector will tell you if he already recognises you in the current position.

*I'm not affiliated with this app or company and receive no income from referrals.
