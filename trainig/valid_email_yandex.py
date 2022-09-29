def checking_email(email: str) -> str:
    current_email = email.lower()
    check_point = '@ya.'
    check_point2 = '@ya-'
    if check_point in current_email:
        cur = current_email.replace('@ya', '@yandex')
        return cur
    if check_point2 in current_email:
        cur = current_email.replace('@ya', '@yandex')
        return cur
    return current_email


assert checking_email('Yandex@Ya.ru') == 'yandex@yandex.ru'
assert checking_email('Yandex@Ya-team.ru') == 'yandex@yandex-team.ru'
assert checking_email('ULIaM@Yandex.ru') == 'uliam@yandex.ru'
