import twitter, requests, time, json 

twitter_consumer_key = '__'
twitter_consumer_secret = '__'
twitter_access_token = '__'
twitter_access_secret = '__'

twitter_api = twitter.Api(consumer_key=twitter_consumer_key, consumer_secret=twitter_consumer_secret, access_token_key=twitter_access_token, access_token_secret=twitter_access_secret)

handle = '@DanielStinDiess'

def formatTime(val):
	weekdays = ['Mon ', 'Tue ', 'Wed ', 'Thu ', 'Fri ', 'Sat ', 'Sun ']
	months = ['Jan ', 'Feb ', 'Mar ', 'Apr ', 'May ', 'Jun ', 'Jul ', 'Aug ', 'Sep ', 'Oct ', 'Nov ', 'Dec ']
	UTC_time = ""

	UTC_time += weekdays[val.tm_wday] + months[val.tm_mon - 1]

	# Right Align Days
	UTC_time += rightAlign(val.tm_mday) + ' '

	# Right Align Hours
	UTC_time += rightAlign(val.tm_hour) + ':'

	# Right Align Mins
	UTC_time += rightAlign(val.tm_min) + ':'

	# Right Align Secs
	UTC_time += rightAlign(val.tm_sec) + ' '
	
	# Format with year
	UTC_time += '+0000 ' + str(val.tm_year)

	return UTC_time

def rightAlign(number):
	string = "";

	if number < 10:
		string += '0' + str(number)
	else:
		string += str(number)

	return string

while True:
	statuses = twitter_api.GetUserTimeline(screen_name=handle, count=10, include_rts=True)

	UTC_time = formatTime(time.gmtime())

	for status in statuses:
		if UTC_time == status.created_at:
			print("LIVE")
		else:
			print("----")