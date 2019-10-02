
from settings import *


def ecriture():
    import sys, re
    if len(sys.argv) != 2:
        print("usage: render.py <file>.template ")
        sys.exit(0)

    filename = sys.argv[1]
    try:
        if re.match("\w+.template", filename):
            with open(filename, 'r') as f:
                contenu = f.read()
                a_ecrire = contenu.format_map(globals())
                file_html = filename.replace('.template', '.html')
            with open(file_html, 'w') as f_h:
                f_h.write(a_ecrire)
        else:
            print("le fichier {} n'a pas .template comme extension.".format(filename))
            sys.exit(0)
    except FileNotFoundError as e:
        print("le fichier {} n'existe pas.".format(e.filename))
        sys.exit(0)
    except PermissionError as e:
        print("Droits de lecture absent sur le fichier{}".format(e.filename))
        sys.exit(0)
    except Exception as e:
        print("Une erreur a empeché l'ouverture du fichier.".format(e))
        sys.exit(0)

if __name__ == '__main__':
    ecriture()