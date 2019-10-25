import sys
import codevilleFileTools as fileTools
import codevilleSortTools as sortTools
import codevilleFormatTools as formatTools

filename = sys.argv[1]
validator = fileTools.FileValidator
validFile = validator.validateFileExists(filename)

if validFile:
    reader = fileTools.FileReader
    listOfCompetitors = reader.readScoresFile(filename)
    sorter = sortTools.ListSorter
    sortedListOfCompetitors = sorter.sort(listOfCompetitors)
    formatter = formatTools.Formatter
    output = formatter.format(sortedListOfCompetitors)
    print(output)
else:
    print("File does not exist")
