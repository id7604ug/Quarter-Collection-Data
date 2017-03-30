import PyPDF2 as PyPDF


def main():

    # Open pdf files as a binary stream
    quarter_report_file = open('50sqReport.pdf', 'rb')
    # Read pdf files into pypdf
    quarter_report_read = PyPDF.PdfFileReader(quarter_report_file)
    # print(quarter_report_read.getDocumentInfo())
    print(quarter_report_read.getPage(23).extractText())
    with open('page_23.txt', 'w') as write_file:
        text_to_write = str(quarter_report_read.getPage(23).extractText().encode("utf-8"))
        write_file.write(text_to_write)
    # # Open pdf files as a binary stream
    # state_quarters_file = open('50sqReport.pdf', 'rb')
    # # Read pdf files into pypdf
    # state_quarters_read = PyPDF.PdfFileReader(state_quarters_file)
    # # print(state_quarters_read.getDocumentInfo())

    quarter_report_file.close()
    # state_quarters_file.close()

if __name__ == '__main__':
    main()
