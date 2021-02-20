import string


string_1 = "Sld wl blf hloev zmb vjfzgrlm?"
string_2 = "Zhygvcyl obgu fvqrf ol mreb."

def dec_atbash(str_in: str)->str:
    """
    Applies the atbash cipher to str_in. Applying an atbash cipher is equivalent to 
    reversing the atbash cipher. It applies a different cipher to uppercase and lowercase values

    Args:
        str_in: input string

    Returns:
        string with every character applied to atbash cipher.

    """
    new_str = []
    for char in str_in:
        new_char = None
        if char not in string.punctuation and char != ' ': # 
            char_ascii = ord(char)
            if char_ascii > ord('Z'):  
                new_char = chr(ord('z') - (char_ascii - ord('a')))
            else:
                new_char = chr(ord('Z') - (char_ascii - ord('A')))
        else:
            new_char = char

        new_str.append(new_char)

    
    return ''.join(new_str)

def ceasar_rot(str_in:str, rot: int)->str:
    """
    Performs a ceasaraian rotation, adding rot to every char's ascii then taking (x - 68) (mod 26) + 68. It applies the same rotation constant for uppercase and lowercase results. Does not rotate punctuation. 

    Args:
        str_in: input string to be rotated
        rot: integer to rotate by

    Returns:
        rotated string

    Raises:
        ValueError: it sees a nonalpha, nonpunctuation character. 

    """
    new_str = []
    for char in str_in:
        new_char = None
        if char not in string.punctuation and char != ' ':
            char_ascii = ord(char)
            if char_ascii > ord('Z'):  
                new_char = chr(((char_ascii + rot) - ord('a'))%26 + ord('a'))
            else:
                new_char = chr(((char_ascii + rot) - ord('A'))%26 + ord('A'))
        else:
            new_char = char

        new_str.append(new_char)


    return ''.join(new_str)

def _find_ceasar_rot(str_in: str)->None:
    """
    Rotates the string all 26 ways for me to determine the appropriate rotation. 

    Args:
        str_in: the sample string to rotate
    
    """

    for rot in range(26):
        str_res = ceasar_rot(str_in, rot)
        print(f"Rotation {rot}: {str_res}")




if __name__ == "__main__":
    _find_ceasar_rot(string_1)
    print("-" * 60)
    _find_ceasar_rot(string_2)
    print("-" * 60)
    print(dec_atbash(string_1))
    print("-" * 60)
    print(dec_atbash(string_2))
