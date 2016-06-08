import nesterstdout

man = []
other = []

try:
    data = open('sketch.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            # strip is used to strip the whitespaces in line_spoken
            line_spoken == line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    data.close()
except IOError:
    print('The datafile is missing')

try:
    with open('man_data.txt', 'w') as man_file:
        nesterstdout.print_lol(man, fh=man_file)
    with open('other_data.txt', 'w') as other_file:
        nesterstdout.print_lol(other, fh=other_file)
    # if there an I/O error occur to writing data at this place,
    # data may be corrupted.so we need a way regardless of whether an IOError
    # has occured
    # Make sure files are closed.
except IOError as err:
    print("File Error " + str(err))

"""
    when we have a situation where we need code that
    need to run no matter what error occur,
    add that code to your try statement's finally suite.
"""

"""
    if no runtime error occur, any code in the finally
    suite executes, Equally if an IOerror occurs, the
    except suites not executes but the finally suits
    executes.
"""

# finally:
#     men_file.close()
#     other_file.close()
