import math
from src.statistics.Statistics import Statistics

# create method to add, subtract, multiply, divide, square and square root
stat = Statistics()


def population_mean(number_list):
    return stat.population_mean(number_list)


def median(number_list):
    return stat.median(number_list)


def pop_standard_deviation(number_list):
    return stat.pop_standard_deviation(number_list)


def mode(number_list):
    return stat.mode(number_list)


def variance_pop_proportion(number_list):
    return stat.variance_pop_proportion(number_list)


def zscore(number_list):
    return stat.zscore(number_list)

def standardized_score(number_list):
    return stat.standardized_score(number_list)

def population_corre_coefficient(number_list):
    return stat.population_corre_coefficient(number_list)

def confidence_interval(number_list):
    return stat.confidence_interval(number_list)

def population_variance(number_list):
    return stat.population_variance(number_list)

def p_value(number_list):
    return stat.p_value(number_list)

def proportion(number_list):
    return stat.proportion(number_list)

def sample_mean(sample_size):
    return stat.sample_mean(sample_size)

def sample_standard_deviation(sample_size):
    return stat.sample_standard_deviation(sample_size)

def variance_sample_proportion(sample_size):
    return stat.variance_sample_proportion(sample_size)


# add (return the value of the sum of num1 and num2)
def add_vals(num1, num2):
    int(num1)
    int(num2)
    return num1 + num2


# subtract (return the value of the difference of num1 and num2)
def subtract_vals(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num2 - num1


# multiply(return the value of the product of num1 and num2)
def multiply_vals(num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    return num1 * num2


def divide_vals(num1, num2):
    return num2 / num1


def square_root_val(num):
    float(num)
    return math.sqrt(num)


def square_number_val(num):
    int(num)
    return num * num


class Calculator:
    value = 0

    def __init__(self):
        pass

    def population_mean(self, number_list):
        self.value = population_mean(number_list)
        return self.value

    def median(self, number_list):
        self.value = median(number_list)
        return self.value

    def pop_standard_deviation(self, number_list):
        self.value = pop_standard_deviation(number_list)
        return self.value

    def mode(self, number_list):
        self.value = mode(number_list)
        return self.value

    def variance_pop_proportion(self, number_list):
        self.value = variance_pop_proportion(number_list)
        return self.value

    def zscore(self, number_list):
        self.value = zscore(number_list)
        return self.value

    def standardized_score(self, number_list):
        self.value = standardized_score(number_list)
        return self.value

    def population_corre_coefficient(self, number_list):
        self.value = population_corre_coefficient(number_list)
        return self.value

    def confidence_interval(self, number_list):
        self.value = confidence_interval(number_list)
        return self.value

    def population_variance(self, number_list):
        self.value = population_variance(number_list)
        return self.value

    def p_value(self, number_list):
        self.value = p_value(number_list)
        return self.value

    def proportion(self, number_list):
        self.value = proportion(number_list)
        return self.value

    def sample_mean(self, sample_size):
        self.value = sample_mean(sample_size)
        return self.value

    def sample_standard_deviation(self, sample_size):
        self.value = sample_standard_deviation(sample_size)
        return self.value

    def variance_sample_proportion(self, sample_size):
        self.value = variance_sample_proportion(sample_size)
        return self.value


    def add(self, num1, num2):
        self.value = add_vals(num1, num2)
        return self.value

    def subtract(self, num1, num2):
        self.value = subtract_vals(num1, num2)
        return self.value

    def multiply(self, num1, num2):
        self.value = multiply_vals(num1, num2)
        return self.value

    def divide(self, num1, num2):
        self.value = divide_vals(num1, num2)
        return round(float(self.value), 8)

    def square_root(self, num1):
        self.value = square_root_val(num1)
        return self.value

    def square_number(self, num1):
        self.value = square_number_val(num1)
        return self.value

