import random
import string


def generate_password(min_lenght, numbers=True, special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation


    characters = letters
    if numbers:
        characters += digits  
    if special_characters:
        characters += special
       
    pwd = ""
    meets_criteria = False
    has_numbers = False
    has_special = False

    while not meets_criteria or len(pwd) < min_lenght:
        new_char = random.choice(characters)
        pwd += new_char


        if new_char in digits:
            has_numbers = True
        elif new_char in special:
            has_special = True

        meets_criteria = True 
        if numbers:
            meets_criteria = has_numbers
        if special_characters:
            meets_criteria = meets_criteria and has_special
    return pwd

min_lenght = int(input("Entre com o minimo de tamanho"))
has_number = input("Quer que tenha numeros  (s/n)? ").lower() == "s"
has_special = input("Quer que tenha numeros especiais  (s/n)? ").lower() =="s"
pwd = generate_password(min_lenght, has_number, has_special)
print("A senha gerada foi:", pwd)





