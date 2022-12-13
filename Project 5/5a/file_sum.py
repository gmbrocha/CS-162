# Author: Glen Brochard
# GitHub username: nezcoupe
# Date: 10/23/2022
# Description: function that uses the read and write methods to sum the numbers contained in a text file that is passed
# to it; outputs that sum to a new file called sum.txt

def file_sum(num_txt):
    """function that opens input text file and sums the numbers contained in it; then writes that sum to a new text
    file, utilizing the write function"""
    sum_of_file = 0  # initialize sum
    with open(num_txt, 'r') as infile:  # open text file that is passed to file_sum()
        for line in infile:  # iterate lines in infile
            num_in = line.strip()  # strip \n
            sum_of_file += float(num_in)  # cast num_in as a float for addition

    with open("sum.txt", 'w') as outfile:  # open new text file for writing
        outfile.write(str(sum_of_file))  # cast sum_of_file as str for write method


# file_sum("Numbers.txt")
