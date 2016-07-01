import yate
import athletemodel

athletes = athletemodel.get_namesID_from_store()

print(yate.start_response())

print(yate.include_header("NUAC's List of Athletes"))

print(yate.start_form("generate_timing_data.py"))

print(yate.para_text("Select an athlete from the list to work with:"))

for each_athlete in athletes:
    # Now athletes are list of lists
    # so amending the code to get the data.
    print(yate.radio_button_id("which_athlete",
                               each_athlete[0], each_athlete[1]))

print(yate.end_form("Select"))

print(yate.include_footer({"Home": "/index.html"}))
