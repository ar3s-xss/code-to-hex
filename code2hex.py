import sys, getopt, os.path

array_of_symbols = []
symbols_hex = []
code =''
def if_file_exists(path_or_script_name):

    if os.path.exists(path_or_script_name):
        print(f"The file {path_or_script_name} exists.\n\n")
    else:
        print(f"The file {path_or_script_name} doesn't exist.\n\n")


     
    with open(path_or_script_name, 'r') as script:
        symbols = script.read()

        array_of_symbols = list(symbols)

    
    symbols_hex = [f'\\x{hex(ord(symbol))[2:]}' for symbol in array_of_symbols]
    code = ''.join(symbols_hex)
    
    print(code)
    print("\n")


    
if __name__ == "__main__":  

    script_name = sys.argv[1]

    if_file_exists(script_name)
    
