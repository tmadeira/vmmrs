line_styles = ["solid", "dotted", "dashed"]


def tex_plot(x, y):
    print("\\addplot coordinates {")
    for i in range(len(x)):
        print("  (%d, %.6f)" % (x[i], y[i]))
    print("};")


# Welford's online algorithm implementation from
# https://en.wikipedia.org/wiki/Algorithms_for_calculating_variance
# For a new value new_value, compute the new count, new mean, the new M2.
# mean accumulates the mean of the entire dataset
# M2 aggregates the squared distance from the mean
# count aggregates the number of samples seen so far
def update_agg(existing_aggregate, new_value):
    (count, mean, M2) = existing_aggregate
    count += 1
    delta = new_value - mean
    mean += delta / count
    delta2 = new_value - mean
    M2 += delta * delta2
    return (count, mean, M2)


# Retrieve mean and variance from an aggregate
def mean_and_variance(existing_aggregate):
    (count, mean, M2) = existing_aggregate
    return (mean, M2 / count)
