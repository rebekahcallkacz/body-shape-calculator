# This script calculates body shape using bust, waist and hip measurements.
# Measurements should be in inches.

# Input should be the three measurements as integers/floats, and output will be a string containing the body shape label.
def calculate_shape(bust, waist, hips):
    # determine if bust is 5% bigger than hips
    if bust/hips >= 1.05:
        shape = 'inverted triangle'

    # determine if waist is less than 25% smaller than bust and bust/hips measurements are within 5% of each other
    # create a list of all measurements
    measure_list = [bust, hips]

    # determine the largest measurement
    largest_measure = max(measure_list)

    # remove the largest measurement from the list
    measure_list.remove(largest_measure)

    if waist/bust >= 0.75 and [measure > largest_measure * 0.95 for measure in measure_list]:
        shape = 'rectangle'

    # determine if hips are at least 5% bigger than bust
    if hips/bust >= 1.05:
        shape = 'triangle'

    # determine if waist is at least 25% smaller than bust and hips
    if waist/bust <= 0.75 and waist/hips <= 0.75:
        shape = 'hourglass'

    return shape