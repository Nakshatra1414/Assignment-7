1. What is the purpose of this program?

The purpose of this program is to analyze a Spotify dataset and determine which musical keys appear most often. It helps identify the most common and least common keys by reading the "key" column in the dataset, counting all occurrences, sorting them, and saving the results into a new file.

2. What does the program do?

This program:

Reads a CSV file containing Spotify song data

Finds the column named "key"

Counts how many times each key appears in the dataset

Sorts the keys from most common to least common

Writes the results (key + count) into a new text file

Input

The path to the Spotify dataset file (for example:
"/Users/khush/Downloads/spotify-2023.csv")

Output

A text file containing lines like:

7 : 415
1 : 380
10 : 345


(Each number represents a key and the count shows its frequency in the dataset.)

3. How do you use the program?

Save the Python file containing the function.

Make sure your Spotify dataset CSV file is saved somewhere (such as Downloads).

At the bottom of the code, call the function like this:

create_sorted_key_list(
    "/Users/khush/Downloads/spotify-2023.csv",
    "C:/Users/khush/Downloads/sorted_keys.txt"
)


Run the Python file.

After running, check your Downloads folder for the generated file
sorted_keys.txt.

This file will contain all unique keys from the dataset sorted from most common to least common, along with the number of times each one appeared.