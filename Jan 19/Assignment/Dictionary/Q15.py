'''
15. Write a Python program to print all unique values in a dictionary. Go to
    the editor Sample Data : [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
    {"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]
Expected Output : Unique Values: {'S005', 'S002', 'S007', 'S001', 'S009'}
'''

sample_data = [{"V":"S001"}, {"V": "S002"}, {"VI": "S001"},
{"VI": "S005"}, {"VII":"S005"}, {"V":"S009"},{"VIII":"S007"}]

unique_values = set()
for each in sample_data:
    for val in each.values():
        unique_values.add(val)
print(f"Unique Values :{unique_values}")
