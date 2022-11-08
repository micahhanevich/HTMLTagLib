from _io import TextIOWrapper
import typing
from .. import *


def import_html(f: [TextIOWrapper, str]) -> Element:
    """
    Import a raw page / file of HTML and return a collection of HTMLTagLib Elements
    :param f: Can be a `TextIOWrapper` passed from the builtin `open` function; a str with the filepath of the file; or a str containing an html page.
    :return: Element
    """

    if type(f) == TextIOWrapper:
        print('Wrapper!')
    else:
        print('Not that!')

    return HTML()


import_html(open('text.txt'))
import_html('text.txt')
