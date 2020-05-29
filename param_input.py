#!/usr/bin/python2.7
import string_validator
import getopt, sys

source_user   = ""
source_domain = "default.domain"
target_user   = ""
target_domain = ""
assume_yes    = False

try:
    short_options = "u:d:t:n:y"
    long_options = ["source-user=", "source-domain=", "target-user=", "target-domain=", "assume-yes"]
    arguments, values = getopt.getopt(sys.argv[1:], short_options, long_options)

    # Evaluate given options
    for current_argument, current_value in arguments:
        if current_argument in ("-u", "--source-user"):
            source_user = current_value
        elif current_argument in ("-d", "--source-domain"):
            source_domain = current_value
        elif current_argument in ("-t", "--target-user"):
            target_user = current_value
        elif current_argument in ("-n", "--target-domain"):
            target_domain = current_value
        elif current_argument in ("-y", "--assume-yes"):
            assume_yes = True
except getopt.error as err:
    # Output error, and return with an error code
    print (str(err))
    sys.exit(2)

validate = string_validator.StringValidator()
if validate.is_username(source_user):
    print (("Source user login:  %s") % (source_user))
else:
    print (("Incorrect format for 'source_user'. Accepted 'user.name', '%s' provided") % (source_user))
print (("Soure user domain:  %s") % (source_domain))
print (("Target user login:  %s") % (target_user))
if not target_domain: target_domain = source_domain
print (("Target user domain: %s") % (target_domain))
if assume_yes : print ("Assumes 'yes' for every prompt")
