import sys, os, subprocess
from sfile import smartedFile
from exceptions import *
from var import *
import json

def main(argv, argc):
    # Arg check
    try:
        if argc < 1:
            raise InvalidArgumentsError(f"Expected at least 1 argument, found {argc}")

        for arg in argv:
            if "-" not in arg:
                with open(arg, 'a+'):
                    op_file = smartedFile(arg)
                    break
            else:
                pass

    except InvalidArgumentsError as argerr:
        print(argerr, file=sys.stderr)
        with open("a.txt", 'a+'):
            op_file = smartedFile("a.txt")

    # Langpath init
    with open(lang_file, 'r') as langf:
        lang_list = json.load(langf)
    

    print("Welcome to smarted v1.0! Press h for help")
    is_listening = True
    inserted = ''
    cl = 1

    while is_listening:
        try:
            command = input(f"{op_file.filename} ({cl})>> ")
            if 'p' in command:
                if command == 'p':
                    op_file.fprint(False)
                elif command == "pn":
                    op_file.fprint(True)
                elif command == "pi":
                    if inserted != '':
                        print(inserted)
                else:
                    raise CommandError
            
            elif 'l' in command:
                newl = command.split('l')
                nl = int(newl[1])
                if not op_file.check_nline(nl):
                    cl = nl
                else:
                    raise InvalidLine(f"Invalid selected line ({nl})")

            elif command == 'i':
                try:
                    insert_mode = True
                    print('[INSERT MODE] Enter+CTRL-C to exit: ', end='')
                    while insert_mode:
                        inserted += input() + '\n'
                except KeyboardInterrupt:
                    print()
                    insert_mode = False
            elif command == 'r':
                extension_l = op_file.filename.split('.')
                extension = extension_l[len(extension_l)-1]
                if extension in lang_list:
                    language_name = lang_list[extension]
                    with open(f"{lang_dir}/{language_name}.json", 'r') as lf:
                        language = json.load(lf)
                    if language["isCompiled"]:
                        pass
                    if language["isInterpreted"]:
                        if os.name == "posix":
                            subprocess.run([language['interpreter_path']['linux'], op_file.filename])
                        elif os.name == "nt":
                            subprocess.run(language['interpreter_path']['windows'])
                else:
                    raise LanguageNotSupported(extension)
            elif command == 'q':
                if inserted == '':
                    break
                else:
                    while True:
                        c = input('Unsaved work detected, are you sure to exit(y/n) ').lower()
                        if c == 'y':
                            is_listening = False
                        break
            elif command == 'w':
                op_file.write(inserted, False)
                inserted = ''
            elif command == 'h':
                print(help_txt)
            else:
                raise CommandError
        except LanguageNotSupported as langerr:
            print(langerr, file=sys.stderr)
        except CommandError as cerr:
            print(cerr, file=sys.stderr)
        except InvalidLine as lerr:
            print(lerr, file=sys.stderr)
        except KeyboardInterrupt:
            print("Keyboard Interrupt")
        except FileNotFoundError as ferr:
            print(f"{ferr}, exiting from the program", file=sys.stderr)
            sys.exit(-1)
            
if __name__ == "__main__":
    argv = sys.argv
    argv.pop(0) # delete the first argument
    argc = len(argv)
    main(argv, argc)
