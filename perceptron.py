import random

LIMIT_ITER = 100000

def gen_weights(dimensionality):
    weights = []
    for _ in range(0, dimensionality + 1):
        weights.append(random.random())
    return weights


def read_input():
    """ This function reads the input and parses the input
    RETURNS:
    the parsed inputs
    """
    d = int(input())
    m = int(input())
    n = int(input())
    training_set = []
    test_example = []
    for _ in range(m):
        l = input().replace(" ", "")
        l = l.split(',')
        l = [float(i) for i in l]
        training_set.append(l)
    for _ in range(n):
        l = input().replace(" ", "")
        l = l.split(',')
        l = [float(i) for i in l]
        test_example.append(l)
    return d, m, n, training_set, test_example

def perceptron_algorithm(training_set, test_set, weights, learning_rate, errors, t):
    while errors != False and t < LIMIT_ITER:
        errors = False
        for points in training_set:
            desired = points[-1]
            points = points[:-1]
            points.append(1.0) 

            desired_comp = [float(points[i]) * weights[i] for i in range(0, len(points))]
            desired_comp = sum(desired_comp)

            if desired_comp >= 0:
                desired_comp = 1
            else:
                desired_comp = 0

            if desired != desired_comp:
                errors = True

            for i in range(0, len(weights)):
                weights[i] += learning_rate * (desired - desired_comp) * points[i] #update weights
        t += 1
    return weights, t

def predict(weights, num_of_iterations):
    if num_of_iterations < LIMIT_ITER:
        for test in test_set:
            test.append(1.0) #bias
            prediction = 0.0
            for i in range(0, len(test)):
                prediction += float(test[i]) * weights[i]
            if prediction >= 0:
                prediction = 1
            else:
                prediction = 0
            print(prediction)
    else:
        print('no solution found')

def main():
    dimensionality, _, _, training_set, test_set = read_input()
    weights = gen_weights(dimensionality)
    new_weights, num_of_iterations = perceptron_algorithm(training_set, test_set, weights, 0.010, 1, 0)
    predict(new_weights, num_of_iterations)


if __name__ == '__main__':
    main()