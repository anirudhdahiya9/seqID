import xlrd
import csv
import os

def csv_from_excel(xfilename, cfilename):
    
    print xfilename
   
    if cfilename+'.csv' in os.listdir('.'):
        print '======>>>>processed already'
        return

    wb = xlrd.open_workbook(xfilename)
    sh = wb.sheet_by_name('Sheet1')
    your_csv_file = open(cfilename+'.csv', 'wb')
    wr = csv.writer(your_csv_file, quoting=csv.QUOTE_ALL)

    for rownum in xrange(2, sh.nrows):
        wr.writerow(sh.row_values(rownum))
    your_csv_file.close()

for root, subs, files in os.walk('./ndata/'):
    for f in files:
        if f.endswith('.xlsx'):
            try:
                csv_from_excel(root+'/'+f, '_'.join(root.replace(' ','_').replace('/','_').split('_')[2:]))
            except:
                print '==============================>>>>>>>>>>>>>>some problem in this file'
