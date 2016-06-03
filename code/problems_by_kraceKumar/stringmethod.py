"""
    Write a program to display the poem The Road Not Taken by Robert Frost.

    count the number of times word "I" is come in Poem.

    # Replace "could not" with "couldn't"
"""
# -*- coding: utf-8 -*-


def main():
    poem = """
    Two roads diverged in a yellow wood,
    And sorry I could not travel both
    And be one traveler, long I stood
    And looked down one as far as I could
    To where it bent in the undergrowth;
    Then took the other, as just as fair,
    And having perhaps the better claim,
    Because it was grassy and wanted wear;
    Though as for that the passing there
    Had worn them really about the same,
    And both that morning equally lay
    In leaves no step had trodden black.
    Oh, I kept the first for another day!
    Yet knowing how way leads on to way,
    I doubted if I should ever come back.
    I shall be telling this with a sigh
    Somewhere ages and ages hence:
    Two roads diverged in a wood, and I
    I took the one less traveled by,
    And that has made all the difference.
    """

    # finding the occurence of I in poem using for loops

    # poem = poem.lower().split()
    # count = 0
    # for each_word in poem:
    #     for character in each_word:
    #         if character == "i":
    #             count += 1
    # print(count)

    # Printing the Poem and Poem author name using format

    poem = "{}\n -- {}".format(poem, "Robert")

    # find the occurence of I in poem

    print("Occurence of I: {}".format(poem.count("I")))

    # Replace the word "could not" with "couldn't"
    print(poem.replace("could not", "couldn't"))

# __name__ holds the name of the current module
if __name__ == "__main__":
    main()  # call main function
