#!/opt/anaconda3/bin/python

# Synchronise the extension directory to incorporate the latest development code
# in the sphinxcontrib-jupyter repository.

# The changes are pulled directly from the development folders on this computer.

import dirsync

dirsync.sync("/home/nsifniotis/PycharmProjects/sphinxcontrib-jupyter/sphinxcontrib",
             "/home/nsifniotis/PycharmProjects/jupinx-extension-test/extension",
             'sync')

# That's all folks!
