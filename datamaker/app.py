#!/bin/python

import xlrd
import sys
# Opens the data file gets a list of lists? of strings
def get_data(filepath):
    output = []
    workbook = xlrd.open_workbook(filepath)
    sheet = workbook.sheet_by_index(0)
    num_cols = sheet.ncols   # Number of columns
    for row_idx in range(0,sheet.nrows):    # Iterate through rows
        row = []
        #print ('-'*40)
       # print ('Row: %s' % row_idx)   # Print row number
        for col_idx in range(0, num_cols):  # Iterate through columns
            cell_obj = sheet.cell(row_idx, col_idx)  # Get cell object by row,
            # col
            if cell_obj.ctype is not 0:
                value = ""
                if cell_obj.ctype is 3:
                    #parse the excel date into a pg date
                    dt = xlrd.xldate.xldate_as_datetime(cell_obj.value,0)
                    dtstring = str(dt.year)+"-"+str(dt.month)+"-"+str(dt.day)
                    value = dtstring
                elif cell_obj.ctype == 2:
                    # all numbers are floats make them ints
                    value = str(int(cell_obj.value))
                else:
                    #must be normal string
                    value = str(cell_obj.value)
                    if value == 'Male':
                        value = 'M'
                    if value == 'Female':
                        value = 'F'
                #if len(value) != 0:
                row.append("'"+value+"'")
                #print ('Column: [%s] cell_obj: [%s]' % (col_idx, cell_obj))
        if len(row) != 0:
            output.append(row)
    return output

# takes a data frame
def make_sql(data):
    prefix = "insert into patient(medicalrecordid,givenname,dateofbirth,gender) values"
    # values list of strings
    values = []
    for row in data:
        rowString = "("
        count = 0
        for cell in row:
            if count == len(row)-1:
                #this is the last element
                rowString += cell+")"
                pass
            else:
                rowString += cell+","
            count += 1
        values.append(rowString)
    #print values

    for value in values:
        prefix += value+","
    return prefix

# Entry point
if __name__ == "__main__":
    #TODO use argparse
    filepath  = sys.argv[1]
    result = get_data(filepath)
    sql = make_sql(result)
    print sql+";"



