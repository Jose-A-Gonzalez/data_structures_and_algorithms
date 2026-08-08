def understand_generators():
    pa = "mo"
    while True:
        yield pa
        pa += "co\n"

def test():

    count = 0
    for i in understand_generators():
        print(i)
        if len(i)>10: 
            break
    

 

def main():
    test()

if __name__ == "__main__":
    main()

