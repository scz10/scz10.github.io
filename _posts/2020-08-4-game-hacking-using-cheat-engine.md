---
title: Game Hacking - Using Cheat Engine to-do Memory Scanning
mode: immersive
header:
  theme: dark
article_header:
  type: overlay
  theme: dark
  background_color: '#123'
  background_image: false
tags: [game-hacking,memory-scanning]
key: game-hacking-1
---
# Background
Applications uses RAM / Memory to store data variables - You can access and manipulate these data in realtime.
So how does it work? To understand this better here's a quick summary of how Apps / RAM works:
```
![diagram1](https://chmy.xyz/post_data/2/diagram1.png){:.border.rounded}
- Apps need RAM / Memory to run. Amount of RAM is allocated by Operating System (OS).
- RAM / Memory is like a huge storeroom with lots of lockers - each locker has an unique ID/address 0x01, 0x02, ... etc. OS will allocate Apps to a set of unique lockers to use.
- Each locker (memory address) can assign to 1 App at anytime.
- OS will manage mappings of all the (App, Memory address) pairs.

Say you've started a Game application on your PC. OS has allocated a chunk of memory addresses for it. We can have another program (with sufficient system accesses + codes to communicate with OS) that access and modify data stored under these memory addresses.

![diagram1](https://chmy.xyz/post_data/2/diagram2.png){:.border.rounded}

Source : https://zoar.io/insight/article6.html

```
So today I will demonstrate how to-do that. I will split this tutorial into 2 category. the first one is Known-value memory scanning and Unknown-value memory scanning. the main difference is you use the second one if you dont know what the value for specific action or state. 

