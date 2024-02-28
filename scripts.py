import os
import socket
from collections import Counter

# Define the file paths
data_directory = '/home/data'
output_directory = '/home/output'
result_file_path = '/home/output/result.txt'

# List all text files in the directory by name
def list_files(directory):
    files = os.listdir(directory)
    text_files = [file for file in files if file.endswith('.txt')]
    return text_files

# Read the number of words in a text file
def count_words(file_path):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)

# Find the top N words with maximum counts in a text file
def find_top_words(file_path, n=3):
    with open(file_path, 'r') as file:
        text = file.read()
        words = text.split()
        word_counts = Counter(words)
        top_words = word_counts.most_common(n)
        return top_words

# Get the IP address of the machine
def get_ip_address():
    return socket.gethostbyname(socket.gethostname())

# Perform the required tasks
def perform_tasks():
    data_files = list_files(data_directory)
    total_words = 0
    file_word_counts = {}
    top_words_IF = []

    ip_address = get_ip_address()

    # Write the output to the result file
    with open(result_file_path, 'w') as result_file:
        result_file.write(f'List of text files at location {data_directory}:\n')
        for file_name in data_files:
            result_file.write(f'{file_name}\n')

        for file_name in data_files:
            file_path = os.path.join(data_directory, file_name)
            words_count = count_words(file_path)
            total_words += words_count
            if file_name == 'IF.txt':
                top_words_IF = find_top_words(file_path)

        result_file.write('\nWord count for each text file:\n')
        for file_name in data_files:
            words_count = count_words(os.path.join(data_directory, file_name))
            result_file.write(f'{file_name}: {words_count} words\n')

        result_file.write('\nTop 3 words with counts in IF.txt:\n')
        for word, count in top_words_IF:
            result_file.write(f'{word}: {count}\n')

        result_file.write(f'\nTotal number of words in all files: {total_words}\n')
        result_file.write(f'IP Address: {ip_address}\n')

    # Read the output file and print its content
    with open(result_file_path, 'r') as result_file:
        print(result_file.read())

# Main function
def main():
    perform_tasks()

if __name__ == '__main__':
    main()