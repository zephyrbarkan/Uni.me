global question
question = input("Input your qiestion: ")

if "acceptance rate" in question:
    if "Harvard" in question:
        print("Harvard's acceptance rate is 5.9%")
    elif "Berkeley" in question:
        print("Berkeley's acceptance rate is 18.1%")
    elif "Caltech" in question:
        print("Caltech's acceptance rate is 8.8%")
    elif "UCLA" in question:
        print("UCLA's acceptance rate is 17.3%")
    elif "Santa Cruz" in question:
        print("Santa Cruz's accpetnace rate is 48.6%")
    elif "Princeton" in question:
        print("Princeton's acceptance rate is 7.4%")
    elif "Stanford" in question:
        print("Stanford's acceptance rate is 5.1%")
    elif "Columbia" in question:
        print("columbia's acceptace rate is 7%")
    elif "MIT" in question or "Massachusetts Institute of Technology" in question:
        print("MIT's acceptance rate it 7.9%")
    elif "Carnegie Mellon" in question:
        print("Carnegie Mellon's acceptance rate is 24.6%")
    elif "Cal" in question and "Poly" in question:
        print("Cal Poly SLO's acceptance rate is 30.9%")
    elif "Evergreen" in question:
        print("Evergreen's acceptance rate is 98.9%")
    else:
        print("We don't have stats on the college you are asking about")
if "personal essay" in question:
    print("Let's talk about essays")
    if "Stanford" in question:
        print("Stanford likes highly personal essays about growth")
    elif "Harvard" in question:
        print("Harvard likes essays about your direct strengths")
if "cost" in question or "to apply" in question:
    print("Let's talk money")
    if "Mines" in question:
        print("It was free for me to apply")
    elif "UC" in question:
        print("It is 55$  to apply")
    elif "Harvard" in question:
        print("It is 75$  to apply via the common app")
    elif "Caltech" in question:
        print("It is 75$  to apply via the common app")
    elif "Princeton" in question:
        print("It is 75$  to apply via the commmon app")
    elif "Columbia" in question:
        print("It is 85$  to apply")
    elif "MIT" in question or "Massachusetts Institute of Technology" in question:
        print("It is 75$  to apply")
    elif "Carnegie Mellon" in question:
        print("It is 75$  to apply via the commmon app")
    elif "Cal" in question and "Poly" in question:
        print("It is 55$  to apply via the CSUmentor application")
    elif "Evergreen" in question:
        print("It is 55$  to apply")
    else:
        print("We have no data on what you are asking for")
if "tuition" in question:
    print("Lets talk money")
    if "Stanford" in question:
        print("Stanford is about $60,000 annually")
    elif "UC" in question:
        print("UCs are 13,250$ a year")
    elif "Mines" in question:
        print("The annual tuition is 32,700$ for out of state students")
    elif "Harvard" in question:
        print("The annual tuition is 43,938")
    elif "Caltech" in question:
        print("The annual tuition is 43,710")
    elif "Princeton" in question:
        print("The annual tuition is 40,170")
    elif "Columbia" in question:
        print("The annual tuition is 51,008")
    elif "MIT" in question or "Massachusetts Institute of Technology" in question:
        print("The annual tuition is 43,720")
if "fuck" in question:
    print("please do not use such profanity")

