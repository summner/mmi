#!/usr/bin/env python

import csv, matplotlib, re
import numpy as np
import matplotlib.pyplot as plt
import matplotlib

from pylab import *

matplotlib.use('Agg')

files = ['x/rsel.csv', 'x/cel-rs.csv', 'x/2cel-rs.csv', 'x/cel.csv', 'x/2cel.csv']
colors = ['blue', 'green', 'red', 'black', 'violet']
names = [ '1-Evol-RS', '1-Coev-RS', '2-Coev-RS', '1-Coev', '2-Coev']
#
#names = [ '' ]
plt.axis([0, 500000, 0.6, 1.0])

for filename, color, label in zip(files, colors, names):
    with open(filename, 'rb') as f:
        r = csv.reader(f)
        headers = r.next()
        prows = []
        efforts = []
        generations = []
        all_runs = []
        for row in r:
            runs = {}
            bunch = []
            rest = {}

            for header, item in zip(headers, row):
                if header.startswith("run-"):
                    bunch.append(float(item))
                else:
                    rest[header] = item

            efforts.append(rest['effort'])
            generations.append(rest['generation'])
            all_runs.append(bunch)

        p = plt.plot(efforts, map(lambda runs: np.mean(runs), all_runs),
                 color=color)
        # plt.setp(p, label=label)
plt.xlabel("Rozegranych gier")
plt.ylabel("Odsetek wygranych gier")
plt.legend(names, loc=4)

plt.show()
print prows

