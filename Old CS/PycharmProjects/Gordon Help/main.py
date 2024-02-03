# "On my honor, as a CCSF student, I Nathan tjong have neither given or received inappropriate help with this assignment."
import random

TEST_DBG = True


def generate_20_rand_ints():
    """
    generates 20 random integers between 1 and 20, using the seed value
    23 so that the list is always the same.
    No parameters
    returns a list containing the 10 integers
    """
    NUM_RANDS = 20

    rand = random.Random()  # module.ObjectConstructor(),
    # as in turtle.Turtle()
    rand.seed(23)

    # LAB 8 PART 1: delete the line below that creates the "random" int list
    # [1,2,3,…,18,19,20], and uncomment and complete the line beneath, which
    # will create a much more random list of 20 ints, each ≥ 1, and ≤ 20.
    # You will know your program is correct when it passes test 1 below.
    randoms = [rand.randint(1, 21) for idx in range(1, 21)]
    return randoms


def moving_7day_mean(nums):
    '''
Compute a 7 item average for the list nums, and returns the result in a list
of floats.
moving_7day_mean parameter: a list of at least 7 items, which 
each item is an int or float.
moving_7day_mean returns a list len(nums) - 6 floats,
where each float is the mean of 7 items
moving_7day_mean error return: bad parameter message if len(nums) < 7, or
if each item in nums is not an int for a float.
   '''
    averages = []
    week_sum = 0
    for idx, num in enumerate(nums):
        print(idx, num)
        week_sum += num
        if idx < 6:
            continue
        # LAB 8 PART II.  Uncomment and complete the next two line to compute
        # the average 7-day moving average
        elif idx > 6:
            week_sum -= nums[idx-7]

        averages.append(week_sum / 7)

    return averages


if __name__ == '__main__':
    # test code for functions in DataLibs-Lab
    num_tests = 0
    num_pass = 0
    print('*** Start DataLibs-Lab validation suite ***\n')
    print('Section 1: generate_20_rand_ints()')
    print('**generate_20_rand_ints() docstring:',
          generate_20_rand_ints.__doc__.rstrip())
    print('** end docstring')
    randoms = generate_20_rand_ints()
    print('\nTest 1, Numbers generated for seed 23.')
    num_tests += 1
    expected = [10, 3, 1, 19, 10, 14, 13, 17, 12, 5, 7, 9, 15, 1, 8, 20, 15, 1, 4, 3]
    print(f'    Expected: {expected}')
    print(f'    Actual:   {randoms}')
    if randoms == expected:
        print('PASS!')
        num_pass += 1
    else:
        print('FAIL :-(')

    print('\nSection 2: moving_7day_mean()')
    # Note — the tests in section 2 will fail unless test 1 in section 1 passed
    print('** moving_7day_mean() docstring:',
          moving_7day_mean.__doc__.rstrip())
    print('** end docstring')
    print('\nTest 2, 7 day moving averages for numbers generated in section 1.')
    num_tests += 1
    means = moving_7day_mean(randoms)  # randoms generated in section 1
    means_str_list = [f'{m:.02f}' for m in means]
    expected = \
        ['10.00', '11.00', '12.29', '12.86', '11.14', '11.00', '11.14', '9.43', '8.14', '9.29', '10.71', \
         '9.86', '9.14', '7.43']
    print(f'    Expected: {expected}')
    print(f'    Actual:   {means_str_list}')
    if means_str_list == expected:
        print('PASS!')
        num_pass += 1
    else:
        print('FAIL :-(')

    # Style note: The 2-line code for writing the summary reflects a preference
    # for avoiding long source code lines.
    fail = num_tests - num_pass
    s = f'{num_tests}; # Pass: {num_pass}; # Failures: {fail}'
    print('\nSummary. # tests: ' + s)
    print('*** End DataLibs_-Lab validation suite ***')
