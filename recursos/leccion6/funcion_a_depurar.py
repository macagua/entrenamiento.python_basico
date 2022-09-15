import pdb


def calculo(cedula, *args):
    pdb.set_trace()
    if args[0]:
        print(args[0])
    elif args[1]:
        print(args[1])
    print(cedula)


calculo(14522590, 12, 2334)
