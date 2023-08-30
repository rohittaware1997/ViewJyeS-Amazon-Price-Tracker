#!/bin/env python

from crontab import CronTab
import subprocess

output = subprocess.check_output(['pwd'])
output_str = output.decode('utf-8').split('\n')

output_u = subprocess.check_output(['whoami'])
output_user = output_u.decode('utf-8').split('\n')

while True:
    # display menu options
    print("Menu:")
    print("1. Add job")
    print("2. List job")
    print("3. Remove job")
    print("4. Exit")
    
    # get user input
    choice = input("Enter your choice (1-4): ")

    #create / loading the existing cron job 
    cron = CronTab(user=output_user[0])
    cmd = 'python3 ' + output_str[0] + '/asin.py > ' + output_str[0]+'/demo.txt'

    # process user input
    if choice == '1':
        # perform option 1
        job = cron.new(command=cmd)
        job.minute.every(1)

        # write the cron job to the cron tab
        cron.write()
        print('Cron job created')

    elif choice == '2':
        # perform option 2
        # list all cron jobs
            for job in cron:
                print(job)

    elif choice == '3':
        # perform option 3
        # remove a cron job
        job_to_remove = cron.find_command(cmd)
        cron.remove(job_to_remove)
        cron.write()

    elif choice == '4':
        # exit loop
        print("Exiting...")
        break

    else:
        # invalid input
        print("Invalid choice. Please enter a number from 1-4.")