# Copyright (C) 2021-22 Intel Corporation
# SPDX-License-Identifier: BSD-3-Clause
# See: https://spdx.org/licenses/

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.collections as mc

def generate_post_spikes(pre_spike_times, num_steps, spike_prob_post):
    """generates specific post synaptic spikes to
    demonstrate potentiation and depression.
    """
    pre_synaptic_spikes = np.where(pre_spike_times == 1)[1]

    spike_raster_post = np.zeros((len(spike_prob_post), num_steps))

    for ts in range(num_steps):
        for pre_ts in pre_synaptic_spikes:
            if ts in range(pre_ts, pre_ts + 20):
                if np.random.rand(1) < spike_prob_post[0]:
                    spike_raster_post[0][ts] = 1

    for ts in range(num_steps):
        for pre_ts in pre_synaptic_spikes:
            if ts in range(pre_ts - 12, pre_ts - 2):
                if np.random.rand(1) < spike_prob_post[1]:
                    spike_raster_post[1][ts] = 1

    return spike_raster_post


def plot_spikes(spikes, figsize, legend, colors, title, num_steps):
    offsets = list(range(1, len(spikes) + 1))
    num_x_ticks = np.arange(0, num_steps + 1, 2)

    plt.figure(figsize=figsize)

    plt.eventplot(positions=spikes,
                  lineoffsets=offsets,
                  linelength=0.9,
                  colors=colors)

    plt.title(title)
    plt.xlabel("Time steps")
    plt.ylabel("Neurons")

    plt.xticks(num_x_ticks)
    plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
    plt.grid(which='major', color='lightgray', linewidth=0.8)
    plt.minorticks_on()

    plt.yticks(ticks=offsets, labels=legend)

    plt.show()


# def plot_spikes_dotted(spikes, figsize, legend, colors, title, num_steps):

#     offsets = list(range(1, len(spikes) + 1))
    
#     num_x_ticks = np.arange(0, num_steps + 1, 1)
    
#     plt.figure(figsize=figsize)
    
#     for i in range(len(spikes)):
#         ones_idx = np.where(spikes[i] == 1)[0]

#         first_one = ones_idx[0]
        
#         if len(ones_idx) > 1:
#             second_one = ones_idx[1]
        
#         if i < (len(spikes) - 1):
#             lines = plt.eventplot(positions=[first_one], 
#                                   lineoffsets=i+1,  
#                                   linelengths=0.9, 
#                                   colors=colors[i])
            
#             coll = lines[0]

#             plt.eventplot(positions=[second_one], 
#                           lineoffsets=i+1, 
#                           linelengths=0.9, 
#                           colors=colors[i], 
#                           linestyle='loosely dashed')
            
#         else:
#             plt.eventplot(positions=[first_one], 
#                         lineoffsets=i+1,  
#                         linelengths=0.9, 
#                         colors=colors[i])

#     plt.title(title)
#     plt.xlabel("Time steps")
#     plt.ylabel("Neurons")

#     plt.xticks(num_x_ticks)
#     plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
#     plt.grid(which='major', color='lightgray', linewidth=0.8)
#     plt.minorticks_on()

#     plt.yticks(ticks=offsets, labels=legend)

#     plt.show()

def plot_spikes_dotted(spikes, figsize, legend, colors, title, num_steps):

    offsets = list(range(1, len(spikes) + 1))
    
    num_x_ticks = np.arange(0, num_steps + 1, 1)
    
    plt.figure(figsize=figsize)
    
    for i in range(len(spikes)):
        ones_idx = np.where(spikes[i] == 1)[0]

        first_one = ones_idx[0]
        
        if len(ones_idx) > 1:
            second_one = ones_idx[1]
        
        if i < (len(spikes) - 1):
            plt.plot([first_one, first_one], [i+0.05, i+0.95], color=colors[i])
            plt.plot([second_one, second_one], [i+0.05, i+0.95], color=colors[i], linestyle='dashed')
        else:
            plt.plot([first_one, first_one], [i+0.05, i+0.95], color=colors[i])

    plt.title(title)
    plt.xlabel("Time steps")
    plt.ylabel("Neurons")

    plt.xticks(num_x_ticks)
    plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
    plt.grid(which='major', color='lightgray', linewidth=0.8)
    plt.minorticks_on()

    plt.yticks(ticks=offsets, labels=legend)

    plt.show()

def plot_time_series(time, time_series, ylabel, title, figsize, color):
    plt.figure(figsize=figsize)
    plt.step(time, time_series, color=color)

    plt.title(title)
    plt.xlabel("Time steps")
    plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
    plt.grid(which='major', color='lightgray', linewidth=0.8)
    plt.minorticks_on()

    plt.ylabel(ylabel)

    plt.show()


def plot_time_series_subplots(time, time_series_y1, time_series_y2, ylabel,
                              title, figsize, color, legend,
                              leg_loc="upper left"):
    plt.figure(figsize=figsize)

    plt.step(time, time_series_y1, label=legend[0], color=color[0])
    plt.step(time, time_series_y2, label=legend[1], color=color[1])

    plt.title(title)
    plt.xlabel("Time steps")
    plt.ylabel(ylabel)
    plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
    plt.grid(which='major', color='lightgray', linewidth=0.8)
    plt.minorticks_on()
    plt.xlim(0, len(time_series_y1))

    plt.legend(loc=leg_loc)

    plt.show()


def plot_spikes_time_series(time, time_series, spikes, figsize, legend,
                            colors, title, num_steps):

    offsets = list(range(1, len(spikes) + 1))
    num_x_ticks = np.arange(0, num_steps + 1, 25)

    plt.figure(figsize=figsize)

    plt.subplot(211)
    plt.eventplot(positions=spikes,
                  lineoffsets=offsets,
                  linelength=0.9,
                  colors=colors)

    plt.title("Spike Arrival")
    plt.xlabel("Time steps")

    plt.xticks(num_x_ticks)
    plt.xlim(0, num_steps)
    plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
    plt.grid(which='major', color='lightgray', linewidth=0.8)
    plt.minorticks_on()

    plt.yticks(ticks=offsets, labels=legend)
    plt.tight_layout(pad=3.0)

    plt.subplot(212)
    plt.step(time, time_series, color=colors)

    plt.title(title[0])
    plt.xlabel("Time steps")
    plt.grid(which='minor', color='lightgrey', linestyle=':', linewidth=0.5)
    plt.grid(which='major', color='lightgray', linewidth=0.8)
    plt.minorticks_on()
    plt.margins(x=0)

    plt.ylabel("Trace Value")

    plt.show()
