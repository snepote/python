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

username_regex  = re.compile("^[a-z]+\.[a-z]+$")
domain_regex    = re.compile("^[a-zA-Z0-9u00a1-\uffff0-]{2,}\.[a-zA-Z0-9u00a1-\uffff0-]{2,}(\S*)$")

source_user     = input_value("User login (format: firstname.lastname): ", username_regex)
source_domain   = input_value("User domain [example.com]: ", domain_regex, "helpling.com")
redirect_user   = input_value("Redirect user login (format: firstname.lastname): ", username_regex)
redirect_domain = input_value("Redirect user domain [" + source_domain + "]: ", domain_regex, source_domain)

print("We will redirect <%s@%s> to <%s@%s>" %(source_user, source_domain, redirect_user, redirect_domain))

while True:
    proceed = raw_input("Proceed (y/n)? ")
    if proceed == "y":
        print("We proceed")
        break
    elif proceed == "n":
        print("Abort")
        break
    else:
        continue
