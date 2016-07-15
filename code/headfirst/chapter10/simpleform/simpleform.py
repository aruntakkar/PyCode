import wsgiref.handlers

from google.appengine.ext import webapp
from google.appengine.ext import db
from google.appengine.ext.webapp import template
from google.appengine.ext.db import djangoforms
import birthDB


class BirthDetailsForm(djangoforms.ModelForm):

    class Meta:
        model = birthDB.BirthDetails


# This class responds to a web request from your web browser.
class SimpleInput(webapp.RequestHandler):

    def get(self):
        html = template.render("templates/header.html",
                               {"title": "Provide your birth details"})

        html = html + template.render("templates/form_start.html", {})

        # Using your new class to generate your form
        # By adding the argument names are generated according to model
        # properties.
        html = html + str(BirthDetailsForm(auto_id=False))

        html = html + template.render("templates/form_end.html",
                                      {"sub_title": "Submit Details"})

        html = html + \
            template.render("templates/footer.html", {"links": ""})
        self.response.out.write(html)

    def post(self):
        # Create a new "BirthDetails" object
        # to hold your data.
        new_birth = birthDB.BirthDetails()

        # Get each of the form's data values
        # and assign them to your new object's
        # attributes
        new_birth.name = self.request.get('name')
        new_birth.date = self.request.get('date')
        new_birth.time = self.request.get('time_of_birth')

        # Put your data to the GAE datastore
        new_birth.put()

        html = template.render('templates/header.html',
                               {'title': 'Thank you!'})

        html = html + "<p>Thank you for providing your birth details.</p>"

        html = html + template.render('templates/footer.html',
                                      {'links': 'Enter <a href="/">another birth</a>.'})

        self.response.out.write(html)


def main():
    # create a new "webapp" object for your application.
    app = webapp.WSGIApplication([('/.*', SimpleInput)], debug=True)
    # Process the HTTP request. The default implementation creates a handler
    # instance using a wsgiref.handlers class to implement the actual WSGI
    # application interface.
    wsgiref.handlers.CGIHandler().run(app)

if __name__ == '__main__':
    main()
