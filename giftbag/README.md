# Your Gift Bag:

### I am sending you each home with an embedded systems 'starter kit' containing:
* A [Trinket M0](https://www.adafruit.com/product/3500)
* A [Micro USB Cable](https://www.amazon.com/Mopower-Samsung-BlackBerry-Motorola-Smartphones/dp/B07J9WTJFQ)
* A [Breadboard](https://www.adafruit.com/product/64)
* Ten (10) [Jumper Wires](https://www.mouser.com/datasheet/2/58/BPS-DAT-(ZW-20)-Datasheet-1282891.pdf) 
* Three (3) [NPN Transistors](https://www.mouser.com/datasheet/2/308/2N3904-1118515.pdf)
* Three (3) [330ohm Resistors](https://www.mouser.com/datasheet/2/427/mbxsma-1539356.pdf)
* Three (3) [Red LEDs](https://www.mouser.com/datasheet/2/239/LITE-ON%20LTL-4221-1139741.pdf)
* Three (3) [Yellow LEDs](https://www.mouser.com/ds/2/239/LTL-4251N-1175429.pdf)
* Three (3) [Green LEDs](https://media.digikey.com/pdf/Data%20Sheets/Lite-On%20PDFs/LTL-4233.pdf)
* One (1) [Infrared Emitter](https://www.mouser.com/datasheet/2/239/E5208A-1144068.pdf)
* One (1) [Infrared Receiver](https://www.mouser.com/datasheet/2/427/tsop986-1489488.pdf)

### The Obligatory Safety Warnings:
Nothing in this kit contains hazardous substances (lead-free, etc.).  Similarly, everything is low voltage, 
so there is [virtually] no risk of hurting yourself.  That said, a few admonishments are prudent:
* Never connect any of this to mains (household) power-that stuff can kill you (!!!)
* Keep these things out of reach of small children-no one wants to spend the night
  in the ER waiting for a younger sibling to 'pass' the LED 'candy'
* Never leave stuff running unattended until its been thoroughly tested
* Always unplug before changing wires/components, etc. to avoid short circuits that can 
  destroy components, and potentially the connected USB port

### That said, have fun and be adventurous!
Do not be afraid to try things out.  Nothing in this kit is particularly expensive 
(the Trinket M0 is the most expensive item, but still less than $9).  If you mis-wire something
and 'fry' a component its no big deal-that's referred to as releasing the 
[magic smoke](https://en.wikipedia.org/wiki/Magic_smoke), and everyone does it.  

A great way to learn about electronics is to see how the 'pros' do it:  Grab stuff from your e-waste
pile and tear it apart.  I have learned a great deal about circuit design, power supplies, etc.
from just tearing things apart and Googling the part numbers.  If you are really adventurous you
can even harvest components to start building a library of parts for yourself.  

>Harvesting Tips: Don't waste your time harvesting the small cheap stuff (LEDs, transistors, etc.) or 
>purpose-built stuff (circuit boards, etc.).  Likewise, don't waste your time trying to harvest really small 
>parts (from cell phones, etc.).  Instead, focus on things like motors, gears, switches, etc.
that tend to be more expensive, are slow to obsolescence, and are the most fun to play with.  Old printers and
>copiers are ideal: They are a treasure-trove of motors, gears, and switches of all types.

### About this Kit
The heart of this kit is the Adafruit Trinket M0.  I chose this device because it's cheap, powerful (ARM Cortex M0) 
and can be coded in a variety of ways based on your comfort level:

* A standard text editor: Notepad, Vim, [VS Code](https://code.visualstudio.com/), [Mu](https://codewith.mu/), etc.
* [Microsoft MakeCode](https://maker.makecode.com/): Python, Javascript, and Blocks
* The good old [Arduino IDE](https://www.arduino.cc/en/main/software)

The approachability and low cost of the Trinket M0 comes with trade-offs: The number of available
input-output (I/O) pins is low (just five), and their ability to drive loads (supply electrical current)
is very limited (they can barely manage a single LED).  If you want to control anything that requires more than 
an LED does (a few milliamps), then you need to use a more robust component that switches on/off based on
a signal from the Trinket (an amplifier).  This is where the transistors come in:  They are solid-state (no moving parts)
switches that sit between the power-hungry device (the 'load'), and ground (the N in NPN transistor stands for 
'negative', aka the circuit's ground). When the Trinket wants to power the load, it sends a positive (the P in NPN) 
signal to the transistor causing the input N to couple with the output N, completing the electrical circuit for the load.

>In case you were wondering, yes there are PNP transistors too.  However, they are more expensive to produce,
generally have lower power ratings (fewer milliamps than the equivalent NPN transistor), and require
inverted inputs (0=on, 1=off).  As a result, NPN transistors are far more common.

>As a side note, the humble transistor is a BIG DEAL in history.  While the idea of general purpose computing was 
>first recognized by [Ada Lovelace](https://en.wikipedia.org/wiki/Ada_Lovelace) way back in the 1800s, the necessary 
>hardware was limited to mechanical ([Babbage](https://en.wikipedia.org/wiki/Analytical_Engine)), and later 
>electro-mechanical ([Eniac](https://en.wikipedia.org/wiki/ENIAC), [Univac](https://en.wikipedia.org/wiki/UNIVAC)) 
>switches.  As a result, those machines were terribly slow, outrageously expensive, notoriously 
>unreliable, and shockingly inefficient (computers the size of buildings for compute power a fraction of your Trinket M0).
>The transistor was immediately recognized as a game-changer, and earned the inventors a Nobel Prize in 1956.  Without the
>humble transistor there would be no smart phones, personal computers, internet, self-driving cars, communication satellites, 
>etc.  

### Getting Started With Your Kit
* Plug in your Trinket M0 and verify the default program is running (on-board multi-color LED cycles through the rainbow)
* Try connecting to the Trinket's serial console (the Mu editor is best for this) to see the console output of the default
  program (analog read values for pin D0)
* Now that things are working, check out Adafruit's [sample projects](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/circuitpython)
* Mix things up a bit and try out the sample projects at [Microsoft MakeCode](https://www.microsoft.com/en-us/makecode)

IMPORTANT: As shipped, your Trinket starts ('boots') into one of two modes:  
1. The user/application mode is the mode that interprets and runs Python code directly.  When you first power up your Trinket M0,
   and the RGB LED is cycling through the rainbow, it is running in this mode.  The files for this mode appear in a 
   CIRCUITPYTHON drive, and are editable.  To change the Trinket's behavior, you simply edit and save the main.py text file 
   for immediate effect.  If you choose to program this way, there is really no reason to leave this mode.
2. The supervisor/bootloader mode exposes the code that runs behind the scenes, and makes the user mode so easy to use 
   (triggering the python interpreter when main.py is saved, etc.).  You can switch to this mode by double-clicking the small
   button on the Trinket.  When in this mode, the Trinket's RGB LED will shine a solid green, and the connected drive will
   appear as "TRINKETBOOT".  It's a good idea to save a copy of the TRINKETBOOT folder somewhere so you can revert back to
   'factory defaults' when things go really bad.  If you don't, that's okay too:  Adafruit publishes the files, along with frequent
   updates, at the [Trinket M0 Circuit Python page](https://circuitpython.org/board/trinket_m0/).
   
>This is worth knowing because other programming workflows (notably Microsoft MakeCode and the Arduino IDE) over-write the supervisor 
>code, eliminating the as-shipped user mode entirely.  As a result, if you use MakeCode or the Arduino IDE things will work fine,
>but you will have to restore the original supervisor mode files for the CIRCUITPYTHON drive to work again.

Choice of Workflows
1. The default (as-shipped) workflow involves directly editing the main.py file in the CIRCUITPYTHON drive.  The runtime 
   environment is a derivative of Python, so don't expect a vast library of Python modules available for import/use.  Space
   on the device is constrained, so Adafruit is selective about what modules get pushed to the Trinket.  There are many
   modules available (for sensors, etc.), but you might have to load them manually (see the 
   [CircuitPython](https://circuitpython.org/board/trinket_m0/) page).  Besides simplicity, the main advantage of this 
   workflow is the serial console:  Since the Trinket has no display, or network connectivity, the serial console is the only 
   practical way to generate debugging messages, etc. during development.  
2. The other tested work flow is Microsoft [MakeCode](https://www.microsoft.com/en-us/makecode).  The MakeCode workflow 
   is fully supported by Adafruit (i.e. you won't break anything), and offers alternatives (graphical blocks and Javascript) 
   for those averse to programming in Python.  Additionally MakeCode lets you switch between the three while coding, allowing
   you to apply your programming knowledge across the different languages.  Lastly, MakeCode is a decent Integrated 
   Development Environment (IDE) with code completion, a simulator with full debugging, Fritzing diagrams for wiring your 
   breadboard, etc.  The trade-offs include the loss of the serial console (which makes debugging a lot harder), and the 
   overwriting of the original firmware (see above).
3. The last [untested] workflow is the [Arduino IDE](https://www.arduino.cc/en/main/software).  The Arduino IDE is great, and for programming Arduinos
   there is really nothing better.  However, the Arduino world is a C/C++ world, which is decidedly not beginner-friendly.
   Getting the Arduino IDE to talk to the Trinket M0 is [non-trivial](https://learn.adafruit.com/adafruit-trinket-m0-circuitpython-arduino/using-with-arduino-ide), especially in a classroom environment where the computing
   resources are unknown.  For all of those reasons I skipped testing the Arduino IDE for the Trinket M0.  That said,
   if someone really wants to use the Arduino IDE, and is having issues, I can certainly take a look at the problem.   
    
### Where To Go Next?
Exhaust your imagination with what's in the bag.  Off the top of my head I can think of a few fun things:
* Use the Red, Yellow, and Green LEDs to make a traffic light
* Use the built-in capacitive (touch) sensor to make something reactive to touch (a door handle alarm, etc.)
* Use the Infrared (IR) emitter and receiver to investigate and control the IR-controlled devices around you (televisions, etc.)
* Play with the Trinket M0's Human Interface Device (HID) capabilities to randomly send phantom keystrokes and mouse moves to
  a connected computer (and watch the person try to figure out what is happening), or wire in the IR receiver so you can inject funny 
  things as people type (press button on remote to inject "I like puppies", etc.).  Note: Don't do this to strangers, or 
  to people you know who may lack the requisite sense of humor.
* Consider acquiring some sensors (proximity, contact, accelerometer, gyroscopic, compass, etc.) or peripherals (motors, etc.)
* Make something cool for halloween
* Move up to a device with more pins, and maybe even more compute power (Raspberry Pi, etc.), and start planning that robot!