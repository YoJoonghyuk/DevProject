from datetime import date


def calculate_age(birthdate):
    today = date.today()
    try:
        birthdate = date.fromisoformat(birthdate)
    except ValueError:
        return "Неверный формат даты рождения. Используйте формат YYYY-MM-DD."
    if birthdate > today:
        return None
    age = (today.year - birthdate.year - ((today.month, today.day)
                                          < (birthdate.month, birthdate.day)))
    return age


if __name__ == "__main__":
    birthdate = input("Введите дату рождения в формате YYYY-MM-DD: ")
    age = calculate_age(birthdate)
    if isinstance(age, int):
        print(f"Ваш возраст: {age} лет")
    else:
        print(age)
