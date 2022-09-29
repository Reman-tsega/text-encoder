# list of alphabet
# encode each letter by shifting .index 
# take input from user 
# ask for shifter

alphabet =["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"," ","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
encoded_word = []
decoded_word=[]

def encoder(word,shifter):
    for z in range(0, len(word)-1):
        position=alphabet.index(word[z])
        new_position = position+shifter
        encoded_letter = alphabet[new_position] 
        encoded_word.append(encoded_letter)
        encoded_message = "".join(encoded_word)
        with open("./encoded_message.txt","w") as f:
            f.write(encoded_message)
    print(f"encoded word is { encoded_message  }")


# ______________-decoder____________-
def decoder(shifter):
    for y in range(len(decoded_letter)):
        position = alphabet.index(decoded_letter[y])
        new_position = position-shifter
        decoded_let = alphabet[new_position]
        decoded_word.append(decoded_let)
        decoded_message = "".join(decoded_word)
    print(f"docoded word is {decoded_message}")


    
    
# save the encoded message into file dir encoded message
with open('encoded_message.txt','r') as f:
    decoded_letter = f.read()


want = input("what do u want \'encode\' or \'decode\' ")

if want=="encode":
    word = input(" enter a message to be sent : \n")
    shifter = int(input("enter a shifter number :  \n"))
    encoder(word,shifter)
else:
    shifter = int(input("enter a shifter number :  \n"))
    decoder(shifter)


