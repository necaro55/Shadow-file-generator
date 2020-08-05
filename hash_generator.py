#hash_generator.py
#This script generates a random number of entries of the /etc/shadow file simulating users with encrypted passwords, the usernames and the passwords are generated using
#a text file, some random number of users are generated with unfeasible to crack passwords and the root user password is also randomly crackable. The script accepts two
#arguments, the file path to the text file and the number of entries plus the root user, if no number of entries is given it generates random entries beetween 1 and 3.
#At least one password entry is crackable every time using the text file word list.
import crypt
import sys
import random
import string

def make_entry(f):#Makes each entry of the shadow file, it receives a list with the username and the password
    return "{}:{}:{}:0:99999:{}:::".format(f[0], crypt.crypt(f[1], crypt.mksalt(crypt.METHOD_SHA512)), random.randint(10000, 20000), random.randint(1,10))
def random_string():#Generates a random string of 15 to 20 charateres including lowercase,digits and punctution
    return "".join(random.choices(string.ascii_lowercase + string.digits + string.punctuation, k= random.randint(15,20)))

def make_user(wordlist,how_many = False):#Creates the users, receives the wordlist from the text file and how many users to create if specified, returns a list of all users entries
    
    how_many -= 1
    w = [password.rstrip() for password in list(wordlist)]
    y = []
    if not how_many:
        how_many = random.randint(1, 3)
    uncrackable = random.randint(0 , how_many-1) #How many users to create if not specified and how many will be uncrackable
    how_many = how_many - uncrackable
    for _ in range(0, how_many):
        y.append(make_entry(random.choices(w, k=2)))
    for _ in range(0, uncrackable):
        y.append(make_entry([random.choice(w), random_string()]))
    if random.getrandbits(1): #if root will be crackable or not
        y.append(make_entry(["root", random_string()]))
    else:
        y.append(make_entry(["root", random.choice(w)]))
    return y
    
if __name__ == "__main__":
    reader = open(sys.argv[1], "r")
    writer = open("shadow", "w")
    try:
        #print("\n".join(make_user(reader)))
        y = []
        writer.write("\n".join(random.sample(y := make_user(reader, int(sys.argv[2])), len(y)))) #writes to a file called shadow
    
    finally:
        reader.close()
        writer.close()
