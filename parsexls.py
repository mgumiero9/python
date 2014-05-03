import xlrd
from zipfile import ZipFile

datafile = "2013_ERCOT_Hourly_Load_Data.xls"

def open_zip(datafile):
    with ZipFile('{0}.zip'.format(datafile), 'r') as myzip:
        myzip.extractall()


def parse_file(datafile):
    workbook = xlrd.open_workbook(datafile)
    sheet = workbook.sheet_by_index(0)

    ### example on how you can get the data
    sheet_data = [[sheet.cell_value(r, col) for col in range(sheet.ncols)] for r in range(sheet.nrows)]
    #print sheet_data
    ### other useful methods:
    print "\nROWS, COLUMNS, and CELLS:"
    print "Number of rows in the sheet:", 
    print sheet.nrows
    print "Type of data in cell (row 3, col 2):", 
    print sheet.cell_type(3, 2)
    print "Value in cell (row 3, col 2):", 
    print sheet.cell_value(3, 2)
    print "Get a slice of values in column 3, from rows 1-3:"
    print sheet.col_values(3, start_rowx=1, end_rowx=4)

    print "\nDATES:"
    print "Type of data in cell (row 1, col 0):", 
    print sheet.cell_type(1, 0)
    exceltime = sheet.cell_value(1, 0)
    print "Time in Excel format:",
    print exceltime
    print "Convert time to a Python datetime tuple, from the Excel float:",
    print xlrd.xldate_as_tuple(exceltime, 0)
    
    #code here
    
    Vmin=99999999999999
    Vmax=0
    Vavg=0
    Vrowmin=0
    Vrowmax=0
    Vtotal=0
    Vcurrow=0
    
    for item in sheet.col_values(1):
        if item != 'COAST':
            Vtotal += item
            Vcurrow += 1
            print 'vtotal' , Vtotal
            if item < Vmin:
                print 'item' , item,
                Vmin = item
                Vrowmin = Vcurrow
                print 'vmin', Vmin, 'vrowmin' , Vrowmin

            elif item > Vmax:
                print 'item' , item,
                Vmax = item
                Vrowmax = Vcurrow
                print 'vmax' , Vmax, 'vcurrow' , Vcurrow
        else:
            Vcurrow += 1
            print Vcurrow

    
    #code end
    
    data = {
            'maxtime': xlrd.xldate_as_tuple(sheet.cell_value(Vrowmax - 1, 0),0),
            'maxvalue': Vmax,
            'mintime': xlrd.xldate_as_tuple(sheet.cell_value(Vrowmin - 1, 0),0),
            'minvalue': Vmin,
            'avgcoast': Vtotal / (sheet.nrows - 1)
            }
    
    print 'ok' , data
    
    return data
    
def test():
    open_zip(datafile)
    data = parse_file(datafile)

    assert data['maxtime'] == (2013, 8, 13, 17, 0, 0)
    assert round(data['maxvalue'], 10) == round(18779.02551, 10)


test()
