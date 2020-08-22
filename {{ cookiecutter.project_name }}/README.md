Values is : {{ cookiecutter.value }}
Updated value is : {{ cookiecutter.updated_value }}

Cookiecutter context looks like -

```json
{{ cookiecutter | jsonify }}
```

{% if cookiecutter.project_name_modified %}
You modified the project name to something other than "advanced_test".
{% endif %}
