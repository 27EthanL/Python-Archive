'''
Hey there! How have you been? I've been great! I just learned about this really cool type of cipher called a Caesar Cipher. 
Here's how it works: You take your message, something like "hello" and then you shift all of the letters by a certain offset. 
For example, if I chose an offset of 3 and a message of "hello", I would code my message by shifting each letter 3 places to the left (with respect to the alphabet). 
So "h" becomes "e", "e" becomes, "b", "l" becomes "i", and "o" becomes "l". Then I have my coded message, "ebiil"! 
Now I can send you my message and the offset and you can decode it. 
The best thing is that Julius Caesar himself used this cipher, that's why it's called the Caesar Cipher! 
Isn't that so cool! Okay, now I'm going to send you a longer coded message that you have to decode yourself!

xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!

This message has an offset of 10. Can you decode it?
'''

# Decoding with Offset = 10
def decoding_10():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = 'xuo jxuhu! jxyi yi qd unqcfbu ev q squiqh syfxuh. muhu oek qrbu je tusetu yj? y xefu ie! iudt cu q cuiiqwu rqsa myjx jxu iqcu evviuj!'
    decoded_message = ''
    for letter in encoded_message:
        if letter in alphabet:
            decoded_message += alphabet[(alphabet.find(letter) + 10) % 26]
        else:
            decoded_message += letter
    print(decoded_message)

# decoding_10()

'''
Great job! 
Now send Vishal back a message using the same offset. 
Your message can be anything you want! 
Remember, coding happens in opposite direction of decoding.
'''

# Encoding with Offset = 10
def encoding_10():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_message = 'among us!'
    encoded_message = ''
    for letter in decoded_message:
        if letter in alphabet:
            encoded_message += alphabet[(alphabet.find(letter) - 10) % 26]
        else:
            encoded_message += letter
    print(encoded_message)
    
# encoding_10
    
'''
You're getting the hang of this! 
Okay here are two more messages, 
the first one is coded just like before with an offset of ten, 
and it contains the hint for decoding the second message!

First message:

jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.

Second message:

bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!

If you haven't already, define two functions decoder(message, offset) and coder(message, offset) that can be used to quickly decode and code messages given any offset.
'''

# Decoder
def decoder(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = message
    decoded_message = ''
    for letter in encoded_message:
        if letter in alphabet:
            decoded_message += alphabet[(alphabet.find(letter) + offset) % 26]
        else:
            decoded_message += letter
    print(decoded_message)
    
# Encoder
def encoder(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    decoded_message = message
    encoded_message = ''
    for letter in decoded_message:
        if letter in alphabet:
            encoded_message += alphabet[(alphabet.find(letter) - offset) % 26]
        else:
            encoded_message += letter
    print(encoded_message)
    
# decoder('jxu evviuj veh jxu iusedt cuiiqwu yi vekhjuud.', 10)
# decoder('bqdradyuzs ygxfubxq omqemd oubtqde fa oapq kagd yqeemsqe ue qhqz yadq eqogdq!', 14)

'''
Hello again friend! 
knew you would love the Caesar Cipher, it's a cool simple way to encrypt messages. 
Did you know that back in Caesar's time, it was considered a very secure way of communication and it took a lot of effort to crack if you were unaware of the value of the shift? 
That's all changed with computers! 
Now we can brute force these kinds of ciphers very quickly, as I'm sure you can imagine.

To test your cryptography skills, this next coded message is going to be harder than the last couple to crack. 
It's still going to be coded with a Caesar Cipher but this time I'm not going to tell you the value of the shift. 
You'll have to brute force it yourself.

Here's the coded message:

vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.

Good luck!
'''

# Brute Forcing
def brute_forcing(message):
    for attempt in range(1, 26):
        print('Attempt #', attempt)
        decoder(message, attempt)

# brute_forcing("vhfinmxkl atox kxgwxkxw tee hy maxlx hew vbiaxkl tl hulhexmx. px'ee atox mh kxteer lmxi ni hnk ztfx by px ptgm mh dxxi hnk fxlltzxl ltyx.")

'''
Salutations! 
As you can see, technology has made brute forcing simple ciphers like the Caesar Cipher extremely easy, 
and us crypto-enthusiasts have had to get more creative and use more complicated ciphers. 
This next cipher I'm going to teach you is the Vigenère Cipher, 
invented by an Italian cryptologist named Giovan Battista Bellaso (cool name eh?) in the 16th century, 
but named after another cryptologist from the 16th century, Blaise de Vigenère.

The Vigenère Cipher is a polyalphabetic substitution cipher, 
as opposed to the Caesar Cipher which was a monoalphabetic substitution cipher. 
What this means is that opposed to having a single shift that is applied to every letter, 
the Vigenère Cipher has a different shift for each individual letter. 
The value of the shift for each letter is determined by a given keyword.

Consider the message

barryisthespy

If we want to code this message, first we choose a keyword. For this example, we'll use the keyword

dog

Now we use the repeat the keyword over and over to generate a _keyword phrase_ that is the same length as the message we want to code. 
So if we want to code the message "barryisthespy" our _keyword phrase_ is "dogdogdogdogd". 
Now we are ready to start coding our message. 
We shift the first letter by the difference between the place value of the first letter in the message and the place value of the first letter in the keyword phrase.

message:       b  a  r  r  y  i  s  t  h  e  s  p  y

keyword phrase:       d  o  g  d  o  g  d  o  g  d  o  g  d

difference in place value:       2  14 15 12 16 24 11 21 25 22 22 17 5

So we shift "b" by four places and get "e", 
we shift "a" by 14 places and get "o", 
we shift "r" by 15 places and get "x", 
shift the next "r" by 12 places and "u", and so forth. 
Once we complete all the shifts we end up with our coded message:

eoxumovhnhgvb

As you can imagine, this is a lot harder to crack without knowing the keyword! 
So now comes the hard part. I'll give you a message and the keyword, 
and you'll see if you can figure out how to crack it! 
Ready? 
Okay here's my message:

dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!

and the keyword to decode my message is 

friends

Because that's what we are! Good luck friend!
'''

# Decoding - Keyword = Friends
def decoding_friends():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    encoded_message = 'dfc jhjj ifyh yf hrfgiv xulk? vmph bfzo! qtl eeh gvkszlfl yyvww kpi hpuvzx dl tzcgrywrxll!'
    decoded_message = ''
    enscribed_message = ''
    keyword = 'friends'
    count = 0
    for letter in encoded_message:
        if letter in alphabet:
            enscribed_message += keyword[count]
            count = (count + 1) % 7
        else:
            enscribed_message += letter
    print(enscribed_message)
decoding_friends()