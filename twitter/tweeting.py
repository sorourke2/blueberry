
#!/usr/bin/env python
import sys
from twython import Twython

from datetime import datetime

now = datetime.now();
current_time = now.strftime("%H:%M:%S")
print("=",current_time)
 

if 0 == 1: 
	tweetStr = "RIP Peeraphan Palusuk, 68, Thai politician, Minister of Science and Technology (since 2013), MP for Yasothon (since 1985)"
	# your twitter consumer and access information goes here
	# note: these are garbage strings and won't work
	apiKey = 'eDmEXJF5ymgJqt1q33OljC0fo'
	apiSecret = 'sj4KlgbElC7yW12R1vVDIfQItXy30FPtCtllMwxGxL70nyAEgc'
	accessToken = '1205580133244911616-ROLSWOoFbp2uZ88Shxx4TmfXtqr28i'
	accessTokenSecret = 'Jwjtkvlf4REc6pO2j5PUptLVKoh202zBO1ELcc6h7a21A' 
	api = Twython(apiKey,apiSecret,accessToken,accessTokenSecret) 
	api.update_status(status=tweetStr)
	print "Tweeted" +tweetStr       
                        
