from banner import banner
from pystyle import *
import subprocess

COLOR_CODE = {
    "RESET": "\033[0m",  
    "UNDERLINE": "\033[04m", 
    "GREEN": "\033[32m",     
    "YELLOW": "\033[93m",    
    "RED": "\033[31m",       
    "CYAN": "\033[36m",     
    "BOLD": "\033[01m",        
    "PINK": "\033[95m",
    "URL_L": "\033[36m",       
    "LI_G": "\033[92m",      
    "F_CL": "\033[0m",
    "DARK": "\033[90m",     
}

print(Colorate.Horizontal(Colors.blue_to_white,Center.XCenter(banner)))
select = input(f'{COLOR_CODE["RED"]}[+]{COLOR_CODE["BOLD"]} Выбрать >{COLOR_CODE["RED"]} ')
if select == '100000000':
    from deanon import get_number
    database_file = 'AkumaNumber.csv' 
    search_value = input(f'{COLOR_CODE["YELLOW"]}[@]Введите номер телефона:')
    get_number(database_file, search_value)
elif select == '1':
    subprocess.run(['python', 'ddos.py'])
    input(f"{COLOR_CODE['RED']}[+]{COLOR_CODE['BOLD']} Нажмите Enter, чтобы вернуться в меню...")
    main()
elif select == '3':
    from get_ip import get_ip
    get_ip()
elif select =='4':
    from ddos import dos
    dos()
elif select == '5':
    print('Временно не доступно')
elif select =='6':
    exit
