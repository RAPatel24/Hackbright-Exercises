#getting the sales report file
log_file = open("um-server-01.txt")

#creating a function for sales_report 
def sales_reports(log_file):
    # go to through each line in the file
    for line in log_file:
        #removing whitespace in the end of string
        line = line.rstrip()
        #initialize variable day with first 4 characters
        day = line[0:3]
        # check if day is Monday we go ahead and print this line
        if day == "Mon":
            print(line)


sales_reports(log_file)
