import urllib.parse
import sys
import time
import os

# Список трекинговых параметров (мусор)
TRACKING_PARAMS = {
    'utm_source', 'utm_medium', 'utm_campaign', 'utm_term', 'utm_content',
    'fbclid', 'gclid', 'yclid', 'dclid', 'msclkid', 'twclid',
    'ref', 'source', 'si', 'igshid', 'mc_cid', 'mc_eid'
}

# Цвета для Termux
PINK = '\033[38;5;218m'
GREEN = '\033[38;5;151m'
BLUE = '\033[38;5;153m'
WHITE = '\033[1;37m'
RESET = '\033[0m'
CLEAR = '\033[2J\033[H' # Очистка экрана

def clean_url(url):
    try:
        parsed = urllib.parse.urlparse(url)
        query_params = urllib.parse.parse_qsl(parsed.query)
        clean_params = [(k, v) for k, v in query_params if k not in TRACKING_PARAMS]
        clean_query = urllib.parse.urlencode(clean_params)
        clean_parsed = parsed._replace(query=clean_query)
        final_url = urllib.parse.urlunparse(clean_parsed)
        if final_url.endswith('?'):
            final_url = final_url[:-1]
        return final_url
    except Exception as e:
        return f"Ошибка: {e}"

def show_animation():
    # Анимация покачивающихся цветочков (3 кадра)
    frames = [
        [
            f"{GREEN}       .  ·  .       {RESET}",
            f"{GREEN}      ·  {PINK}✿{GREEN}  ·       {RESET}",
            f"{GREEN}     .    |    .      {RESET}"
        ],
        [
            f"{GREEN}        .  ·  .        {RESET}",
            f"{GREEN}       ·  {PINK}✿{GREEN}  ·        {RESET}",
            f"{GREEN}      .    |    .      {RESET}"
        ],
        [
            f"{GREEN}          .  ·  .      {RESET}",
            f"{GREEN}         ·  {PINK}✿{GREEN}  ·      {RESET}",
            f"{GREEN}        .    |    .    {RESET}"
        ]
    ]
    
    # Прячем курсор
    sys.stdout.write('\033[?25l')
    sys.stdout.flush()
    
    # Проигрываем анимацию 3 секунды
    for _ in range(10):
        for frame in frames:
            sys.stdout.write(CLEAR)
            print_logo()
            print("\n".join(frame))
            time.sleep(0.15)
            
    # Возвращаем курсор
    sys.stdout.write('\033[?25h')
    sys.stdout.flush()

def print_logo():
    logo = f"""
{PINK}  ███████╗ ██████╗ ██╗  ██╗    ██╗      ██████╗  ██████╗ ██████╗  ██████╗ ██████╗ 
  ██╔════╝██╔═══██╗██║ ██╔╝    ██║     ██╔═══██╗██╔════╝ ██╔══██╗██╔═══██╗██╔══██╗
  █████╗  ██║   ██║█████╔╝     ██║     ██║   ██║██║  ███╗██████╔╝██║   ██║██████╔╝
  ██╔══╝  ██║   ██║██╔═██╗     ██║     ██║   ██║██║   ██║██╔═══╝ ██║   ██║██╔═══╝ 
  ██║     ╚██████╔╝██║  ██╗    ███████╗╚██████╔╝╚██████╔╝██║     ╚██████╔╝██║     
  ╚═╝      ╚═════╝ ╚═╝  ╚═╝    ╚══════╝ ╚═════╝  ╚═════╝ ╚═╝      ╚═════╝ ╚═╝     {RESET}
    """
    print(logo)
    print(f"{BLUE}         ~ Твой проводник в мир чистых ссылок ~{RESET}\n")

def show_menu():
    os.system('clear' if os.name == 'posix' else 'cls')
    print_logo()
    
    print(f"{WHITE}  1.{RESET} {GREEN}Инструкция по использованию{RESET}")
    print(f"{WHITE}  2.{RESET} {GREEN}Вставить ссылку (Очистить){RESET}")
    print(f"{WHITE}  3.{RESET} {GREEN}Об авторе{RESET}")
    print(f"{WHITE}  0.{RESET} {PINK}Выход{RESET}")
    print("\n" + "─" * 50)

def show_instructions():
    os.system('clear' if os.name == 'posix' else 'cls')
    print_logo()
    print(f"{WHITE}📖 ИНСТРУКЦИЯ:{RESET}")
    print(f"{GREEN}1.{RESET} Выбери пункт 2 в меню.")
    print(f"{GREEN}2.{RESET} Вставь длинную ссылку (например, из Телеграма).")
    print(f"{GREEN}3.{RESET} Нажми Enter и получи очищенный вариант без мусора.")
    print(f"{GREEN}4.{RESET} Скопируй результат и пользуйся!")
    input(f"\n{BLUE}Нажми Enter, чтобы вернуться в меню...{RESET}")

def show_about():
    os.system('clear' if os.name == 'posix' else 'cls')
    print_logo()
    print(f"{WHITE}👤 ОБ АВТОРЕ:{RESET}")
    print(f"Привет! Меня зовут Тамя (Talopa).")
    print(f"Я создаю полезные и легкие утилиты для Termux.")
    print(f"Мой канал в Telegram: {PINK}@avatatkok{RESET}")
    print(f"\n{GREEN}Подписывайся, там много интересного!{RESET}")
    input(f"\n{BLUE}Нажми Enter, чтобы вернуться в меню...{RESET}")
