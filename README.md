# Pandoc ignoreheading 

A Pandoc filter that implements support for `ignoreheading` tags in
Org mode documents.  Headlines tagged with this tag are removed from
the document, but the content under those headlines remains.

This allows you to create "virtual" headlines for organizational
purposes (which can be folded, etc.) that won't appear in the exported
document.  This is especially useful for things like front matter and

For example:
```
* Here is a headline with no tag

And here is its content

* Here is one that should be ignored                 :othertag:ignoreheading:

So this content should appear below the first headline
```

## Use

Run pandoc with -F/--filter ignoreheading.py 
