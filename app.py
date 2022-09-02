class GraduationCeremony:
    def __init__(self, total_days):
        if type(total_days) == 'int':
            raise TypeError("Please provide integer values")
        self.total_days = total_days
        self.possible_ways_to_attend = self._possible_ways_to_attend_classes()
    
    def number_of_ways_to_attend_classes(self):
        return len(self.possible_ways_to_attend)

    def probability_to_miss_gradution_ceremony(self):
        impossible_ways = self._impossible_ways_to_attend_classes()
        return len(impossible_ways) / self.number_of_ways_to_attend_classes()

    def _possible_ways_to_attend_classes(self):
        arr = []
        pattern = ""
        self._util(self.total_days, pattern, arr)
        return arr
    
    def _util(self, total_days, pattern, arr):
        if total_days == 0:
            arr.append(pattern)
        else:
            self._util(total_days - 1, pattern + 'A', arr) 
            self._util(total_days - 1, pattern + 'P', arr)    
    def _impossible_ways_to_attend_classes(self):
        return list(filter(lambda way: "AAAA" in way, self.possible_ways_to_attend))

if __name__ == "__main__":
    try:
        total_days = int(input("Enter no of days: "))
        print("total no of days {}".format(total_days))
    except ValueError:
        print("Please provide integer values")
    except Exception as e:
        print(e)
    else:
        class_data = GraduationCeremony(total_days)
        print("Answer: {}/{}".format(class_data.probability_to_miss_gradution_ceremony(), class_data.number_of_ways_to_attend_classes()))