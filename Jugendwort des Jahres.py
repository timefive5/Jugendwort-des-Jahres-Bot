import requests
import time
import re
import sys


# General values
i           = 0
done_string = '\033[1mFertig\033[0m'
survey_url  = 'https://www.surveymonkey.com/r/7JZRVLJ?embedded=1'
age_groups  = [
("3067519627", "10 bis 15 Jahre"),
("3067519628", "16 bis 20 Jahre"),
("3067519629", "21 bis 30 Jahre"),
("3067519630", "über 30 Jahre")
]


# User-defined values, tweak as you wish
word          = 'Hurensohn' # The word to submit
iterations    = 10          # The number of times to submit the word for each age group
time_interval = 5           # The time interval between submissions in seconds


# Setup
print(f"Beziehe Daten vom Server...", end="")
sys.stdout.flush()
r = requests.get(survey_url)

survey_data = re.search(r'survey_data" value="(.*?)" />', r.text).group(1)
post_data = {
	'463803414'  : "",
	'463803684'  : word,
	'483089934[]': '3189794655',
	'is_previous': 'false',
	'survey_data': survey_data,
	'disable_survey_buttons_on_submit': ''
}

print(done_string)


# Main loop
while i < iterations:
	
	# Go through each age group
	for age_key, age_string in age_groups:
		
		# Set age group for next submission
		post_data["463803414"] = age_key
		
		# Wait the specified amount of time
		print(f"Warte {time_interval} Sekunde(n)...", end="")
		sys.stdout.flush()
		time.sleep(time_interval)
		print(done_string)
		
		# Submit survey
		print(f'Stimme ab mit der Altersgruppe "{age_string}"...', end="")
		sys.stdout.flush()
		requests.post(survey_url, data=post_data)
		print(done_string)
		print()
