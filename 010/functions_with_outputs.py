def captalize_names(f_name, l_name):
    """Take a first and last name and format it
    to return the title case version of the name."""
    return f"{f_name} {l_name}".title()


complete_name = captalize_names("ISABELLA", "silva")
print(complete_name)
print(captalize_names("ISABELLA", "silva"))
