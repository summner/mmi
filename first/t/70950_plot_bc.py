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
marks = [ 'o', 'v', 'D', 's', 'd' ]

plt.axis([0, 500, 0.6, 1.0])
fig = plt.figure(1)
bplotdata=[]
for filename, color, mark in zip(files, colors, marks):
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
        plt.subplot(121)
        plt.xlim([0, 500])
        plt.plot(map(lambda e: float(e)/1000.0, efforts), map(lambda runs: np.mean(runs)*100, all_runs),
                 color=color, markevery=20, marker=mark)
        # bplotdata.append(map(lambda runs: np.mean(runs), all_runs))
        bplotdata.append(np.array(all_runs).flatten()*100)

    # bplotdata.append(map(lambda runs: np.mean(runs), all_runs))

print len(bplotdata)
print len(names)
plt.subplot(122)
plt.grid()
plt.boxplot( bplotdata, notch=True, whis = [10, 90],
             showmeans=True, meanprops={'marker': 'o','color': 'b'}, flierprops={'markevery': 100} )
ax = plt.gca()
ax.set_xticklabels(names)
locs, labels = plt.xticks()
plt.setp(labels, rotation=30)
plt.ylim([60, 100])
ax.yaxis.tick_right()

plt.subplot(121)
plt.grid()
plt.xlabel("Rozegranych gier (x1000)")
plt.ylabel("Odsetek wygranych gier [%] ")
plt.legend(names, loc=4)

ax = plt.gca()
ax2 = ax.twiny()
ax2.set_xlabel("Pokolenie")
ax2.set_xticklabels([0, 40, 80, 120, 160, 200])

plt.show()
print prows

