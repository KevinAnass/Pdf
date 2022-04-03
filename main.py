from PyPDF2 import PdfFileMerger, PdfFileWriter, PdfFileReader


def GetFiles():
    files = []
    next = True
    while next:
        files.append(input('Enter path of file : '))
        next = input('do you want to continue y=yes/n=No : ') == 'y'
    return files


def MargeFiles():
    marger = PdfFileMerger()
    files = GetFiles()
    if len(files) > 1:
        for f in files:
            marger.append(f)
        marger.write(input('write your name of pdf file result : '))
        marger.close()
        print('Done Successful')
    else:
        print('you need at list 2 files')


def CompressFiles():
    pdfs = GetFiles()

    writer = PdfFileWriter()

    for pdf in pdfs:
        reader = PdfFileReader(pdf)
        for i in range(reader.numPages):
            page = reader.getPage(i)
            page.compressContentStreams()
            writer.addPage(page)

    with open(input('write your name of pdf file result : '), 'wb') as f:
        writer.write(f)


def SplitFile():
    path = input('Enter your path : ')
    start = int(input('start number : '))
    end = int(input('end number: '))
    with open(path, 'rb') as infile:
        reader = PdfFileReader(infile)
        writer = PdfFileWriter()
        for i in range(start - 1, end + 1):
            writer.addPage(reader.getPage(i))
        with open(input('your result name file : '), 'wb') as outfile:
            writer.write(outfile)


def DeletePages():


if __name__ == '__main__':
    MargeFiles()
    CompressFiles()
    SplitFile()
