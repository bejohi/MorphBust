# The make tool should be included in your unix environment.
# # On Windows Host you have to install the GNU Tools first.
# # Open a terminal cd to the directory the MAKEFILE is located.
# # The run "make <cmd>", where <cmd> is one of the below commands.
#
# # if you have python2 and python3 installed the pip cmd might by pip3
# # otherwise only pip
 pipversion = pip3
 pythonversion = python
#
# # Installs all necessary external python libraries.
 install-requirements:
				pip install -r requirements 
#         # Starts the application
	run:
        $(pythonversion) src/main.py

# Runs all unit tests
 	test:
         python3 -m unittest discover -s . -p '*_test.py'

         release: install-requirements test run

