import hashlib
import sys


def heading(title):
    # ANSI codes make headings cyan in terminals like the one in VS Code.
    if sys.stdout.isatty():
        print("\n\033[36m" + title + "\033[0m")
    else:
        print("\n" + title)


def generate_hash():
    heading("SHA-256 Hash")
    print("Hashing makes a fingerprint of data. It does not encrypt it.")
    print("A hash cannot be decrypted to recover the original input.")
    choice = input("Hash text (1) or a file (2)? ").strip()

    if choice == "1":
        message = input("Enter text: ")
        data = message.encode("utf-8")
    elif choice == "2":
        path = input("Enter the file path (without quotes): ").strip()
        try:
            # Binary mode lets us hash any kind of file, not just text.
            with open(path, "rb") as file:
                data = file.read()
        except (OSError, ValueError):
            print("Could not read that file. Check the path and permissions.")
            return
    else:
        print("Please choose 1 or 2.")
        return

    result = hashlib.sha256(data).hexdigest()
    print("SHA-256:", result)


def caesar_cipher(message, shift):
    result = ""
    for character in message:
        # The remainder wraps letters around when we go past Z or z.
        if "A" <= character <= "Z":
            position = ord(character) - ord("A")
            result += chr((position + shift) % 26 + ord("A"))
        elif "a" <= character <= "z":
            position = ord(character) - ord("a")
            result += chr((position + shift) % 26 + ord("a"))
        else:
            result += character
    return result


def cipher_menu(decrypt):
    if decrypt:
        heading("Decrypt Text (Caesar Cipher)")
    else:
        heading("Encrypt Text (Caesar Cipher)")
    print("Encryption is reversible: the shift lets us change the letters back.")
    print("This cipher is for practice and is not secure for real use.")
    message = input("Enter a message: ")
    try:
        shift = int(input("Enter a whole-number shift (use the same shift to decrypt): "))
    except ValueError:
        print("The shift must be a whole number.")
        return

    if decrypt:
        shift = -shift
    print("Result:", caesar_cipher(message, shift))


def digital_signature_demo():
    heading("Digital Signature Demonstration")
    # RSA is complicated, so a tested library handles the math for us.
    try:
        from cryptography.exceptions import InvalidSignature
        from cryptography.hazmat.primitives import hashes
        from cryptography.hazmat.primitives.asymmetric import padding, rsa
    except ImportError:
        print("Install the required library with: python -m pip install cryptography")
        return

    print("A signature checks that a message matches what the private key signed.")
    print("It detects changes, but does not hide the message like encryption does.")
    message = input("Enter a message to sign: ")
    print("Generating temporary RSA keys...")
    private_key = rsa.generate_private_key(public_exponent=65537, key_size=2048)
    public_key = private_key.public_key()

    # PSS is the padding used with RSA signatures, along with SHA-256.
    signature_padding = padding.PSS(
        mgf=padding.MGF1(hashes.SHA256()),
        salt_length=padding.PSS.MAX_LENGTH
    )
    signature = private_key.sign(
        message.encode("utf-8"), signature_padding, hashes.SHA256()
    )
    print("Message signed with the private key.")

    try:
        public_key.verify(
            signature, message.encode("utf-8"), signature_padding, hashes.SHA256()
        )
        print("Original message: verification succeeded.")
    except InvalidSignature:
        print("Original message: verification failed.")

    # Keep the same signature but change the message to see what happens.
    changed_message = message + " (changed)"
    print("Changed message:", changed_message)
    try:
        public_key.verify(
            signature, changed_message.encode("utf-8"),
            signature_padding, hashes.SHA256()
        )
        print("Changed message: verification succeeded (unexpected).")
    except InvalidSignature:
        print("Changed message: verification failed, as expected.")
    print("These keys are only used for this demonstration and are not saved.")


def main():
    while True:
        heading("Cybersecurity Practice")
        print("1. Generate SHA-256 Hash")
        print("2. Encrypt Text (Caesar Cipher)")
        print("3. Decrypt Text (Caesar Cipher)")
        print("4. Digital Signature Demonstration")
        print("5. Exit")
        choice = input("Choose an option: ").strip()

        if choice == "1":
            generate_hash()
        elif choice == "2":
            cipher_menu(False)
        elif choice == "3":
            cipher_menu(True)
        elif choice == "4":
            digital_signature_demo()
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Please choose a number from 1 to 5.")


if __name__ == "__main__":
    main()
