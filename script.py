import os
import shutil

from datetime import datetime
from os import path


def generate_log(text):
    global log

    current_date = datetime.now()
    date_str = current_date.strftime('%d/%m/%y %H:%M:%S')

    log.append(f'{date_str} {text}\n')


def log_read(file_name):
    file = open('./logs/' + file_name, 'r')
    print(file.read())


def check_directory():
    generate_log('')
    generate_log('Checking directories ...')

    directories = ['in', 'out', 'bads', 'logs']

    for type in directories:
        check = os.path.exists(type)
        
        if check == False:
            generate_log('')
            generate_log(f'Missing directory {type}!')
            generate_log(f'Creating directory {type} ...')
            
            os.mkdir(f'./{type}')


def analyze_file():
    generate_log(f'')
    generate_log(f'Starting file analysis ...')

    files_dir_in = os.listdir('./in/')
    
    if len(files_dir_in) == 0:
        generate_log(f'There are no files to process ...')
    else:
        generate_log(f'There are {len(files_dir_in)} file(s) to process ...')
        counter = 0

        while counter < len(files_dir_in):
            file_name = files_dir_in[counter]
            result = 0

            generate_log('')
            generate_log('Processing the file ' + file_name)

            with open('./in/' + file_name, 'r') as content:
                text = content.readlines()
                num_line = 0
                
                while num_line < len(text):
                    line = text[num_line].split()
                    
                    for word in line:                
                        
                        if word == 'key':
                            result = result + 1
                    
                    num_line = num_line + 1
            
            if result > 0:
                generate_log('Key found!')
                generate_log('Moving file to out directory ...')

                shutil.move('./in/' + file_name, './out/' + file_name)
            else:
                generate_log('Key not found!')
                generate_log('Moving file to bads directory...')

                shutil.move('./in/' + file_name, './bads/' + file_name)
            
            counter = counter + 1


if __name__ == '__main__':
    error_num = 0
    log = []

    generate_log('=============================================')
    generate_log('===============File Manager==================')
    generate_log('=============================================')
    generate_log('')

    current_date = datetime.now()
    date_str = current_date.strftime('%Y%m%d%H%M%S')
    file_name = "log_" + date_str + ".log"
    log_file = path.join('./logs/', file_name)
    
    generate_log('Starting processing ...')

    try:
        check_directory()
    except Exception as e:
        log.append('Failed to check directory ...')
        log.append(f'Error: {e}')
        error_num += 1

    try:
        analyze_file()
    except Exception as e:
        generate_log('')
        generate_log('Failed to analyze file')
        generate_log(f'Error: {e}')
        error_num += 1

    if error_num == 0:
        generate_log('')
        generate_log('=============================================')
        generate_log('Final Status: SUCCESS')
        generate_log('=============================================')
    else:
        generate_log('')
        generate_log('=============================================')
        generate_log(f'Final Status: ERROR: Were found {error_num} error(s) ...')
        generate_log('=============================================')


    with open(log_file, 'w+') as log_recorder:
        log_recorder.writelines(log)

    log_read(file_name)