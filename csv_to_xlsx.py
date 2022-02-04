import os
import csv
import openpyxl
import argh

from tqdm import tqdm


def csv_to_xlsx(csvfile):
    wb = openpyxl.Workbook()
    ws = wb.active
    with open(csvfile, 'r') as f:
        reader = csv.reader(f)
        for r, row in enumerate(reader, start=1):
            for c, val in enumerate(row, start=1):
                ws.cell(row=r, column=c).value = val
    wb.save(csvfile[:-4] + '.xlsx')


def all(file='file_name or file_path'):
    """
    Converts all csv files in the folder. 
    """
    _csvs = tqdm(list_csv())
    for _csv in _csvs:
        _csvs.set_description('Converting: {:<20}'.format(_csv))
        csv_to_xlsx(_csv)


def file(file):
    """Converts the given file"""
    if valid_csv(file):
        csv_to_xlsx(file)


def show():
    """Prints all the names of the csv files in the folder"""
    print('csv files in the folder')
    print('\n'.join(list_csv()))


def list_csv():
    return filter(lambda x: valid_csv(x), os.listdir())


def valid_csv(s):
    return s.split('.')[-1] == 'csv'


parser = argh.ArghParser()
parser.add_commands([all, show, file])

if __name__ == '__main__':
    parser.dispatch()
    # argh.dispatch_command(main)
