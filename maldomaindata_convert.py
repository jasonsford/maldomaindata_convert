with open("/home/user/sample-maldomaindata.txt", "r") as domainrepdata:
    lines = domainrepdata.readlines()

with open("/home/user/sample-maldomaindata.txt", "w") as domainrepdata:
    for pos, line in enumerate(lines):
        if pos != 0:
            domainrepdata.write(line)

domainrepdata.close()

with open("/home/user/sample-maldomaindata.txt", "r") as domainrepdata:
    lines = domainrepdata.readlines()

with open("/home/user/sample-maldomaindata.txt", "w") as domainrepdata:
    for line in lines:     
        domain = line.split(',')
        domainrepdata.write("\n" + domain[0])