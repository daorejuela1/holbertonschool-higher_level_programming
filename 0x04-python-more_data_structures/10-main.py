#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

a_dictionary = {'John': 0, 'Bob': 1, 'Mike': 2, 'Molly': 3, 'Adam': 5}
best_key = best_score(a_dictionary)
print("Best score: {}".format(best_key))

best_key = best_score(None)
print("Best score: {}".format(best_key))

