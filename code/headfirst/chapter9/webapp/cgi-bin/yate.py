from string import Template
# Importing the Template class from the standard
# module string, This allow for simple string-subsititution templates


def start_response(resp="text/html"):
    return('Content-type:' + resp + '\n\n')

# This function takes a single(optional) string argument and uses it to create
# CGI "Content-type:" line with "text/html" as the default


def include_header(the_title):
    with open('templates/header.html') as headf:
        head_text = headf.read()
    header = Template(head_text)
    return(header.substitute(title=the_title))
"""
    Open the template file(which is HTML), read it in,
    and substitute in the provided title.

    This function takes a single argument and uses at the
    title for the start of the HTML page. The page
    itself is stored in within a seprate file in
    "templates/header.html", and the title is
    substituted in as needed.
"""


def include_footer(the_links):
    with open('templates/footer.html') as footf:
        foot_text = footf.read()

    # Turning the dictionary of links into a string.
    link_string = ''
    for key in the_links:
        link_string += '<a href=' + \
            the_links[key] + '>' + key + '</a>&nbsp;&nbsp;&nbsp;&nbsp;'

    footer = Template(foot_text)
    return(footer.substitute(links=link_string))

"""
    This function takes a argument the_links(links as a
    dictionary), footer file is open and read

    a empty string link_string is created.
    with the help of key in the_links dictionary adding
    the <a> tags in the link_string.

    and the links are substitued as needed.
"""


"""
    This function returns the HTML for the start of a
    form and lets the caller specify the URL to send the
    form's data to, as well method to use

    * POST/GET
"""


def start_form(the_url, form_type="POST"):
    return('<form action="' + the_url + '" method="' + form_type + '">')


"""
    This function help in genrating the HTML for the
    form terminaton code, allowing the caller to
    customize the text of the form's submit button.
"""


def end_form(submit_msg="submit"):
    return('<p></p><input type=submit  value="' + submit_msg + '"></form>')


"""
    This function helps in creating the radio buttons

    Takes two arguments name, value for the input of the
    radio button

    radio button value after in the input and <br> tag
    after it.

    Note both arguments are required because none of the
    value is default
"""


def radio_button(rb_name, rb_value):
    return('<input type="radio" name="' + rb_name + '" value="' + rb_value + '"> ' +
           rb_value + '<br/>')


"""
    This function takes a argument(a list of item)
    A string which contain <ul>
    After each iteration item is added to the li, li
    added in the u_string
    after the iteration </ul> is ended.
"""


def u_list(items):
    u_string = '<ul>'
    for item in items:
        u_string += '<li>' + item + '</li>'
    u_string += '</ul>'
    return(u_string)

"""
    This function takes two arguments header_text,
    header_level with the default value 2

    for specifying the h1, h2, so on tag accroding to value of
    the header_level

    header_text is for provding the header_text which is required.
"""


def header(header_text, header_level=2):
    return('<h' + str(header_level) + '>' + header_text + '</h' + str(header_level) + '>')


"""
     Function simply return paragraph tag with the
      text.
"""


def para_text(para_text):
    return('<p>' + para_text + '</p>')


def create_inputs(inputs_list):
    html_inputs = ""
    for each_input in inputs_list:
        html_inputs = html_inputs + '<input type="Text" name="' + each_input + '" size=40>'
    return (html_inputs)


def do_form(name, the_inputs, method="POST", text="Submit"):
    # Grabing the Template from the disk
    with open('templates/form.html') as formf:
        form_text = formf.read()
    # Create the list of <input> tags
    inputs = create_inputs(the_inputs)
    # Create a Template Form
    form = Template(form_text)
    # Substituting the arguments and generated <INPUT> tags into the template
    # to create the form.
    return(form.substitute(cgi_name=name,
                           http_method=method,
                           list_of_inputs=inputs,
                           submit_text=text))
