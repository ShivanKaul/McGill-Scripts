import cookielib
import mechanize as mech
import sys

USERNAME = sys.argv[1]
PASSWORD = sys.argv[2]

URL = "https://mycourses2.mcgill.ca/Shibboleth.sso/Login?entityID=https://shibboleth.mcgill.ca/idp/shibboleth&amp;target=https%3A%2F%2Fmycourses2.mcgill.ca%2Fd2l%2FshibbolethSSO%2Flogin.d2l"

br = mech.Browser()
cj = cookielib.LWPCookieJar()
br.set_cookiejar(cj)
br.open("https://mycourses2.mcgill.ca/Shibboleth.sso/Login?entityID=https://shibboleth.mcgill.ca/idp/shibboleth&amp;target=https%3A%2F%2Fmycourses2.mcgill.ca%2Fd2l%2FshibbolethSSO%2Flogin.d2l")
br.set_handle_robots(False)
br.select_form(nr=0)
br.form["j_username"] = USERNAME
br.form["j_password"] = PASSWORD
#br.submit()
response = br.submit()
br.select_form(nr=0)
response2 = br.submit()
print response2.read()


response3 = br.open("https://mycourses2.mcgill.ca/d2l/le/140311/discussions/threads/230632/View")
print response3.read()
#print br.response()
#print br.response().readline()
