#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division  # Division in Python 2.7
import matplotlib
# matplotlib.use('Agg')                       # So that we can render files without GUI
import matplotlib.pyplot as plt
from matplotlib import rc
import numpy as np
import colorsys
import math
# matplotlib.use('Agg')


from matplotlib import colors


def plot_color_gradients(gradients, names):
    # For pretty latex fonts (commented out, because it does not work on some machines)
    # rc('text', usetex=True)
    # rc('font', family='serif', serif=['Times'], size=10)
    rc('legend', fontsize=10)

    column_width_pt = 400  # Show in latex using \the\linewidth
    pt_per_inch = 72
    size = column_width_pt / pt_per_inch

    fig, axes = plt.subplots(nrows=len(gradients), sharex=True, figsize=(size, 0.75 * size))
    fig.subplots_adjust(top=1.00, bottom=0.05, left=0.25, right=0.95)

    for ax, gradient, name in zip(axes, gradients, names):
        # Create image with two lines and draw gradient on it
        img = np.zeros((2, 1024, 3))
        for i, v in enumerate(np.linspace(0, 1, 1024)):
            img[:, i] = gradient(v)

        im = ax.imshow(img, aspect='auto')
        im.set_extent([0, 1, 0, 1])
        ax.yaxis.set_visible(False)

        pos = list(ax.get_position().bounds)
        x_text = pos[0] - 0.25
        y_text = pos[1] + pos[3] / 2.
        fig.text(x_text, y_text, name, va='center', ha='left', fontsize=10)

    plt.show()
    # fig.savefig('my-gradients.pdf')


def hsv2rgb(h, s, v):
    if s == 0.0: return [v, v, v]
    i = int(h*6.)
    f = (h*6.)-i
    p,q,t = v*(1.0-s), v*(1.0-s*f), v*(1.0-s*(1.0-f))
    i%=6
    if i == 0: return [v, t, p]
    if i == 1: return [q, v, p]
    if i == 2: return [p, v, t]
    if i == 3: return [p, q, v]
    if i == 4: return [t, p, v]
    if i == 5: return [v, p, q]
    # c = s * v  # chroma
    # h1 = 6 * h
    # x = c * (1 - np.fabs(h1 % 2 - 1))

    #
    # (r,g,b) = (0,0,0)
    # if h1 < 0:
    #     (r, g, b) = (0, 0, 0)
    # elif h1 < 1:
    #     (r, g, b) = (c, x, 0)
    # elif h1 < 2:
    #     (r, g, b) = (x, c, 0)
    # elif h1 < 3:
    #     (r, g, b) = (0, c, x)
    # elif h1 < 4:
    #     (r, g, b) = (0, x, c)
    # elif h1 < 5:
    #     (r, g, b) = (x, 0, c)
    # elif h1 <= 6.0:
    #     (r, g, b) = (c, 0, x)
    # else:
    #     (r, g, b) = (0, 0, 0)

    # return (r, g, b)


def gradient_rgb_bw(v):
    # TODO
    return (v, v, v)


def gradient_rgb_gbr(v):
    g = 0
    r = 0
    if (v > 0.5):
        r = 2.0 * v - 1.0
    else:
        g = 1.0 - v * 2.0
    b = v * 2 - r * 2.0
    # b = 0

    return (r, g, b)


def gradient_rgb_gbr_full(v):
    r = 0
    g = 0
    if (v < 0.25):
        g = 1
        b = v * 4
    elif (v < 0.5):
        g = 2.0 - v * 4
        b = 1
    elif (v < 0.75):
        b = 1
        r = 4 * v - 2
    else:
        b = 4 - 4 * v
        r = 1
    return (r, g, b)


def gradient_rgb_wb_custom(v):
    (r, g, b) = (1, 1, 1)
    x = 7.0
    d = 1 / x
    if v < d:
        g = -v * x
    elif (v < d * 2):
        g = 0
        r = 2 - v * x
    elif (v < d * 3):
        g = v * x - 2
        r = 0
    elif (v < d * 4):
        r = 0
        b = 4 - v * x
    elif (v < d * 5):
        b = 0
        r = v * x - 4
    elif (v < d * 6):
        b = 0
        g = 6 - v * x
    elif (v < d * 7):
        b, g = 0, 0
        r = 7 - v * x

    return (r, g, b)


def gradient_hsv_bw(v):
    # TODO
    # return np.array(hsv2rgb(1, v, 1)) + np.array(hsv2rgb(1, v, 1)) + np.array(hsv2rgb(1 , v, 1))
    return hsv2rgb(0, 0, v)

def gradient_hsv_gbr(v):
    # TODO
    return hsv2rgb(120/360+240*v/360.0, 1, 1)


def gradient_hsv_unknown(v):
    # TODO
    return hsv2rgb(.3- .3*v, .6, 1)


def gradient_hsv_custom(v):
    # TODO
    return hsv2rgb(.3 + 2*v, 1, 1)


if __name__ == '__main__':
    def toname(g):
        return g.__name__.replace('gradient_', '').replace('_', '-').upper()

    gradients = (gradient_rgb_bw, gradient_rgb_gbr, gradient_rgb_gbr_full, gradient_rgb_wb_custom,
                 gradient_hsv_bw, gradient_hsv_gbr, gradient_hsv_unknown, gradient_hsv_custom)

    plot_color_gradients(gradients, [toname(g) for g in gradients])
