import random
from concurrent.futures import ThreadPoolExecutor

def getDNASamples():
    alphabet = ['A', 'T', 'G', 'C']
    random.seed(43)
    list = [''.join(''.join([random.choice(alphabet) for x in range(10000)])) for y in range(100)]
    return list


def find_sequence(sample, idx, sequence):
    index = sample.find(sequence)

    if index != -1:
        return "DNA sequence found în sample " + str(idx)
    else:
        return ""
        
 
if __name__ == '__main__':
    dna_list = getDNASamples()
    sequence = "CGATGGCAA"

    with ThreadPoolExecutor(max_workers = 30) as executor:
        results = executor.map(find_sequence, dna_list, [x for x in range(len(dna_list))], [sequence for _ in range(len(dna_list))])
    
    for result in results:
        if result != "":
            print(result)
 
