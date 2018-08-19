import csv

query = []
subject = []

with open("resultado.txt") as results:
	for line in results:
		select_ID = line.split()
		query.append('>' + select_ID[0]) # Seleciona o ID do query
		subject.append('>' + select_ID[1]) # Seleciona o ID do subject

subject_cds = []

with open("cds.gma.fasta") as subject_db:
	for lin in subject_db:
		select_db = lin.split()
		subject_cds.append(select_db[0])


query_cds = []

with open("cds.zma.fasta") as query_db:
	for lin in query_db:
		select_q_db = lin.split()
		query_cds.append(select_q_db[0])


seq_pair = []
x = 0
while x < 30: # seleciona os 30 primeiros genes e sequencias
	if query[x] in query_cds:
		#query[x] -> query gene ID
		qseq = query_cds.index(query[x])
		query_seq = query_cds[qseq + 1] # Sequence of this query[x] gene
		seq_pair.append(query[x])
		seq_pair.append(query_seq)
	if subject[x] in subject_cds:
		#subjct[x] -> subject gene ID
		sseq = subject_cds.index(subject[x])
		subseq = subject_cds[sseq + 1] # Sequence of this subject[x] gene
		seq_pair.append(subject[x])
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
