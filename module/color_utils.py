import numpy


def get_avg_color(frame):
    avg_color_per_row = numpy.average(frame, axis=0)
    avg_color = numpy.average(avg_color_per_row, axis=0)
    return avg_color
