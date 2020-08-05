# Shadow-file-generator
A random shadow file generator, for use with [shadow file cracker](https://github.com/necaro55/Shadow-file-cracker).
This script generates a random number of entries of the /etc/shadow file simulating users with encrypted passwords, the usernames and the passwords are generated using
a wordlist text file, some random number of users are generated with unfeasible to crack passwords and the root user password is also randomly crackable.

## Usage
The script accepts two arguments, the file path to the wordlist text file and the number of non root user entries. The root user is added to this number, if no number of entries is given it generates random entries beetween 1 and 3.

hash_generator.py [Path to wordlist file] [Number of non root users]

At least one password entry is crackable every time using the word list text file .
