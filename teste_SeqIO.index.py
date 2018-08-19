from Bio import SeqIO
import csv

query = []
subject = []

with open("resultado.txt") as results:
	for line in results:
		select_ID = line.split()
		query.append(select_ID[0]) # Seleciona o ID do query
		subject.append(select_ID[1]) # Seleciona o ID do subject

# função para identificar o ID do query e subject
def get_acc(identifier):
	parts = identifier.split()
	return parts[0]
query_dict = SeqIO.index("cds.zma.fasta", "fasta", key_function=get_acc)
subject_dict = SeqIO.index("cds.gma.fasta", "fasta", key_function=get_acc)

seq_pair = []
x = 0
while x < 30: # seleciona os 30 primeiros genes e sequencias
	if query[x] in query_dict:
		#query[x] -> query gene ID
		qseq = query_dict[query[x]]
		query_seq = qseq.seq
		#query_seq = query_dict[qseq + 1] # Sequence of this query[x] gene
		seq_pair.append(">" + query[x])
		seq_pair.append(query_seq)
	if subject[x] in subject_dict:
		#subjct[x] -> subject gene ID
		sseq = subject_dict[subject[x]]
		subseq = sseq.seq 
		#subseq = subject_dict[sseq + 1] # Sequence of this subject[x] gene
		seq_pair.append(">" + subject[x])
		seq_pair.append(subseq)

	# Aqui devo criar o arquivo com as duas sequencias e IDs!
	file = f"./result_pairseq/Seq{x + 1}.fasta"
	with open(file, "w") as output: # abre o arquivo Seq.txt em modo write/edição "w"
		writer = csv.writer(output, lineterminator='\n')
		for val in seq_pair:
			writer.writerow([val])
	# Limpar lista seq_pair - para inserir póximo par de IDs e sequences
	seq_pair.clear()
	x += 1

query_dict.close()
subject_dict.close()
