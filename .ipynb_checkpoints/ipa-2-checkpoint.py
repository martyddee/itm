'''Individual Programming Assignment 2

70 points

This assignment will develop your proficiency with Python's control flows.
'''

def shift_letter(letter, shift):
    '''Shift Letter.
    5 points.

    Shift a letter right by the given number.
    Wrap the letter around if it reaches the end of the alphabet.

    Examples:
    shift_letter("A", 0) -> "A"
    shift_letter("A", 2) -> "C"
    shift_letter("Z", 1) -> "A"
    shift_letter("X", 5) -> "C"
    shift_letter(" ", _) -> " "

    *Note: the single underscore `_` is used to acknowledge the presence
        of a value without caring about its contents.

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    shift: int
        the number by which to shift the letter.

    Returns
    -------
    str
        the letter, shifted appropriately, if a letter.
        a single space if the original letter was a space.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shift = shift % 26
    
    if ord(letter) == 32:
        shifted_letter = " "
    else:
        new_letter = ord(letter) + shift
        while new_letter > 90:
            new_letter = 65 + (new_letter - 91)
            break
        shifted_letter = chr(new_letter)
    
    return shifted_letter

def caesar_cipher(message, shift):
    '''Caesar Cipher.
    10 points.

    Apply a shift number to a string of uppercase English letters and spaces.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    shift: int
        the number by which to shift the letters.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    shift = shift % 26
    all_caps_message = message.upper()
    shifted_message = ""
    
    for character in all_caps_message:
        if ord(character) == 32:
            shifted_message += " "
        else:
            new_character = ord(character) + shift
            while new_character > 90:
                new_character = 65 + ord(character) + shift - 91
                break
            shifted_message += chr(new_character)
    
    return shifted_message

