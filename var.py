op_file = None
c = None
help_txt = '''--HELP--

p               print
pl              print current line (see l for changing the current line)
pn              print with line numbers
pi              print only inserted text
pl <num>        print line <num> without changing the current line
pln             pl + pn
p -p            print permissions

i               insert mode
iw              save after quitting insert mode
esc             exit insert mode

w               save
x               save and exit
b               generate backup file
q               quit

s               substitute word (ed syntax)
m               add word before ... (ed syntax)
a               append at the end of the current line
l <num>         set current line to <num>

!               run bash command

n               add a new line before the current line
d               remove the current line'''