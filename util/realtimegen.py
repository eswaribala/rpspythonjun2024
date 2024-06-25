from time import sleep


def read_large_file(file_path):
    with open(file_path, 'r') as file:
        for line in file:
            yield line
            sleep(1)


# Create a generator object for reading a large file

# Print each line in the large file
for line in read_large_file('prices.csv'):
    print(line)
