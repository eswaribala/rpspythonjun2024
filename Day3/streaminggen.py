def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
# Create a generator object for reading a large file
file_gen = read_large_file('prices.csv')
# Print each line in the large file
for line in file_gen:
    print(line)