import pytest
from jinja2 import Environment, FileSystemLoader
from jinja_layout import LayoutExtension
import os


templates_path = os.path.join(os.path.dirname(__file__), "templates")


@pytest.fixture()
def env():
    env = Environment(loader=FileSystemLoader(templates_path))
    env.add_extension(LayoutExtension)
    env.default_layout = "base.html"
    return env


def test_blocks(env):
    html = env.get_template("blocks.html").render()
    assert "title=foobar" in html
    assert "content=hello world" in html


def test_mixed(env):
    html = env.get_template("mixed.html").render()
    assert "title=foobar" in html
    assert "content=\n\nhello world" in html


def test_noblock(env):
    html = env.get_template("noblock.html").render()
    assert "data=\nhello world" in html
