def create_sorted_key_list(input_file, output_file):
    # Open the input CSV file
    file = open(input_file, "r")
    header = file.readline()  # read the first line (column names)

    # Split the header into column names
    columns = header.strip().split(",")

    # Find the column index of "key"
    key_index = columns.index("key")

    # Dictionary to count how often each key appears
    key_counts = {}

    # Count key occurrences
    for line in file:
        parts = line.strip().split(",")
        song_key = parts[key_index]

        if song_key in key_counts:
            key_counts[song_key] += 1
        else:
            key_counts[song_key] = 1

    file.close()

    # Sort keys from most common → least common
    sorted_keys = sorted(key_counts, key=lambda k: key_counts[k], reverse=True)

    # Write keys + counts to output file
    out = open(output_file, "w")
    for k in sorted_keys:
        out.write(k + " : " + str(key_counts[k]) + "\n")
    out.close()

    print("Finished! Keys with counts written to:", output_file)



# Call the function, save output in your Downloads
create_sorted_key_list(
    "/Users/khush/Downloads/spotify-2023.csv",
    "C:/Users/khush/Downloads/sorted_keys.txt"
)

