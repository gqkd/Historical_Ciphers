# Enigma Machine Encryption in Python

This Python code implements the encryption and decryption of messages using the Enigma machine. The Enigma machine was a cipher machine used by Germany during World War II. It was a very complex machine, but this code implements a simplified version of it.

The code uses the following modules:

* `string`: This module provides the `ascii_lowercase` constant, which is a list of all lowercase letters.
* `json`: This module is used to read the configuration of the Enigma machine from a JSON file.

The code also defines the following functions:

* `rotate()`: This function rotates the rotors of the Enigma machine.
* `shift()`: This function encrypts or decrypts a letter using the Enigma machine.
* `encrypt()`: This function encrypts a message using the Enigma machine.
* `decrypt()`: This function decrypts a message using the Enigma machine.

To use the code, you first need to create a configuration object. This object specifies the configuration of the Enigma machine, such as the order of the rotors and the reflector. You can create a configuration object by reading the configuration from a JSON file.

Once you have created a configuration object, you can use the `encrypt()` or `decrypt()` functions to encrypt or decrypt a message.

The following is an example of how to use the code:


```python
import enigma

# Create a configuration object.
with open("enigma.json") as f:
  config = json.load(f)

# Encrypt a message.
message = "hello world"
ciphertext = enigma.encrypt(message, config)

# Decrypt the message.
plaintext = enigma.decrypt(ciphertext, config)

print(plaintext)
```


This code will encrypt the message "hello world" and print the ciphertext. You can then decrypt the ciphertext using the `decrypt()` function.

The code is well-commented and easy to understand. It is also modular, so you can easily modify it to add new features or change the configuration of the Enigma machine.

