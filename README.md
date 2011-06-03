# Markupupdowndown

Markupupdowndown is a ridiculous name for a simple script. It translates the markdown found in you `src` directory into html and puts it in your `html` directory using Trent Mick's [markdown2](https://github.com/trentm/python-markdown2) library. 

The code is available here: [https://github.com/j2labs/markupupdowndown](https://github.com/j2labs/markupupdowndown).


## Markdown2

To install `markdown2`, use the command below.

    pip install markdown2


## Using it

Open up `settings.py` and adjust as necessary.

    src_dir = './src/'
    html_dir = './html/'
    header_file = '%s%s' % (src_dir, 'header.html')
    footer_file = '%s%s' % (src_dir, 'footer.html')

Then just do it.

C'mon... do it.

    ./cmon_doit.py


## Some examples

How about some headers??


### Header3

Some text 


#### Header4

Some text 


##### Header5

Some text 


###### Header6

And maybe a list?

* bullet point a
* bullet point b
* bullet point c

And a numbered list?

1. hi
2. hi
3. hi
4. hi
5. hi

Sweet.


## License

BSD, as usual
