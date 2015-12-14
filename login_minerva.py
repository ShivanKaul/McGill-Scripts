import mechanize as mech
import getpass
import sys

def main():
	USERNAME = raw_input('Enter your McGill email: ')
	PASSWORD = getpass.getpass('Enter McGill password (won\'t show up): ')

	### NOTE: I was trying to use Mechanize to get MyCourses stuff, which is why I had to add all the headers and bother with cookies et al. I probably don't need all this for Minerva ###

	NAME = USERNAME.rsplit('@', 1)[0].title().replace(".", "")
	# Browser
	br = mech.Browser()
	# Cookie jar
	cj = mech.LWPCookieJar()
	br.set_cookiejar(cj)

	# Define URLs
	URL = "https://horizon.mcgill.ca/pban1/" 
	URL_transcript = "bzsktran.P_Display_Form?user_type=S&tran_type=V"
	URL_login = "twbkwbis.P_WWWLogin"

	# Open authentication URL for Minerva
	br.open(URL + URL_login)

	# Browser options. NOTE: Probably don't need these for Minerva.
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mech._http.HTTPRefreshProcessor(), max_time=1)

	# Headers. NOTE: Probably don't need these for Minerva.
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'), ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), ('Accept-Language', 'en-US,en;q=0.8')]

	# Get form on page and fill
	br.select_form(nr=0)
	br.form["sid"] = USERNAME
	br.form["PIN"] = PASSWORD

	# Submit login credentials
	response = br.submit()

	if 'Failure' in response.read():
		print("Invalid McGill username/password. Your mother would be ashamed of you.")
		exit()


	print("Fetching transcript.html... By the way, you should be studying right now.")

	# Download transcript
	response2 = br.open(URL + URL_transcript)

	# Get response data
	tr = response2.read()

	###### BEWARE! EXTREMELY HACKY STRING EDITING, PLEASE IMPROVE THIS, I HAVE AN EXAM TOMORROW ######
	tr = tr[tr.index('<TABLE  CLASS="dataentrytable"'):]
	tr = tr[:tr.index('<TABLE  CLASS="plaintable')]

	# Save transcript to disk
	transcript = open(NAME + "-UnofficialTranscript.html", "w")
	transcript.write(tr)
	transcript.close()

	print("Done. Have a nice day.")

if __name__ == "__main__":
	main()
