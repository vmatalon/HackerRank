import sys
import numpy as np
from scipy import stats

this_input = sys.stdin.readlines()

T = int(this_input[0].strip())

for t in range(0,T): # For each Test Case
    # Extract the Data from Input
    i = 7*t
    N = int(this_input[i+1].strip())
    gpa = np.fromstring(this_input[i+2], dtype=float, sep=' ') 
    test_1 = np.fromstring(this_input[i+3], dtype=float, sep=' ')
    test_2 = np.fromstring(this_input[i+4], dtype=float, sep=' ')
    test_3 = np.fromstring(this_input[i+5], dtype=float, sep=' ')
    test_4 = np.fromstring(this_input[i+6], dtype=float, sep=' ')
    test_5 = np.fromstring(this_input[i+7], dtype=float, sep=' ')
    tests = [test_1, test_2, test_3, test_4, test_5]

    # Calculate Correlation between Aptitude Test Results and GPA
    correlations = [stats.pearsonr(gpa,test)[0] for test in tests]

    # Return Aptitude Test Number
    print(correlations.index(max(correlations)) + 1)
