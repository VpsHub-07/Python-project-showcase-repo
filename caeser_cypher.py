letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',]


should_continue=True

def caeser(original_text, shift_amount, encode_or_decode  ):
    original_text=original_text.lower()
    rearrenged_letter=""
    if encode_or_decode =="encode":
        shift_amount *= -1
    for letter in original_text:
        if letter not in letters:
            rearrenged_letter+=letter
        else:
            shift=letters.index(letter)-shift_amount
            shift%=len(letters)       
            rearrenged_letter+=letters[shift]
    print(f"Your {encode_or_decode}d message is {rearrenged_letter}")

while should_continue:
    text=input("Enter a message: ").lower()
    shi=int(input("Enter shift amount: "))
    direction=input("Do you want to encode or decode: ").lower()
    caeser(text, shi, direction)
    restart= input("Type 'yes' to do it again. Otherwise type 'no'.\n").lower()
    if restart == "no":
        should_continue=False
        print("Goodbye")