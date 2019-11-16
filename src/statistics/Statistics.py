import math

from src.statistics.StatisticsAbstract import StatisticsAbstract
from src.statistics.GetSample import GetSample


def population_mean(number_list):
    # population mean formula:
    number_list = list(number_list)
    sum_value = 0

    for x in number_list:
        sum_value = sum(number_list)

    # take the sum of the items and then divide it by the number of items
    number_count = len(number_list)

    result = sum_value / number_count
    # then return that value
    return result


def median(number_list):
    # first sort the list
    number_list = list(number_list)
    number_list.sort()

    # take the list and get the value at the middle of the number list
    if len(number_list) % 2 is not 0:
        middle_val_index = int(len(number_list) / 2)

        middle_val = number_list[middle_val_index]

        # self.result = middle_val
        return middle_val

    else:
        # if the number count of the list is even, take the middle two numbers... add them and divide by 2
        middle_val_index = int((len(number_list) - 1) / 2)
        after_middle_index = middle_val_index + 1
        # self.result = int((float(number_list[middle_val_index]) + float(number_list[after_middle_index])) / 2.0)
        return (float(number_list[middle_val_index]) + float(number_list[after_middle_index])) / 2


def pop_standard_deviation(number_list):
    # 1. Calculate the mean of number_list
    mean = population_mean(number_list)
    # 2. Subtract mean from each data point and then square each value
    new_list = []
    for x in number_list:
        new_val = x - mean
        new_val = math.pow(new_val, 2)
        new_list.append(new_val)
    # 3. Calculate the mean of the squared differences, this is the variance
    new_mean = population_mean(new_list)
    # 4. pop standard deviation is the square root of the variance
    result = math.sqrt(new_mean)

    return result


def mode(number_list):
    number_list = list(number_list)
    value_dict = {}
    mode_val = 0

    for val in number_list:
        value_dict[val] = number_list.count(val)

    for key in value_dict.keys():
        if value_dict.get(key) == max(value_dict.values()):
            mode_val = key

    return mode_val


def variance_pop_proportion(number_list):
    # the formula for this is PQ / n
    # P is the population proportion
    number_list = list(number_list)
    p = 0
    for x in number_list:
        p = p + x
    # Q is the proportion of population elements that do no have particular attr. => Q = 1  - P
    q = p - 1
    # n is the num of elements in a sample
    n = len(number_list)

    result = (p * q) / n

    return result


def p_value(number_list):
    number_list = list(number_list)
    ttest, pval = ttest(number_list, population_mean(number_list))

    return pval


def proportion(number_list):
    number_list = list(number_list)
    p = 0
    for x in number_list:
        p = p + x

    n = len(number_list)

    result = p / n

    return result


def sample_mean(number_list, sample_size):
    # population mean formula:
    number_list = list(number_list)
    sample = GetSample(number_list, sample_size)
    sum_value = 0

    for x in number_list:
        sum_value = sum(sample)

    # take the sum of the items and then divide it by the number of items
    number_count = len(sample)

    result = sum_value / number_count
    # then return that value
    return result


def sample_standard_deviation(number_list, sample_size):
    # 1. Calculate the mean of number_list
    mean = sample_mean(number_list, sample_size)
    # 2. Subtract mean from each data point and then square each value
    new_list = []
    for x in number_list:
        new_val = x - mean
        new_val = math.pow(new_val, 2)
        new_list.append(new_val)
    # 3. Calculate the mean of the squared differences, this is the variance
    new_mean = population_mean(new_list)
    # 4. pop standard deviation is the square root of the variance
    result = math.sqrt(new_mean)

    return result


def variance_sample_proportion(number_list, sample_size):
    # the formula for this is SQ / n
    # S is the sample proportion
    number_list = list(number_list)
    sample = GetSample(number_list, sample_size)
    s = 0
    for x in number_list:
        s = s + x
    # Q is the proportion of population elements that do no have particular attr. => Q = 1  - S
    q = s - 1
    # n is the num of elements in a sample
    n = len(sample)

    result = (s * q) / n

    return result


class Statistics(StatisticsAbstract):

    result = 0

    def population_mean(self, number_list):
        self.result = population_mean(number_list)
        return self.result

    def median(self, number_list):
        self.result = median(number_list)
        return self.result

    def mode(self, number_list):
        self.result = mode(number_list)
        return self.result

    def pop_standard_deviation(self, number_list):
        self.result = pop_standard_deviation(number_list)
        return self.result

    def variance_pop_proportion(self, number_list):
        self.result = variance_pop_proportion(number_list)
        return self.result

    def zscore(self, number_list):
        self.result = zscore(number_list)
        return self.result

    def standardized_score(self, number_list):
        self.result = standardized_score(number_list)
        return self.result

    def population_corre_coefficient(self, number_list):
        self.result = population_corre_coefficient(number_list)
        return self.result

    def confidence_interval(self, number_list):
        self.result = confidence_interval(number_list)
        return self.result

    def population_variance(self, number_list):
        self.result = population_variance(number_list)
        return self.result

    def p_value(self, number_list):
        self.result = p_value(number_list)
        return self.result

    def proportion(self, number_list):
        self.result = proportion(number_list)
        return self.result

    def sample_mean(self, sample_size):
        self.result = sample_mean(sample_size)
        return self.result

    def sample_standard_deviation(self, sample_size):
        self.result = sample_standard_deviation(sample_size)
        return self.result

    def variance_sample_proportion(self, sample_size):
        self.result = variance_sample_proportion(sample_size)
        return self.result
