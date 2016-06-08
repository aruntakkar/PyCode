import pickle
import nesterstdout

new_man = []

try:
    with open('man_data.txt', 'rb') as man_file:
        new_man = pickle.load(man_file)
except IOError as err:
    print('File error ' + str(err))
except pickle.PickleError as perr:
    print('Pickling error ' + str(perr))

nesterstdout.print_lol(new_man)
