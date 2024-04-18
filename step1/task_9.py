# Сделайте так, чтобы число секунд отображалось в виде 
# дни:часы:минуты:секунды.

seconds = int(input('Введите число секунд: '))
days = seconds // (24*60*60)
seconds %= 24*60*60
hours = seconds // (60*60)
seconds %= 60*60
minutes = seconds // 60
seconds %= 60
print(f'{days}:{hours}:{minutes}:{seconds}')

