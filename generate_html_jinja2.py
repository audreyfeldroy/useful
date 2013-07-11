from jinja2 import FileSystemLoader
from jinja2.environment import Environment


def generate_html():
    """ Takes an HTML template with Jinja2 blocks/filters as input.
        Writes out an HTML template. """

    env = Environment()
    env.loader = FileSystemLoader('templates/')

    tmpl = env.get_template('input.html')
    rendered_html = tmpl.render()

    with open('templates/output.html','w') as fh:
        fh.write(rendered_html)


if __name__ == '__main__':
    generate_html()
