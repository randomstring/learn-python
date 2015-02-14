#!/usr/bin/python3
# 5) Given a set of n jobs with [start time, end time, cost] find a
# subset so that no 2 jobs overlap and the cost is maximum ?

from random import randint

def gen_random_jobs(jobs, time_range, cost_range):
    """
    input: the number of jobs (int), a time range(int), cost range (int)
    output: list of tuples (start_time, duration, cost)
    """
    return [ [s, s+d if s+d <= time_range else time_range + 1 , c  ] for s,d,c in [ ( randint(0,time_range), randint(1,time_range), randint(1,cost_range) ) for i in range(jobs) ]]

job_list = gen_random_jobs(5, 20, 100)
print("unsorted:", job_list)
job_list.sort(key= lambda x:x[0])
print("sorted:", job_list)

def cost(job_list):
    """
    input: list of job tuples, (start, end, cost)
    output: total cost of the jobs, (return zero if there is overlap?)
    """
    cost = 0
    return cost
