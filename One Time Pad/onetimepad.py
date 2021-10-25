import random
import string
alphabet = list(string.ascii_letters+'1234567890')
text = input('Enter text here: ')
encrypted_text,l = '',[]
# Main encryption algorithm
for t in text:
    if t!=' ':
        s = random.randint(1,26)
        if alphabet.index(t)+s>=len(alphabet):
            l.append(s)
            s-=(len(alphabet)-alphabet.index(t)-1)
            encrypted_text+=alphabet[s]
        else:
            encrypted_text+=alphabet[alphabet.index(t)+s]
            l.append(s)
    else:
        encrypted_text+=' '
print('')
print('Original text:',text); print('')
print('Encrypted text:',encrypted_text); print('')
print('List of random dice rolls:',l); print('')
print('Number of Trials to break:',str(26**len(text))); print('')
