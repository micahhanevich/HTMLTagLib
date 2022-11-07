from typing import Iterable


class Element:
    """ Represents a generic HTML tag. Used to make dynamic page
    generation in-code easily applicable to a ``bottle`` webpage.
    Used as the base class for more advanced objects of this type.

    :param tag: Type of HTML tag.
    :param attr: Dictionary of attribute choices for the Element. (default: None)
    :param html: Overrides generated html str (default: None)
    :param end_tag: Whether to generate a terminating tag. Ex: </div> (default: True) """

    _attributes: dict

    # Initialize Class
    def __init__(self, tag: str, attr: dict = None, html: str = None, end_tag: bool = True):

        # HTML Element Type
        self.tag = tag

        # Raw HTML Text
        self._html = html

        # HTML Child Elements (accessible
        #  through indexing the object)
        self._items = []

        # List of HTML Attributes (accessible
        #  through python as attributes)
        self._attributes = attr

        # Determines if the closing tag (</tag>)
        #  is included or not
        self.end_tag = end_tag

        # If initialized as not bool, set to False
        if type(end_tag) is not bool:
            self.end_tag = False

        # If initialized blank, set to empty dict
        if attr is None:
            self._attributes = {}

        # If initialized blank, generate html based
        #  on _attributes and tag
        if html is None:
            self._gen_html()

    def _gen_html(self):
        """Loops through the object's
        attributes and children, formats them
        into html, and sets self._html equal
        to the calculated string."""

        # The character to insert for newlines
        # Unless the child is an Element, gets set to empty
        inserted_char = '\n'

        # The str version of the attributes; this var is
        #  used to store the data between loops
        attr_list = ''

        # The str version of the attributes; this var is
        #  used to store the data between loops
        children_list = ''

        # If there are no attributes, we still need a
        #  space for it to be valid HTML
        if len(self._attributes) > 0:
            attr_list += ' '

        # For every attribute entered:
        for attr_name, attr_val in self._attributes.items():

            # If neither the name or value are None (implying
            #  it is a valid attribute):
            if attr_name is not None and attr_val is not None:

                # Special case handling for the 'Class' attribute:
                #  all objects have a .class method; therefore we
                #  have to call our class attribute something
                #  slightly different to avoid errors.

                # If it is not a specialized attribute:
                if attr_name[0:4] != 'HTML':

                    if type(attr_val) == type(''):
                        # Add the attribute normally. 'attribute=value'
                        attr_list += f'{attr_name}=\"{attr_val}\"'
                    else:
                        # Add the attribute normally. 'attribute=value'
                        attr_list += f'{attr_name}={attr_val}'

                else:

                    if type(attr_val) == type(''):
                        # Add the specialized attribute.
                        attr_list += f'{attr_name[4:]}=\"{attr_val}\"'
                    else:
                        # Add the specialized attribute.
                        attr_list += f'{attr_name[4:]}={attr_val}'

            # If the attribute has a name but no value, it means
            #  we want a special type of attribute. If this type
            #  is used, it's name is entered with no '='.
            #  For ex. <button disabled> created by Element('button', {'disabled': None})

            # else if the attribute has a value of None:
            elif attr_val is None:

                # Add only the attribute name.
                attr_list += f'{attr_name}'

            # If we're not on the last attribute:
            if attr_name != list(self._attributes.keys())[-1]:
                # Add a space between this attribute and the next.
                attr_list += ' '

        # For every child object:
        try:
            for child in self._items:

                # If the child is an Element object:
                if issubclass(type(child), Element):

                    # Update it and it's childrens' HTML.
                    child.reload()

                # Else if the child is a String or None object:
                elif type(child) is str or child is None:

                    # Set the inserted char to empty.
                    inserted_char = ''

                # Update the children_list
                child = str(child).strip('\n')
                children_list += f'{child}\n'

        except TypeError:
            pass

        # If the end tag (</Element>) is set to False:
        if self.end_tag is not True:

            # Save the updated HTML to the object, without the end tag.
            self._html = f"""<{self.tag}{attr_list}>{inserted_char}{children_list}"""

        # If the Element is not a comment:
        elif self.tag != '!--':

            # Save the updated HTML to the object.
            self._html = f"""<{self.tag}{attr_list}>{inserted_char}{children_list}</{self.tag}>"""

        # If the Element is a comment:
        else:

            # Save the updated HTML Comment to the object.
            self._html = f"""<{self.tag}{inserted_char}{children_list}-->"""

    def reload(self):
        """Updates the object's HTML.
        Usable as an easy-to-overwrite
        public call to _gen_html"""

        self._gen_html()

    def __getitem__(self, key):
        """Magic Method override; returns
        the appropriate value when
        indexing into the object"""

        try:
            return self._items[key]

        except IndexError as e:
            print('Key: ' + str(key))
            raise e

    def __setitem__(self, key, value):
        """Magic Method override; sets
        the appropriate value when
        indexing into the object;
        updates HTML"""

        self._items[key] = value
        self._gen_html()

    def __getattr__(self, item):
        super().__getattribute__(item)

    def set_items(self, value: list):
        """Sets the self._items array to a
        value; updates HTML"""

        self._items = value
        self._gen_html()
        return self

    def add_item(self, item: any):
        """Appends an item onto self.items;
        updates HTML"""

        self._items.append(item)
        self._gen_html()
        return self

    def add_items(self, value: Iterable):
        """Appends a list of values onto
        self.items; updates HTML"""

        for item in value:
            self._items.append(item)
        self._gen_html()
        return self

    # https://stackoverflow.com/questions/4984647/accessing-dict-keys-like-an-attribute
    #  plus some personal additions to allow normal attr access as well
    # def __getattr__(self, name):
    #     """Magic Method override; Returns
    #     items in self._attributes as if they
    #     were actual attributes / properties"""
    #
    #     try:
    #
    #         return self._attributes
    #
    #     except KeyError:
    #
    #         try:
    #
    #             return super().__getattribute__(self, name)
    #
    #         except KeyError:
    #
    #             msg = "'{0}' object has no attribute '{1}'"
    #             raise AttributeError(msg.format(type(self).__name__, name))

    def __str__(self):
        """Magic Method override; Defines
        how to return object as string"""
        return self._html

    def __len__(self):
        """Magic Method override; defines
        how to return object length"""
        return len(self._items)
