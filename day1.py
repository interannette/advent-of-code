def count(captcha):
    result = 0
    for i in range(1, len(captcha)):
        j = (i + 1) % len(captcha)
        if captcha[i] == captcha[j]:
            result += int(captcha[i])
    print(result)