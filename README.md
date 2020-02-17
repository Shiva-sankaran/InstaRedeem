# break-the-crowd
# 17-02-2020

uses selenium to get free codes in free fire ( game ) from instagram posts and enters in the redemption site

Lots of offers and freebies are given as reddemable codes which is usually posted in instagram as stories but, these freebies have lot of competiton. This is where this code can be used it can redeem a code in less than 15 seconds and 20 codes in less than 2 minutes (actual time will depend on system and network). In this program i have used to get codes to a battle royal game.In case of more than 1 code being given in the story this program opens multiple tabs and runs them parallely.

Pre-requisites

see the first few lines of code to see the modules needed and install them
create a directory in /home as "insta_video" 
Make a custom firefox profile 
  - eneable "always do this option" for the download prompt in firefox
  -change location of downloaded files into insta_video instead of downloads.
  - sign in once in the redemption site and allow cookies for password to get stored.

This is done using " storydownloader.net" from where instagram stories are downloaded but can be extended to other similar websites ( NOTE: when changing site the Xpath and web elements must also be changed)

Since the option of opening multiple tabs have been removed in selenium (i searched the web cant find anything useful). A workaround was used by :-

-> google.com was first opened and searched for the site accurately so that the site comes as the first result.
-> The first result was clicked multiple times to open multiple tabs of the same site 

please feel free to use this code anywhere you like.

