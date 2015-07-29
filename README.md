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
* **Python** 2.7
* Note: there's no official support for Python 3+ for `mechanize`, the headless browser library that the script uses. There are workarounds; if you have the time, you could [port the script to Python 3+ by forking it and sending a Pull Request](https://github.com/ShivanKaul/mcgill-scripts#fork-destination-box).
* **Mechanize** 
	* (To get mechanize, use your package manager; if you're on Debian/Ubuntu, just type `sudo apt-get install python-mechanize`. Else, you could use pip to get mechanize thusly: `pip install mechanize`. To get pip, use easy_install: `easy_install pip`. To get easy_install, use your package manager {or `sudo apt-get install python-setuptools python-dev build-essential` on Debian})
