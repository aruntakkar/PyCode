# Default Values for the arguments is needed in some case


# if you forget to set the value explictly then something is there for default
def get_gender(sex="Unknown"):
    if sex is "m":
        sex = "Male"
    elif sex is "f":
        sex = "Female"
    print(sex)

get_gender("m")
get_gender("f")
get_gender()
