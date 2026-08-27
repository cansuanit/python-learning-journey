#DNA SEQUENCE ANALYZER
dna_sequence = "   aat gcg tta cgc aa   "
sequence_title = "---  DNA SEQUENCE REPORT  ---"
print (sequence_title.center(50))
#1. Remove leading and trailing whitespaces. 
clean_space= dna_sequence.strip()
#2. Remove spaces within the sequence.
all_space = clean_space.replace(" ","")
#3. Convert all letter  to uppercase.
upper_letter = all_space.upper()
#4. Print the cleaned DNA sequence.
#5. Calculate the total number of nucleotides.
count_nukleotid = len(upper_letter)

#6. Count A, T, G and C seperately.
count_A = upper_letter.count("A")
count_T = upper_letter.count("T")
count_G = upper_letter.count("G")
count_C = upper_letter.count("C")

#7. Calculate the GC percentage.
# (G count + C count) / total sequence lenght * 100
percent_GC = (count_G + count_C)/ count_nukleotid *100

#8. Display the first and last three bases of the sequence.
#9. Display the reserved sequence.
reserved_sequence = upper_letter[::-1]
#10.Print the results as a formatted report.

print("Sequence         :   "+upper_letter)
print("Legth            :   "+str(count_nukleotid))
print("A count          :   "+str(count_A))
print("T count          :   "+str(count_T))
print("G count          :   "+str(count_G))
print("C count          :   "+str(count_C))
print("GC percentage    :   "+str(round(percent_GC,2))+ " % ")
print("First 3 bases    :   "+upper_letter[0:3])
print("Last 3 bases     :   "+upper_letter[-3:])
print("Reserved         :   "+reserved_sequence)