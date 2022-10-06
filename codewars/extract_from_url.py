def domain_name(url):
    return url.split('//')[-1].split('www.')[-1].split('.')[0]


assert domain_name("http://google.com") == "google"
assert domain_name("http://google.co.jp") == "google"
assert domain_name("www.xakep.ru") == "xakep"
assert domain_name("https://youtube.com") == "youtube"
assert domain_name("codewars.com") == "codewars"
assert domain_name("http://www.codewars.com") == "codewars"
