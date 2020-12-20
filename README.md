# Onix
Get yourself a nice, strong, memorable password instantly.

### USAGE:
1. Provide a dictionary.txt file containing the words you would like to use as passwords.
2. Running:
2.1. Import the Onix class:
```
    from onix import Onix
```
2.2. Create random password with a length of 8 characters from the dictionary.txt file with the word 'badword' banned:
```
    onix = Onix(length=8, plaintext="", options="123", banned="badword")
```
2.3. Turn 'mypassword' into a hardened password:
```
    onix = Onix(plaintext="mypassword", options="123")
```
