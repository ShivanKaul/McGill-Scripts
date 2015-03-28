Minerva Transcript Fetcher, and MyCourses CLI logon  
-----------
Uses Mechanize to fetch transcript from Minerva, and authenticate from the CLI for MyCourses.  

Usage:  
-----------
To get your transcript, type:
<pre><code>python login_minerva.py</code></pre>You will be prompted for your McGill username and password. If you want to login into your MyCourses from the CLI, use this script:  
<pre><code>python login_mycourses.py</code></pre>However, not sure if it's working. Haven't gotten time to test.

 Requirements:
------
Python 2.7+  
Mechanize (To get mechanize, use your package manager; if you're on Debian/Ubuntu, just type `sudo apt-get install python-mechanize`. Else, you could use pip to get mechanize thusly: `pip install mechanize`. To get pip, use easy_install: `easy_install pip`. To get easy_install, use your package manager {or `sudo apt-get install python-setuptools python-dev build-essential` on Debian})
