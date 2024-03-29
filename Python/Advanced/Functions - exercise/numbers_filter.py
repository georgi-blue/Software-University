def even_odd_filter(**kwargs):
    for k,v in kwargs.items():
        if k == "even":
            kwargs[k] = [n for n in v if n % 2 == 0]
        elif k == "odd":
            kwargs[k] = [n for n in v if n % 2 != 0]

    return dict(sorted (kwargs.items(), key=lambda x: -len(x[1])))

print(even_odd_filter(
    odd=[2, 2, 30, 44, 10, 5],
))
