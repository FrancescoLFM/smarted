import sys
from sfile import smartedFile
from exceptions import InvalidArgumentsError, CommandError

def main(argv, argc):
    op_file = None
    inserted = ''
    c = None
    is_listening = True

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

    while is_listening:
        try:
            command = input(f"{op_file.filename} >> ")
            if 'p' in command:
                if command == 'p':
                    op_file.print(False)
                elif command == "pn":
                    op_file.print(True)
                else:
                    raise CommandError
            elif command == 'i':
                try:
                    insert_mode = True
                    print('[INSERT MODE] Enter+CTRL-C to exit: ', end='')
                    while insert_mode:
                        inserted += input() + '\n'
                except KeyboardInterrupt:
                    insert_mode = False
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
            else:
                raise CommandError
        except CommandError as cerr:
            print(cerr, file=sys.stderr)
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
