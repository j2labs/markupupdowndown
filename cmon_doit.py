#!/usr/bin/env python

"""
This script converts Markdown files in the current directory into HTML. The
mechanism is simply to put the head first, rendered markdown and then the
footer.

Some javascript is included for syntax highlighting in browsers that support
javascript.

This script makes use of the markdown2 module, which is recently added to the
project requirements file. If you need to install it, use this:

    pip install markdown2

"""

import markdown2
import fnmatch
import os

from upupdowndown import header_file, footer_file, src_dir, html_dir

### Documentation themes are *just* headers and footers
header_data = open(header_file, 'r').read()
footer_data = open(footer_file, 'r').read()


for filename in os.listdir(src_dir):
    if fnmatch.fnmatch(filename, '*.md'):
        print 'Working on:', filename
        file_path = '%s%s' % (src_dir, filename)
        
        fd = open(file_path, 'r')
        #fd.readline() # ignore first line
        data = fd.read()
        fd.close()
        
        marked_up = markdown2.markdown(data)
        
        new_filename = filename[:-3] # remove '.md'
        new_filename = os.path.basename(new_filename)
        new_filename = new_filename.lower()

        # Change <pre><code> to use prettify javascript
        marked_up = marked_up.replace('<pre><code>',
                                      '<pre><code class="prettyprint">')
        
        html_filepath = '%s%s.html' % (html_dir, new_filename)
        print '   writing:', html_filepath

        rendered_fd = open(html_filepath, 'w')
        rendered_fd.write(header_data)
        rendered_fd.write(marked_up.encode('utf8'))
        rendered_fd.write(footer_data)
        rendered_fd.close()
    
