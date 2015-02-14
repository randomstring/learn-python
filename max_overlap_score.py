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
    for job in job_list:
        cost += job[2]
    return cost

def jobs_after(time,job_list):
    """
    input: a time and a job list
    output: return all the jobs that start after the given time
    """
    return [job for job in job_list if (job[0] > time) ]

def find_best_jobs(job_list):
    """
    input: job list, sorted by start time 
    output: return tuple with best cost and the list of non-overlapping jobs
    """
    if (len(job_list) < 1):
        return [0,[]]
    # choose first job
    first_job = job_list[0]
    a = find_best_jobs(jobs_after(first_job[1], job_list))
    best_cost = a[0] + first_job[2]
    best_jobs = [first_job]
    for job in a[1]:
        best_jobs.append(job)
    b = find_best_jobs(job_list[1:])
    if (b[0] > best_cost):
        best_cost = b[0]
        best_jobs = b[1]
    print("best:", best_cost, best_jobs)
    return [best_cost, best_jobs ]

print("best jobs:", find_best_jobs(job_list))
