## Advanced context modification for cookiecutter.

[![](https://img.shields.io/github/stars/samj1912/cookiecutter-advanced-demo?label=Star%20this%20repo&style=social)](https://github.com/samj1912/cookiecutter-advanced-demo/stargazers)

This repo is an advanced example of a cookiecutter that can modify cookiecutter's
context values from hooks. Read the [pre_gen_project.py](https://github.com/samj1912/cookiecutter-advanced-demo/blob/master/hooks/pre_gen_project.py) for examples and a demo on how to modify context.

<details>
<summary>Contents - pre_gen_hook.py</summary>
    
```python
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
```
</details>

To run this demo cookiecutter do -

    cookiecutter https://github.com/samj1912/cookiecutter-advanced-demo

This demo shows how to do the following -

1. Add values to the cookiecutter context.

The above is useful for a bunch of cases -
* Being able to add values to the context independent of the user input -
    for eg. creating a valid project slug from a project name by escaping
    the values.
* When you are sharing files between different cookiecutter
    directories and you want to define defaults in order to avoid
    Jinja from complaining the certain values are not defined.

2. Modify existing values cookiecutter context values even after user input-

This is useful when you want to handle bad user input and instead of raising an
error, set the cookiecutter context values correct. For eg modifying the project_slug
from the user to be valid.

3. Conditionally modify the above based on user input.

Note - You can also do this to change the name of the variable that is used to define the generated project directory. This is useful when handling inputs from the user that you want to escape.
