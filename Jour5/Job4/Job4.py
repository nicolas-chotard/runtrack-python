def caesar(message, shift):

  alphabet = "abcdefghijklmnopqrstuvwxyz"

  encrypted_message = ""

  for char in message:
    if char.lower() in alphabet:

      char_index = alphabet.index(char.lower())


      shift_index = (char_index + shift) % 26


      if char.isupper():
        encrypted_message += alphabet[shift_index].upper()
      else:
        encrypted_message += alphabet[shift_index]
    else:

      encrypted_message += char


  return encrypted_message

print(caesar("Bonjour!", 3))

