import os
import sys
import datetime
# Basic information about the site.
SITENAME = 'Apache Infra Actions'
SITEDESC = 'Test site for Infra actions'
SITEDOMAIN = 'infra.apache.org'
SITEURL = 'https://infra.apache.org'
SITELOGO = 'https://infra.apache.org/images/AOO4_website_logo.png'
SITEREPOSITORY = 'https://github.com/apache/infrastructure-actions/testsite/'
CURRENTYEAR = datetime.date.today().year
NOW = datetime.datetime.now()
TRADEMARKS = ''
TIMEZONE = 'UTC'
# Theme includes templates and possibly static files
THEME = 'simple' # a built-in theme
# Specify location of plugins, and which to use
PLUGIN_PATHS = [ 'plugins' ] # For local plugins
PLUGINS=['gfm','missing'] # gfm must be loaded before asfreader
# This file is imported twice
if len(sys.argv) > 3:
    # print(f"sys.argv: {sys.argv}",file=sys.stderr)
    over = sys.argv[3] # PLUGIN_PATHS=["plugins", "/home/runner/work/_actions/..."]
    # print(over, file=sys.stderr)
    pdir = eval(over.split('=')[1])[-1] # get array and extract last value
    # print(pdir, file=sys.stderr)
    # Test all the plugins
    names=PLUGINS
    try:
        for f in sorted(os.listdir(pdir)):
            if f.endswith('.py'):
                names.append(os.path.splitext(f)[0])
            if os.path.isdir(os.path.join(pdir,f)):
                names.append(f)
    except FileNotFoundError:
        pass
    PLUGINS = names
print(PLUGINS, file=sys.stderr)
ASF_RUN = [ '/bin/bash show_environ.sh start' ]
ASF_POSTRUN = [ '/bin/bash show_environ.sh end' ]

# All content is located at '.' (aka content/ )
PAGE_PATHS = [ 'pages' ]
STATIC_PATHS = [ '.',  ]
# Where to place/link generated pages

PATH_METADATA = 'pages/(?P<path_no_ext>.*)\\..*'

PAGE_SAVE_AS = '{path_no_ext}.html'
# Don't try to translate
PAGE_TRANSLATION_ID = None
# Disable unused Pelican features
# N.B. These features are currently unsupported, see https://github.com/apache/infrastructure-pelican/issues/49
FEED_ALL_ATOM = None
INDEX_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
ARCHIVES_SAVE_AS = ''
# Disable articles by pointing to a (should-be-absent) subdir
ARTICLE_PATHS = [ 'blog' ]
# needed to create blogs page
ARTICLE_URL = 'blog/{slug}.html'
ARTICLE_SAVE_AS = 'blog/{slug}.html'
# Disable all processing of .html files
READERS = { 'html': None, }

# Configure the asfgenid plugin
ASF_GENID = {
 'unsafe_tags': True,
 'metadata': True, # to pick up {{metadata}} references in MD files
 'elements': True,
 'permalinks': True,
 'tables': True,

 'headings': True,
 'headings_re': '^h[1-4]',


 'toc': True,
 'toc_headers': '^h[1-6]',

 'debug': False,
}
