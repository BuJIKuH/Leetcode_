def find_needle(haystack: list):
    while True:
        if 'needle' in haystack:
            index = [i.index('needle') for i in [haystack]]
            return f"found the needle at position {str(index).strip('[]')}"
        else:
            return None

print(find_needle(["hay", "junk", "hay", "hay", "moreJunk", "needle", "randomJunk"]))