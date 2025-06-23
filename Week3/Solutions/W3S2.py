""" 
File Handling & Generators

Iterate over the rows of a CSV file using a generator function.
"""


from random import randint

def generate_csv_data(filename, num_rows=100):
    """Generate a CSV file with random data."""
    with open(filename, 'w') as file:
        file.write("ID,Value\n")
        for i in range(num_rows):
            file.write(f"{i},{randint(1, 100)}\n")

def yield_data(filename):
    with open(filename, 'r') as file:
        for line in file.readlines():
            yield line.strip().split(',')


avg = lambda data: sum(data) / len(data) if data else 0

    

if __name__ == "__main__":
    #generate_csv_data('../Data/data.csv', 1000)
    print("Data from CSV file:")
    data = []
    for i, pt in yield_data('./Data/data.csv'):
        if i == 'ID':
            continue
        #print(f'{int(pt)}: {type(pt)}')
        data.append(int(pt))
        print(f'{i}: {pt}, avg: {avg(data)}')
        