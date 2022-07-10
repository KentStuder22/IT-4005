#NumbStat2
#29 September 2020
#IT 4001, Dale Musser

#Reading integers from a file and doing a series
#of calculations

doCalc = True
while( doCalc ):
    
    #initializing the values
    count = 0
    total = 0
    average = 0
    maximum = 0
    minimum = 0
    numrange = 0
    median = 0
    mode = 0

    try:
        filename = input("What is the name of the file you would like processed: ")

        infile = open(filename, "r")

        unconverted = infile.readlines()

        numlist = []

        for number in unconverted:
            numlist.append(int(number))

        if len(numlist) == 0:
            print("There are no numbers in the file")

        if len(numlist) == 1:
            print("There is only one number in the file")

        if len(numlist) >= 1:

            total = sum(numlist)
            count = len(numlist)
            maximum = max(numlist)
            minimum = min(numlist)

            average = total / count
            numrange = maximum - minimum

            numlist.sort()
        
            if count % 2 == 0:
                number1 = numlist[count//2]
                number2 = numlist[(count//2) - 1]
                median = (number1 + number2) / 2
            else:
                median = numlist[count//2]

            modes = list()
            
            number_counts = {}
            for number in numlist:
                if number in number_counts:
                    number_counts[number] +=1
                else:
                    number_counts[number] = 1

            maxCount = 0
            for number in number_counts:
                count = number_counts[number]
                if( count > maxCount):
                    maxCount = count

            for number in number_counts:
                count = number_counts[number]
                if( count == maxCount):
                    modes.append(number)
            

            infile.close()

    except Exception as err:
        print("An error occured while reading", filename)
        print("The error is", err)

    if len(numlist) >= 1:
        print("Filename: ", filename)
        print("Sum: ", total)
        print("Count: ", count)
        print("Average: ", average)
        print("Maximum: ", maximum)
        print("Minimum: ", minimum)
        print("Range: ", numrange)
        print("Median: ", median)
        print("Mode: ", modes)

    another = input("Would you like to do another set of calculations: (y/n)")
    if another != 'y':
        doCalc = False
            

        
            
    
