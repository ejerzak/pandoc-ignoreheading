#!/usr/bin/env python

import pandocfilters as pf

def has_ignore_tag(value):
    """
    Recursively checks a value to see whether it contains an ignoreheading tag
    somewhere inside it.
    """
    if isinstance(value, dict):
        # the case we're actually looking for:
        # a tag buried inside a Span element
        if (value.has_key('t') and # avoid barfing on citation elements
            value['t'] == 'Span' and
            value['c'][0][1] == ['tag'] and
            # TODO: not sure what else Pandoc might stuff in here that could
            # mess up the list indexing. I have at least tested that this works
            # on headlines with multiple tags.
            value['c'][0][2][0][1] == 'ignoreheading'):
            return True
        # for other non-leaf dictionaries, recurse:
        elif value.has_key('c'):
            return has_ignore_tag(value['c'])
        # we're at the bottom of the tree:
        return False

    elif isinstance(value, list):
        for elt in value:
            if has_ignore_tag(elt):
                return True
            
    return False

def ignore_heading(key, value, format, meta):
    "Filter that removes headers tagged with ignoreheading tag"
    if key == 'Header' and has_ignore_tag(value):
        return [] # this tells pandocfilters to delete the element

if __name__ == '__main__':
    pf.toJSONFilter(ignore_heading)
