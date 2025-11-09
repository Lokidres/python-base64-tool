import base64
import argparse

def get_input():
    parser = argparse.ArgumentParser()
    parser.add_argument("-e","--encode",help="base64 content for encoding")
    parser.add_argument("-d","--decode",help="base64 content for decoding")
    parser.add_argument("-ef","--encodefile",help="base64 file path for encoding")
    parser.add_argument("-df","--decodefile",help="base64 file path for decoding")
    args = parser.parse_args()
    return args

inputs = get_input()

def main():
    if inputs.encode:
        bytec = inputs.encode.encode('utf-8')
        output = base64.b64encode(bytec)
        print(f"input: {inputs.encode}, output: {output.decode()}")

    elif inputs.decode:
        decoded_bytec = base64.b64decode(inputs.decode)
        decoded_strc = decoded_bytec.decode('utf-8')
        print(f"input: {inputs.decode}, output: {decoded_strc}")
        
    elif inputs.encodefile:
        with open(inputs.encodefile, "rb") as f:  # Binary okuma
            content = f.read()
        
        encoded_content = base64.b64encode(content)
        
        with open(inputs.encodefile, "wb") as f:  # Binary yazma
            f.write(encoded_content)
        
        print(f"new content is: {encoded_content.decode('utf-8')}")
        
    elif inputs.decodefile:
        with open(inputs.decodefile, "r") as f:  # as f eklendi!
            content = f.read()
        
        byte_content = base64.b64decode(content)
        str_content = byte_content.decode('utf-8')
        
        with open(inputs.decodefile, "w") as f:
            f.write(str_content)
        
        print(f"new content is: {str_content}")

main()





