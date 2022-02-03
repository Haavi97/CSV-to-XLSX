import csv
import openpyxl
import argh

def csv_to_xlsx(csvfile):
    wb = openpyxl.Workbook()
    ws = wb.active
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader, start=1):
            for c, val in enumerate(row, start=1):
                ws.cell(row=r, column=c).value = val
    wb.save(csvfile[:-4] + '.xlsx')


if __name__ == '__main__':
    csv_to_xlsx('export-address-token-0xd5b0524d734dd7f494c3e326534139129013b86d.csv')