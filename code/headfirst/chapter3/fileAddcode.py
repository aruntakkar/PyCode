import os

if os.path.exists('sketch.txt'):
    data = open('sketch.txt')

    for each_line in data:
        # if colon (:) is there in each_line than perform the operation.

        if not each_line.find(':') == -1:
            # split the string in two parts according to (:)
            (role, line_spoken) = each_line.split(':', 1)
            print(role, end='')
            print(' said ', end='')
            print(line_spoken, end='')

    data.close()
else:
    print("The data file is missing")
