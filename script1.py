from bs4 import BeautifulSoup
import sys

def remove_timeago_td(html_content):
    """Удаляет все <td> с классом timeago из HTML таблицы"""
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Находим все td с классом timeago и удаляем их
    timeago_tds = soup.find_all('td', class_='timeago')
    for td in timeago_tds:
        td.decompose()
    
    return str(soup)

def main():
    if len(sys.argv) != 2:
        print("Использование: python script1.py input.html")
        return
    
    input_file = sys.argv[1]
    output_file = 'output_cleaned.txt'
    
    try:
        # Читаем HTML файл
        with open(input_file, 'r', encoding='utf-8') as f:
            html_content = f.read()
        
        # Обрабатываем HTML
        cleaned_html = remove_timeago_td(html_content)
        
        # Сохраняем результат
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(cleaned_html)
        
        print(f"Файл обработан успешно! Результат сохранен в {output_file}")
        
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()