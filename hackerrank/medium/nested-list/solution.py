if __name__ == '__main__':
    records = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        records.append([name, score])
        
    nums = set([record[1] for record in records])
    ordered_nums = sorted(nums)
    second_lowest_grade = ordered_nums[1]
    names = sorted([record[0] for record in records if record[1] == second_lowest_grade])
    for name in names:
        print(name)
    
    
