from google.appengine.ext import vendor

# Add any libraries installed in the "lib" folder.
vendor.add('lib')

## to install other libraries, go to app root folder and type
## pip install -t lib <lib name>
## see https://cloud.google.com/appengine/docs/python/tools/libraries27#vendoring