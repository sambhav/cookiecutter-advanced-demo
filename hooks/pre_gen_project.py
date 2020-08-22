"""
You can update the cookiecutter context though Jinja.
In order to do so - you can use Jinja inside the pre gen hook
to update the cookiecutter context.

I use the docstring of the pre gen hook since it is an easy way to update things
without causing any syntax errors.

Example -

1. You can add values to the context -

{{ cookiecutter.update({"updated_value": cookiecutter.value * 2 }) }}

The above is useful for a bunch of cases -
* Being able to add values to the context independent of the user input -
    for eg. creating a valid project slug from a project name by escaping
    the values.
* When you are sharing files between different cookiecutter
    directories and you want to define defaults in order to avoid
    Jinja from complaining the certain values are not defined.

2. You can also modify existing values -

{{ cookiecutter.update({"modify_value": "modified_value" }) }}

3. It is also possible to use Jinja tags to modify values conditionally.
You can also do this to change the name of the generated project directory.
See the example below. This is useful when handling inputs from the user
that you want to escape.

Eg -

{% if cookiecutter.project_name != "advanced_test" %}
{{ cookiecutter.update({ "project_name_modified": True }) }}
{% else %}
{{ cookiecutter.update({ "project_name_modified": False }) }}
{% endif %}
"""
