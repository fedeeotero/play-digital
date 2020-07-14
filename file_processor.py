import codecs, sys

input_path = sys.argv[1]
output_path = sys.argv[2]

def processDataEngineers(input_path,output_path):
	i=0
	content = {}

	with codecs.open(input_path, 'rU', 'utf-16-le') as infile:
	    for l in infile:
	    	row = l.split('\t')
	    	
	    	if i==0:
	    		number_fields = len(row)
	    		header = '|'.join(row)
	    		i+=1
	    	else:
	    		row = [e.replace('\n','').strip() for e in row]
	    		if (row[0].isnumeric() and int(row[0]) == i):
	    			key = int(row[0])
	    			values = row[1:]
	    			content[key] = values
	    			i+=1
	       		else:
	    			content[key].extend(row)

	with open(output_path, 'wb') as outfile:
		outfile.write(header.encode('utf8'))
		for k in content:
			if (len(content[k]) + 1) > number_fields:
				content[k] = [e for e in content[k] if e != u'']
			output_row = str(k) + '|' + '|'.join(content[k]) + '\n'
			if  (len(content[k]) + 1) == number_fields:
				outfile.write(output_row.encode('utf8'))

	infile.close()
	outfile.close()

print("Transforming tsv file into csv file...")

try:
	processDataEngineers(input_path,output_path)
	print("Everything finished OK!")

except Exception as ex:
	print("Exception: %s" % ex)