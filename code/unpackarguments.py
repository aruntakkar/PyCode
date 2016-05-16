# Writing a function health_calculator
def health_calculator(age, apples_ate, cigs_smoke):
    answer = (100-age) + (apples_ate * 2) - (cigs_smoke * 2)
    print(answer)

arun_data = [24, 20, 0]

# One approach is passing the parameters one by one
health_calculator(arun_data[0], arun_data[1], arun_data[2])

# Another apporach is unpacking the arguments list approach
health_calculator(*arun_data)
