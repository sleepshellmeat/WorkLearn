from help import Parse


def main():
    start_url = 'http://www.navsource.org/'
    parse = Parse(start_url)
    reponse = parse.get_start_url()


if __name__ == '__main__':
    main()

