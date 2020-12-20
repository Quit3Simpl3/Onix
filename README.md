# Onix
Get yourself a nice, strong, memorable password instantly.

USAGE:
1. Provide a dictionary.txt file containing the words you would like to use as passwords.
2. Running:
    from onix import Onix
    # Create random password with a length of 8 characters from the dictionary.txt file with the word 'badword' banned:
    onix = Onix(length=8, plaintext="", options="123", banned="badword")
    # Turn 'mypassword' into a hardened password:
    onix = Onix(plaintext="mypassword", options="123")
