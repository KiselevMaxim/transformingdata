import read

def clear_subdomain(domain):
    if ((domain != "nan") and (type(domain) == str)):
        if domain.count(".") > 1:
            splitted = domain.rsplit(".", maxsplit=2)
            cleared = splitted[1]+"."+splitted[2]
        else:
            cleared = domain
    else:
        cleared = domain
    return(cleared)

data = read.load_data()
data["url"] = data["url"].apply(lambda x: clear_subdomain(x))
domains = data["url"].value_counts(normalize=False, sort=True, ascending=False, bins=None, dropna=True)


domains = domains.head(100)

for name, row in domains.items():
    print("{0}: {1}".format(name, row))