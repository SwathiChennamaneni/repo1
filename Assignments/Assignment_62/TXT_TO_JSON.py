import csv

#jsfile = file('prod.json', 'w')
jsfile = file('output_file.json', 'w')
jsfile.write('[\r\n')
with open('product.txt','r') as f:
    next(f) # skip headings
    reader=csv.reader(f,delimiter='\t')
    row_count = len(list(reader))
    ite = 0
    f.seek(0)
    next(f)
    for name,empid,dept in reader:
        ite+= 1
        jsfile.write('\t{\r\n')
        n = '\t\t\"name\": \"' + name + '\",\r\n'
        i = '\t\t\"empid\": \"' + empid + '\",\r\n'
        d = '\t\t\"department\": \"' + dept + '\"\r\n'
        jsfile.write(n)
        jsfile.write(i)
        jsfile.write(d)
        jsfile.write('\t}')
        if ite < row_count:
            jsfile.write(',\r\n')
        jsfile.write('\r\n')
jsfile.write(']')
jsfile.close()
        
