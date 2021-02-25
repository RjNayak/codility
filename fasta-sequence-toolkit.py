
'''
The toolkit for FASTA sequence file operations
'''
import sys


class fasta_file_tools():

    '''
    The function is used to load a file to the program
    '''

    def __init__(self, filename):
        self.filename = filename
        self.dict = {}
        f_reader = open(self.filename)
        for line in f_reader:
            line = line.strip("\n")
            if ">" in line:
                header = line
                self.dict[header] = ""
            else:
                self.dict[header] += line
        f_reader.close()

    '''
    The function reads a FASTA file and returns the number of records in the file
    '''

    def find_no_of_records(self):

        print("Total number of records are in the multi-FASTA file: %d \n" %
              len(self.dict))

    '''
    The function is used to get the lenght of seequences in the file along with the longest and shortest sequence length
    '''

    def find_seq_length_data(self):
        length_dict = {}
        for key, value in self.dict.items():
            length_dict[key] = len(value)

        max_length = max(length_dict.values())
        print("The length of the longest sequence: %d \n" % max_length)

        min_length = min(length_dict.values())
        print("The length of the shortest sequence: %d \n" % min_length)

        record_max_length = [
            item for item in length_dict if length_dict[item] == max_length]
        print("The number of records with longest sequence: %d \n" %
              len(record_max_length))

        record_min_length = [
            item for item in length_dict if length_dict[item] == min_length]
        print("The number of records with shortest sequence: %d \n" %
              len(record_min_length))

    def orf_postion_finder(self, dna_seq):
        start_codon = "ATG"
        stop_codons = ["TAA", "TAG", "TGA"]

        pos_dict = {}

        for i in range(3):
            pos = []

            if i == 0:
                frame = [dna_seq[j:j+3] for j in range(i, len(dna_seq), 3)]
            else:
                frame = [dna_seq[:i]] + [dna_seq[j:j+3]
                                         for j in range(i, len(dna_seq), 3)]

            start_pos = []
            stop_pos = []
            try:
                index_start_pos = [m for m, y in enumerate(frame) if
                                   y == start_codon]
                start_pos += index_start_pos
            except ValueError:
                pos.append((-1, 0))
                continue

            for stop_codon in stop_codons:
                try:

                    index_stop_codon = [n for n, x in enumerate(frame) if
                                        x == stop_codon and n > min(start_pos)]
                    stop_pos += index_stop_codon
                except ValueError:
                    continue
            if len(stop_pos) == 0:
                pos.append((-1, 0))
            else:

                while len(start_pos) != 0:
                    start = min(start_pos)
                    try:
                        end = min([stop for stop in stop_pos if stop > start])
                    except ValueError:
                        break

                    s_pos = len("".join(frame[:start])) + 1
                    pos.append((s_pos, (end - start + 1)*3))
                    start_pos.remove(start)
            pos_dict["frame%d" % (i+1)] = pos

        return pos_dict

    # def get_reverse_compliment(self, dna_seq):
    #     pairs = {"A": "T", "C": "G", "G": "C", "T": "A"}
    #     return "".join([pairs[s] for s in dna_seq])[::-1]

    def orf_toolkit(self):

        orf_dict = {}
        for header, dna_seq in self.dict.items():
            pos = self.orf_postion_finder(dna_seq)
            orf_dict[header] = pos

        id_key = [
            key for key in orf_dict if "gi|142022655|gb|EQ086233.1|16" in key]

        idx = id_key[0]

        frame1, frame2, frame3, all_frames, id_frames = [], [], [], [], []
        for key, dict_value in orf_dict.items():
            frame1 += dict_value["frame1"]
            frame2 += dict_value["frame2"]
            frame3 += dict_value["frame3"]
            frames = dict_value["frame1"] + \
                dict_value["frame2"] + dict_value["frame3"]
            all_frames += frames
            if key == idx:
                id_frames = dict_value["frame1"] + \
                    dict_value["frame2"] + dict_value["frame3"]

        print("The start position of longest ORF in frame1: %d \n" %
              max(frame1, key=lambda x: x[1])[0])
        print("The length of longest ORF in frame2: %d \n" %
              max(frame2, key=lambda x: x[1])[1])

        print("The length of longest ORF in frame3: %d \n" %
              max(frame3, key=lambda x: x[1])[0])
        print("The longest ORF of all frames and sequences: %d \n" %
              max(all_frames, key=lambda x: x[1])[1])

        print("The length of longest ORF for ",
              idx, "is: %d \n" % max(id_frames, key=lambda x: x[1])[1])

    '''The functions is used to find all the repeats in a sequence'''

    def _repeats_search(self, dna_seq, n):

        repeats_dict = {}
        for i in range(0, len(dna_seq)):
            repeat = dna_seq[i:i+n]
            if len(repeat) == n:
                if repeat not in repeats_dict:
                    repeats_dict[repeat] = 1
                else:
                    repeats_dict[repeat] = repeats_dict.get(repeat) + 1
        return repeats_dict

    '''The function help asnwering all the questions related to repeats'''

    def repeat_toolkit(self, n):

        repeats_set = {}
        for header, dna_seq in self.dict.items():
            repeats = self._repeats_search(dna_seq, n)

            repeats_set[header] = repeats

        combined_repeats = {}
        for dict_value in repeats_set.values():
            for key in dict_value:
                if key not in combined_repeats:
                    combined_repeats[key] = dict_value[key]
                else:
                    combined_repeats[key] = combined_repeats.get(key) \
                        + dict_value[key]

        # for key in combined_repeats:
        #     print("Repeat %s occures %s times" % (key, combined_repeats[key]))

        most_freq = max(combined_repeats.values())
        print(" \n The most frequent repeat occurs: %d times \n" %
              most_freq)

        most_freq_seq = [key for key in combined_repeats if
                         combined_repeats[key] == max(combined_repeats.values())]
        print("The repeats that occured most frequently: \n",
              most_freq_seq)


if __name__ == "__main__":
    # Load file
    file_name = "../bioproject/data/dna2.fasta"
    toolkit = fasta_file_tools(file_name)
    # Calculate how many records in the file
    toolkit.find_no_of_records()
    # Calcualte the length of the sequences
    # Find the longest or shortest sequence in the file
    # how many longest or shortest sequence
    # Indentifiers of the longest and shortest sequence
    toolkit.find_seq_length_data()

    # indetify all ORFs in a sequence
    # Longest or shortest ORF
    # fidn the sequence with longest ORF
    # Find the longest ORF in a sequence
    # starting postion of tthe ORF in the sequence
    toolkit.orf_toolkit()
    # indentify all repeats of length N
    # idnentify how many times eahc repart occures
    # which is the most frequent repart of given lenth N
    toolkit.repeat_toolkit(7)
    sys.exit(0)