def shift_by_letter(letter, letter_shift):
    '''Shift By Letter.
    10 points.

    Shift a letter to the right using the number equivalent of another letter.
    The shift letter is any letter from A to Z, where A represents 0, B represents 1,
        ..., Z represents 25.

    Examples:
    shift_by_letter("A", "A") -> "A"
    shift_by_letter("A", "C") -> "C"
    shift_by_letter("B", "K") -> "L"
    shift_by_letter(" ", _) -> " "

    Parameters
    ----------
    letter: str
        a single uppercase English letter, or a space.
    letter_shift: str
        a single uppercase English letter.

    Returns
    -------
    str
        the letter, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    if ord(letter) == 32:
        shifted_letter = " "
    else:
        new_letter_shift = ord(letter_shift) - 65
        new_letter = ord(letter) + new_letter_shift
        while new_letter > 90:
            new_letter = 65 + (new_letter - 91)
            break
        shifted_letter = chr(new_letter)
    
    return shifted_letter

def vigenere_cipher(message, key):
    '''Vigenere Cipher.
    15 points.

    Encrypts a message using a keyphrase instead of a static number.
    Every letter in the message is shifted by the number represented by the
        respective letter in the key.
    Spaces should be ignored.

    Example:
    vigenere_cipher("A C", "KEY") -> "K A"

    If needed, the keyphrase is extended to match the length of the key.
        If the key is "KEY" and the message is "LONGTEXT",
        the key will be extended to be "KEYKEYKE".

    Parameters
    ----------
    message: str
        a string of uppercase English letters and spaces.
    key: str
        a string of uppercase English letters. Will never be longer than the message.
        Will never contain spaces.

    Returns
    -------
    str
        the message, shifted appropriately.
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    message = message.upper()
    key = key.upper()
    length = len(message)
    
    extended_key = (key * (length // len(key))) + key[:length % len(key)]
    # 1st term: gets the integer of how many times the length of "key" can fit in the length of the message"
    # 2nd term: gets the remainder of the key that can only fit a part of its length
    # extended the length of the key to equal the length of the message ensure that each character in the message has its own key
    
    shifted_message = ""
    for i in range(length):
        character = message[i]
        shift = extended_key[i]
        # matches up the characters of both the message and the extended key that share the same index
        
        if ord(character) == 32:
            shifted_message += " "
        else:
            key_shift = ord(shift) - 65
            new_character = ord(character) + key_shift
            while new_character > 90:
                new_character = 65 + ord(character) + key_shift - 91
                break
            shifted_message += chr(new_character)
    
    return shifted_message

def scytale_cipher(message, shift):
    '''Scytale Cipher.
    15 points.

    Encrypts a message by simulating a scytale cipher.

    A scytale is a cylinder around which you can wrap a long strip of
        parchment that contained a string of apparent gibberish. The parchment,
        when read using the scytale, would reveal a message due to every nth
        letter now appearing next to each other, revealing a proper message.
    This encryption method is obsolete and should never be used to encrypt
        data in production settings.

    You may read more about the method here:
        https://en.wikipedia.org/wiki/Scytale

    You may follow this algorithm to implement a scytale-style cipher:
    1. Take a message to be encoded and a "shift" number.
        For this example, we will use "INFORMATION_AGE" as
        the message and 3 as the shift.
    2. Check if the length of the message is a multiple of
        the shift. If it is not, add additional underscores
        to the end of the message until it is.
        In this example, "INFORMATION_AGE" is already a multiple of 3,
        so we will leave it alone.
    3. This is the tricky part. Construct the encoded message.
        For each index i in the encoded message, use the character at the index
        (i // shift) + (len(message) // shift) * (i % shift) of the raw message.
        If this number doesn't make sense, you can play around with the cipher at
         https://dencode.com/en/cipher/scytale to try to understand it.
    4. Return the encoded message. In this case,
        the output should be "IMNNA_FTAOIGROE".

    Example:
    scytale_cipher("INFORMATION_AGE", 3) -> "IMNNA_FTAOIGROE"
    scytale_cipher("INFORMATION_AGE", 4) -> "IRIANMOGFANEOT__"
    scytale_cipher("ALGORITHMS_ARE_IMPORTANT", 8) -> "AOTSRIOALRH_EMRNGIMA_PTT"

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the encoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    length = len(message)
    
    if shift <= 0:
        return "error"
    elif length == 0:
        return ""
    elif length % shift == 0:
        pass
    else:
        message += "_" * (shift - (length % shift))
        
    # these conditionals check if the length of the message is a multiple of the shift
    # conditionals also check for errors (i.e. shift <= 0, etc.)
    # the 'else' statement add the number of underscores needed to be added to the message for it to be a mulitple of the shift value
    
    length = len(message)
    encrypted_message = ""
   
    for i in range(length):
        index = (i // shift) + (length // shift) * (i % shift)
        # got the formula from the given info
        encrypted_message += message[index]
         
    return encrypted_message    

def scytale_decipher(message, shift):
    '''Scytale De-cipher.
    15 points.

    Decrypts a message that was originally encrypted with the `scytale_cipher` function above.

    Example:
    scytale_decipher("IMNNA_FTAOIGROE", 3) -> "INFORMATION_AGE"
    scytale_decipher("AOTSRIOALRH_EMRNGIMA_PTT", 8) -> "ALGORITHMS_ARE_IMPORTANT"
    scytale_decipher("IRIANMOGFANEOT__", 4) -> "INFORMATION_AGE_"

    There is no further brief for this number.

    Parameters
    ----------
    message: str
        a string of uppercase English letters and underscores (underscores represent spaces)
    shift: int
        a positive int that does not exceed the length of message

    Returns
    -------
    str
        the decoded message
    '''
    # Replace `pass` with your code.
    # Stay within the function. Only use the parameters as input. The function should return your answer.
    decrypted_message = ""
    length = len(message)
    shift = length // shift
    
    for i in range(length):
        index = (i // shift) + (length // shift) * (i % shift)
        decrypted_message += message[index]
    
    return decrypted_message

    # changed the formula of the index, it rotates the orientation of the scytale_cipher
    # when the code reads downwards, it will read the original message due to the new orientation
    # replaced shift = length // shift, reverses the input and outputs of cipher in #5
    