#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example for FDEM inversion using a real data example."""
import os

import numpy as np
from pygimli.physics import FDEM


datafile = os.path.dirname(__file__) + '/example.xyz'
fdem = FDEM(datafile)
print(fdem)
nlay = 4
xpos = 0
err = 0.1
name = datafile.lower().rstrip('.xyz')
fdem = FDEM(datafile)
print(fdem)
fdem.deactivate(56320.)  # do not use highest frequency
fdem.plotAllData(outname=None)
INV = fdem.invBlock(xpos=xpos, nlay=nlay, verbose=False)
model = np.asarray(INV.run())
INV.echoStatus()
print("thk = ", model[:nlay - 1])
print("res = ", model[nlay - 1:])
fig, ax = fdem.showModelAndData(model, xpos, INV.response())
# INV = fdem.inv2D(nlay)
# INV.run()
