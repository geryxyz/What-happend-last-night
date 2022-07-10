import argparse


def sleeping(locations: list[str], item: str) -> str:
    sentence = "aludt "
    for location in locations:
        sentence += location + " "
    return sentence + item


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a tale.')
    parser.add_argument('-i', '--items', type=str, nargs='+', required=True,
                        help='the list of things which are sleeping')
    parser.add_argument('-l', '--locations', type=str, nargs='+', required=True,
                        help='the list of locations where are sleeping')
    parser.add_argument('-n', '--name', type=str, required=True,
                        help='the name of the baby')
    args = parser.parse_args()

    print('Mi történt az este?')
    for outer_index in range(1, len(args.locations)):
        print('Hát az úgy volt, hogy ', end='')
        for inner_index in range(outer_index):
            locations = []
            if inner_index > 0:
                locations = args.locations[:inner_index]
            item = args.items[inner_index]
            print(sleeping(locations, item), end='; ')
        print('...')
        print(f'Na jó és {args.name} baba? Á! Ő ébren volt.')
    print('Hát az úgy volt, hogy ', end='')
    print(sleeping(args.locations, args.name + ' baba.'))
