try:
    data = open('missing.txt')
    print(data.readline(), end='')
    """
        if we need to know about the error
        When an exception is raised, python interpreter
        raises an exception object into the suite,
        we can make this exception suite available to
        your code
    """
    # exception object name is given by you.
except IOError as err:
    print("File Error" + str(err))
finally:
    """
        if there is any I/O error to file data file
        object could not be created so NameError is
        occured
        To Fix this use locals() BiF which returns a
        collection of names defined in the current scope.
    """
    if 'data' in locals():
        data.close()
