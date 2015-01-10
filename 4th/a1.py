#!/usr/bin/env python
# -*- coding: utf -*-
from __future__ import division
from pylab import *
from numpy import *
from scipy import *

w = 50
T = 1

n = T * w
t = linspace(0, T, n, endpoint=False)

f = lambda t : sin(2*pi*t)  # def. funkcji
signal = f(t)                 # funkcja sprÃ³bkowana

subplot(211)
plot(t, signal, '*')
ylabel("amplituda")
xlabel("t")
signal1 = fft(signal)
signal1 = signal1
print signal1
subplot(212)
freqs = linspace(0, w, len(signal1), endpoint=False)

stem(freqs, signal1*2/n, '-*')
xticks(arange(0, w+1, 5.0))
xlabel("t")
ylabel("Amplituda")

show()