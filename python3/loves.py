import sys

# take the names from argv
first_name = sys.argv[1]
second_name = sys.argv[2]
sentence = '{} loves {}'.format(first_name, second_name)
# first remove the space and lower the sentence
sentence = sentence.replace(' ', '').lower()

# variable to store numbers
intermediate = ''

# now loop the sentence to build the numbers from it
while len(sentence):
    # find the occurrence of the first char
    intermediate += str(sentence.count(sentence[0]))
    # remove the entire first char from string
    sentence = sentence.replace(sentence[0], '')

# now lets calculate the percentage
while int(intermediate) > 100:
    tmp = ''
    for i in range(0, int(len(intermediate) / 2)):
        # add the first and the last, and continue
        tmp += str(int(intermediate[i]) + int(intermediate[(i + 1) * -1]))

    # if it's odd
    if (len(intermediate) % 2) > 0:
        # add the number from middle
        tmp += intermediate[int(len(intermediate) % 2)]

    # replace the intermediate variable
    intermediate = tmp

# print the results
print(
    "Love percentage between {} and {} is {}%".format(
        first_name,
        second_name,
        intermediate
    )
)
