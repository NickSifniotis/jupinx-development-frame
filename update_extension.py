#!/opt/anaconda3/bin/python

# Synchronise the extension directory to incorporate the latest development code
# in the sphinxcontrib-jupyter repository.

# The changes are pulled directly from the development folders on this computer.

import dirsync
import os

extension_development_location = "/home/nsifniotis/PycharmProjects/sphinxcontrib-jupyter/sphinxcontrib"
local_extension_copy = "extension/"

if not os.path.isdir(extension_development_location):
    print("Critical Error: Unable to locate the development copy of Jupinx. Are you sure it is in "
          + extension_development_location + "?")
    exit(1)

if not os.path.isdir(local_extension_copy):
    os.mkdir(local_extension_copy)
    print("Created directory for local copy of extension.")

dirsync.sync(extension_development_location,
             local_extension_copy,
             'sync')

print("Extension updated! Run make jupyter to test it.")
# That's all folks!
