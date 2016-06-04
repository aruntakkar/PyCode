"""
    There are two types of error mainly:
        Syntax error:-  also known as parsing errors, the parser
        repeates the offending line and and displays a little 'arrow'
        pointing at the earliest point in the line where error is detected.
        the error is caused by(or at least detected at) the token preceding the
        arrow.

        Exceptions:- Even if a statement or expression is syntactically Correct
        it may cause an error when attempt is made to exectue it,
        (Errors Detected during Execution are called exceptions and are not
        unconditionally Fatal)

        To Handle Exceptions we can use try & except(put your suspicious code
        in try: block, After the try block include an execept: statement,
        followed by block of code which can handle the problem as elegently as
        possible)
"""

while True:
    try:
        number = int(input("Enter your Favourite Number?"))
        print(18 / number)
        break
    except ValueError:
        print("Make sure you enter a number")
    except ZeroDivisionError:
        print("Don't Pick Zero")
    except:
        break
    finally:
        print("loop is completed")
