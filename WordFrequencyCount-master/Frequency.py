# CSC-11300 Final Project
# Frequency.py
# Description: This class reads the file(Words.txt by default) and calculate the frequencies
import math


class Frequency (object):
    def __init__(self, filename='Words.txt'):
        self.total_count = 0  # Total count
        self.freq_dict = dict()  # Frequencies
        self.prob_dict = dict()  # Probabilities
        self.angle_dict = dict()  # Angles

        # Open the file and read
        file = open(filename, 'r')
        content = file.read()

        # Counting and storing info
        for char in content:
            self.total_count = self.total_count + 1
            self.freq_dict[char] = self.freq_dict.get(char, 0) + 1

        self.freq_dict['white space'] = self.freq_dict.pop(' ')

        # Close the file
        file.close()

        # Calculate the probabilities and angles
        for char in self.freq_dict:
            self.prob_dict[char] = self.freq_dict[char] / self.total_count
            self.angle_dict[char] = self.prob_dict[char] * math.pi * 2
