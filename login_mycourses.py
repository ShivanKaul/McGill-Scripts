import cookielib
import mechanize as mech
import getpass
import sys

###### NOTE: NOT TESTED. I seem to be able to login fine, but not sure why I can't fetch PDFs. Try it and let me know ######

def main():

	USERNAME = raw_input('Enter your McGill email: ')
	PASSWORD = getpass.getpass('Enter McGill password: ')

	# Browser
	br = mech.Browser()
	# Cookie jar
	cj = cookielib.LWPCookieJar()
	br.set_cookiejar(cj)

	# Open URL for Shibboleth
	br.open("https://mycourses2.mcgill.ca/Shibboleth.sso/Login?entityID=https://shibboleth.mcgill.ca/idp/shibboleth&amp;target=https%3A%2F%2Fmycourses2.mcgill.ca%2Fd2l%2FshibbolethSSO%2Flogin.d2l")

	# Browser options
	br.set_handle_equiv(True)
	br.set_handle_redirect(True)
	br.set_handle_referer(True)
	br.set_handle_robots(False)
	br.set_handle_refresh(mech._http.HTTPRefreshProcessor(), max_time=1)

	# Headers
	br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.101 Safari/537.36'), ('accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'), ('Accept-Language', 'en-US,en;q=0.8'), ('accept-encoding', 'gzip, deflate'), ('Cache-Control', 'max-age=0'), ('Connection', 'keep-alive'), ('Host', 'shibboleth.mcgill.ca'), ('Origin', 'https://shibboleth.mcgill.ca')]

	# Get first form on page and fill
	br.select_form(nr=0)
	br.form["j_username"] = USERNAME 
	br.form["j_password"] = PASSWORD

	# Submit
	response = br.submit()

	br.select_form(nr=0)
	rs = br.submit()


if __name__ == "__main__":
	main()
