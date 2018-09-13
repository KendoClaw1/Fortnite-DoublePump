import keyboard
import pyautogui
import time
from sys import argv




print """
 ,______________________________________
|_________________,----------._ [____]  ""-,__  __....-----=====
               (_(||||||||||||)___________/   ""                |
                  `----------' Krogg98[ ))"-,                   |
                                       ""    `,  _,--....___    |
                                               `/           \"\"\"\"
                                               Twitter: @KendoClaw1
                                               github: KendoClaw1
                                               DoublePump Automation script
"""





#The Keybind to shoot using the double pump.
pumpkey = argv[1]

#They location of the pump shotguns in the Weapons slots, for example 3 4.
pumplocations = argv[2:]

#The default time betweet each shot, after some tests using my Avg ping which is: 70ms i found that this's the lowest i could get between each shot without escaping any chance to shoot, lowering this may cause the script tp escape shots.
#Also when using Double Deagle/Tac/Revolver you have to lower this to achieve the Maximum power of the script.
defaultTime = 0.65

def doublepump():

	for pump in pumplocations :

		pyautogui.click()
		pyautogui.press(pump)
		time.sleep(defaultTime)

print "You can adjust the speed by pressing *-* and *+* on your keyboard, each press will increase/decrease the speed by 0.05 secs (the default for doublepump is 0.65, it won't work if the default speed is set lower than this) \n\n"

print "press * to Exit..."

try:

	while True:

		if keyboard.is_pressed(pumpkey):
			doublepump()

		elif keyboard.is_pressed("*"):
			exit()


		if keyboard.is_pressed("+"):
			defaultTime += 0.05
			print "The time between each shot is now set to: "+str(defaultTime)+" secs (default for doublepump is 0.65)"
			time.sleep(0.3)

		elif keyboard.is_pressed("-"):
			defaultTime -= 0.05
			print "The time between each shot is now set to: "+str(defaultTime)+" secs (default for doublepump is 0.65)"
			time.sleep(0.3)


except KeyboardInterrupt:
	print "Thanks for using."
