try:
    data = open('sketch.txt')

    for each_line in data:
        # code in try block is protected from run-time errors

        """
            with this type of data is best to ignore lines that
            don't confirm to expected format.
            if call to split() method causes an exception.
            let simply pass it on reporting it as an error.
        """

        try:
            # split the string in two parts according to (:)
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')
        except ValueError:
            print("String other than required format string for split format")
            pass

    data.close()
except IOError:
    print('The data file is missing')
