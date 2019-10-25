class Formatter:
    @staticmethod
    def format(sortedList):
        message = "The top 3 scores are:\n"
        for index in range(0, 3):
            message = message + "{}: {}\n".format(sortedList[index].fullname, sortedList[index].score)
        return message