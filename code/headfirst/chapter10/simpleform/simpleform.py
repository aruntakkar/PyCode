from google.appengine.ext.webapp import templates
from google.appengine.ext.db import djangoforms
import birthDB


class BirthDetailsForm(djangoforms.ModelForm):

    class Meta:
        model = birthDB.BirthDetailsForm

    html = template.render("templates/header.html",
                           {"title": "Report a Possible Sightings"})

    html = html + template.render("templates/form_start.html", {})

    # Using your new class to generate your form
    # By adding the argument names are generated according to model properties.
    html = html + str(BirthDetailsForm(auto_id=False))

    html = html + template.render("templates/form_end.html",
                                  {"sub_title": "Submit Sightings"})

    html = html + template.render("templates/footer.html", {"links": ""})
