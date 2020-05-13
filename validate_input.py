import re

def input_value(prompt, regex, default = None):
    while True:
        value = raw_input(prompt)
        if not value and not default is None:
            value = default
        if not regex.match(value):
            print("Incorrect format. Please try again.")
            continue
        else:
            break
    return value

username_regex = re.compile("^[a-z]+\.[a-z]+$")
domain_regex   = re.compile("^[a-zA-Z0-9u00a1-\uffff0-]{2,}\.[a-zA-Z0-9u00a1-\uffff0-]{2,}(\S*)$")

source_user     = input_value("User login [firstname.lastname]: ", username_regex)
source_domain   = input_value("User domain [helpling.com]: ", domain_regex, "helpling.com")
redirect_user   = input_value("Redirect user login [firstname.lastname]: ", username_regex)
redirect_domain = input_value("Redirect user domain [" + source_domain + "]: ", domain_regex, source_domain)

print("User login is " + source_user)
print("User domain is " + source_domain)
print("Redirect user is " + redirect_user)
print("Redirect user domain " + redirect_domain)

while True:
    proceed = raw_input("Proceed (y/n)?")
    if proceed == "y":
        print("We proceed")
        break
    elif proceed == "n":
        print("Abort")
        break
    else:
        continue
