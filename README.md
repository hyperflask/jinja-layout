# Jinja Layout

![GitHub Actions Workflow Status](https://img.shields.io/github/actions/workflow/status/hyperflask/sqlorm/python.yml?branch=main)

Easier layouts for Jinja templates.

## Installation

    pip install jinja-layout

## Usage

The `jinja_layout.LayoutExtension` needs to be added to your environment:

    from jinja2 import Environment, PackageLoader

    env = Environment(loader=PackageLoader(__name__, 'templates'))
    env.add_extension('jinja_layout.LayoutExtension')

Jinja-layout introduces the `use_layout` directive. There are two
optional arguments:

 - a template name to extend from (default: "layout.html")
 - the name of the default block to override (default: "content")

You can change the default layout template using the `defaut_layout`
attribute on your environment and the default block name using
the `default_layout_block` attribute.

This directive is similar to Jinja's `extends` directive but does
not require the use of blocks. The content which is not used in
blocks, will be automatically wrapped in a block. The name of this
block is defined by the second argument of the directive.

## Example

Let's consider the following layout saved as *layout.html*:

    <html>
      <head>{% block head %}{% endblock %}</head>
      <body>{% block content %}{% endblock %}</body>
    </html>

Basic layout example:

    {% use_layout %}
    hello world

Overriding the header block:

    {% use_layout %}
    {% block head %}<title>example</title>{% endblock %}
    hello world

Using blocks all the way:

    {% use_layout %}
    {% block head %}<title>example</title>{% endblock %}
    {% block content %}hello world{% endblock %}