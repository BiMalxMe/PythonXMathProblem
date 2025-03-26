import random
import time

operators=['+',"-","*"]
min_operand=3
max_operand=12
Total_problems=10


def generate_problem():
    left=random.randint(min_operand,max_operand)
    right=random.randint(min_operand,max_operand)
    operator=random.choice(operators)

    expr=str(left)+ " " +operator+ ' ' +str(right)
    answer=eval(expr)

    return expr,answer


input("Press Enter to start")
print(".........................")
start_time=time.time()

wrong=0
for i in range(Total_problems):
    expr,answer= generate_problem()
    while True:
        guess=input("Problem ."+str(i+1)+" :"+expr+" = ")
        if guess==str(answer):
            break
        wrong+=1

End_time=time.time()
total_time=End_time-start_time
print('------------------------------')
print("You Finished in {} seconds time".format(total_time))
print("You got {} questions wrong ".format(wrong))