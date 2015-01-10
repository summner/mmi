#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 50
T = 2

n = T * w
t = linspace(0, T, n, endpoint=False)

f = lambda t : sin(2*pi*t)  # def. funkcji
signal = f(t)                 # funkcja sprÃ³bkowana

subplot(211)
plot(t, signal, '*')
signal1 = fft(signal)
signal1 = abs(signal1)        # moduÅ‚

subplot(212)
freqs = range(n)              # <-- ZACZNIJ TUTAJ. UÅ¼yj linspace
stem(freqs, signal1, '-*')
xticks(arange(0, w, 1.0))

show()