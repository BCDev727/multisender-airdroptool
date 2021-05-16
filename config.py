to = []
try:
    txt_file = open("address.txt", "r")
    print('Import addresses from the address.txt...')
    # to = txt_file.readlines()
    to = txt_file.read().splitlines()
    txt_file.close()
    print('Successfully completed: ' + str(len(to)) + ' addresses imported')
except IOError:
    print("Failed: address.txt not accessible!")

private = 'Your account private key'