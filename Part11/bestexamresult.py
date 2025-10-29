class ExamResult:
    def __init__(self, name: str, grade1: int, grade2: int, grade3: int):
        self.name = name
        self.grade1 = grade1
        self.grade2 = grade2
        self.grade3 = grade3


def best_results(results: list):
    return [max(numb.grade1, numb.grade2, numb.grade3) for numb in results]

        
if __name__ == "__main__":
    result1 = ExamResult("Peter",5,3,4)
    result2 = ExamResult("Pippa",3,4,1)
    result3 = ExamResult("Paul",2,1,3)
    results = [result1, result2, result3]
    print(best_results(results))