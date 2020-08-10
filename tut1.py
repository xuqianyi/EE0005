try:
    f=open('blocklist.txt')
    print(f.readlines())
    f.close()
except FileNotFoundError:
    print('The file is not found.')
finally:
    print("thank you")
