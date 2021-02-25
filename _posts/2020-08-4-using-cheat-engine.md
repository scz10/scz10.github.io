---
title: Using Cheat Engine to-do Memory Scanning
redirect_from:
  - /game-hacking-using-cheat-engine
  - /game-hacking-using-cheat-engine/
mode: immersive
header:
  theme: dark
article_header:
  type: overlay
  theme: dark
  background_color: '#123'
  background_image: false
tags: [memory-scanning]
key: Using-Cheat-Engine-to-do-Memory-Scanning
---
Applications uses RAM / Memory to store data variables - You can access and manipulate these data in realtime.
So how does it work? To understand this better here's a quick summary of how Apps / RAM works:

<!--more-->
---

![diagram1](https://chy.my.id/post_data/2/diagram1.png){:.border.rounded}

- Apps need RAM / Memory to run. Amount of RAM is allocated by Operating System (OS).
- RAM / Memory is like a huge storeroom with lots of lockers - each locker has an unique ID/address 0x01, 0x02, ... etc. OS will allocate Apps to a set of unique lockers to use.
- Each locker (memory address) can assign to 1 App at anytime.
- OS will manage mappings of all the (App, Memory address) pairs.

Say you've started a Game application on your PC. OS has allocated a chunk of memory addresses for it. We can have another program (with sufficient system accesses + codes to communicate with OS) that access and modify data stored under these memory addresses.

![diagram1](https://chy.my.id/post_data/2/diagram2.png){:.border.rounded}

Source : [Zoar](https://zoar.io/insight/article6.html)

# Read before start reading this article: This tutorial is for educational purposes only. the author(s) has no intention to use the knowledge for any undoings, please make sure that you are not violating the EULA/TOS of the specific game/application.

## Getting Started
So today I will demonstrate how to-do that. I will split this tutorial into 2 category. the first one is Known-value memory scanning and Unknown-value memory scanning. the main difference is you use the method based data what you got. e.g if you dont know what the value for specific action or state you can use the second one, else use the first one.

## Install Cheat Engine
First you need to install Cheat Engine first, Cheat Engine available for Windows operating system. you can download the program here
[Download](https://www.cheatengine.org/downloads.php) In this tutorial im using Cheat Engine version 7.1. for the Installation it was easy, just install like software as usual. Ok now lets go to next step.

## Known-value Memory Scanning
As i said before, this method used if you know the value for something that you wanna know. let say you play a FPS game, and then you want to edit your Health point or gun ammo. in that case you can use this method to do that. Because mostly i play MMORPG game. So now i will do scan to read how much monster available in the Radar in RF Online game. here the outline

1. Open the game
2. Open Cheat Engine
3. Target the game process using Cheat Engine
4. Scan the initial value
5. Move your character so the value in game changed
6. Do a next scan in Cheat Engine to get the Address
7. Repeat Step 5 and 6 until you find the "real address"

Ok now lets go to step 1-3 first. after you open the game and cheat engine. now lets target the game processs like screenshot below 

![Screenshot1](https://chy.my.id/post_data/2/Screenshot_1.png){:.border.rounded}

now lets back to game, and as you can see. there is 2 monster in my game Radar

![Screenshot2](https://chy.my.id/post_data/2/Screenshot_2.png){:.border.rounded}

Because we know the initial value will be 2, so let do first scan using that value, for scan type we use an Exact value and the type is 4-byte

![Screenshot3](https://chy.my.id/post_data/2/Screenshot_3.png){:.border.rounded}

Now after you scan that initial value, in your Cheat Engine left side, you will see a lot of address. to reduce the address. lets move our character away from the monster, so the monster that detected in radar become only 1. 

![Screenshot4](https://chy.my.id/post_data/2/Screenshot_4.png){:.border.rounded}

and then lets go scanning again but now scan with the updated value, in my case it will be 1 and then click **Next Scan**

![Screenshot5](https://chy.my.id/post_data/2/Screenshot_5.png){:.border.rounded}

Now, because my address result still big (150k Address) i will repeat step 5-6 until i got a "real address"

![Screenshot6](https://chy.my.id/post_data/2/Screenshot_6.png){:.border.rounded}
![Screenshot7](https://chy.my.id/post_data/2/Screenshot_7.png){:.border.rounded}

Now only **14 Address** left. lets do it 1 more time

![Screenshot8](https://chy.my.id/post_data/2/Screenshot_8.png){:.border.rounded}
![Screenshot9](https://chy.my.id/post_data/2/Screenshot_9.png){:.border.rounded}

Now we got the "real address", lets add the address by clicking it 2 times. Now everytime you move your character. the value of the address will change based on how much monster that detected in the radar. 

![Screenshot10](https://chy.my.id/post_data/2/Screenshot_10.png){:.border.rounded}

Thats it for Known-value memory scanning. next i will show you how to-do memory scanning for Unknown-value. 

## Unknown-value Memory Scanning
For this Unknown-value memory scanning, I will find what is my current target in game is.. but the problem is, i didnt even know what intial value is. so lets go use this method to find this.

So near my character there is 2 monster, lets name it Monster A and Monster B. First i will change my current target to Monster A

![Screenshot16](https://chy.my.id/post_data/2/Screenshot_16.png){:.border.rounded}

Now let scan using Unknown initial value scan type and 4-byte value type. 

![Screenshot17](https://chy.my.id/post_data/2/Screenshot_17.png){:.border.rounded}

As image above, we got so much address(157 million), lets reduce the address. now back to the game and change our target to Monster B and. and do scan again, but for this time, we change the scan type to **Changed value**, Ok you may ask why **"Changed value"**. Because when we do the first scan our **Current Target is to Monster A** but then we change our **Current Target to Monster B**. so the value must be change. so thats why we use **Change value scan type**. 

now lets do scan again, this time we change our **current target to nothing** and scan again using **Changed value** scan type

![Screenshot18](https://chy.my.id/post_data/2/Screenshot_18.png){:.border.rounded}

Now scan again, but this time we **dont** change our **current target**. so this time we use **Unchanged value** scan type

![Screenshot19](https://chy.my.id/post_data/2/Screenshot_19.png){:.border.rounded}

Now lets repeat that step until you got the **real address** like the image below

![Screenshot20](https://chy.my.id/post_data/2/Screenshot_20.png){:.border.rounded}

Then lets add that one address we found to our address list. 

![Screenshot21](https://chy.my.id/post_data/2/Screenshot_21.png){:.border.rounded}

Monster A have value 196. and Monster B value is 142. 

![Screenshot22](https://chy.my.id/post_data/2/Screenshot_22.png){:.border.rounded}

Now lets change our current target to nothing, the value in our address will be updated to 255 like this image below

![Screenshot23](https://chy.my.id/post_data/2/Screenshot_23.png){:.border.rounded}

Now, double click the value and manually edit the value to Monster B (which 142). If the address is real address. our current target will be change to Monster B automaticly when we change our value in Cheat Engine

![Screenshot24](https://chy.my.id/post_data/2/Screenshot_24.png){:.border.rounded}

Now its working. thats its for Unknown-value memory scanning.

## Find pointer
So what is pointer? in simple way pointer is a variable whose value is the address of another variable, i.e., direct address of the memory location. So the next time you want add the address you dont need to do scanning memory one-by-one like step above, but just add the address manually by input the **Pointer + Offset**

So lets go, I will find the pointer of how many monster in radar that i have write the step above.

Now right click in you address has been add before. and choose Pointer scan for this address

![Screenshot11](https://chy.my.id/post_data/2/Screenshot_11.png){:.border.rounded}

Now in the next step, we just change the Max level to 3. so we will scan faster because Cheat Engine will not scan too deep. 

![Screenshot12](https://chy.my.id/post_data/2/Screenshot_12.png){:.border.rounded}

Here the result, find address that always appear and choose the pointer when the address only have 1 offset ( for most case, this kind type pointer is the pointer that we want)

![Screenshot13](https://chy.my.id/post_data/2/Screenshot_13.png){:.border.rounded}

So this was our pointer "RF_Online.bin"+01F3B6E0 + 170, lets add the pointer manually in Cheat Engine

![Screenshot15](https://chy.my.id/post_data/2/Screenshot_15.png){:.border.rounded}


Then tadaaa, its done. save your pointer. so next time you dont need to do memory scanning from the first time like we do before. 
with this pointer we can just add it manually.
Next post i will show you how to Read and Write to the memory address in C++.
