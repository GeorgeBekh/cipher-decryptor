import sys
import caesar_decryptor


def main(args):
    """The main routine."""
    print("Text to decrypt: " + args[1])
    a = caesar_decryptor.CaesarDecryptor();
    print(a.letterFrequency)
    

if __name__ == "__main__":
    main(sys.argv)