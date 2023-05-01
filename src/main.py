from bfs import bfsPath
from dfs import dfsPath
import wikipediaapi

def choosePages(wiki: wikipediaapi.Wikipedia) -> tuple:
    while True:
        page1 = wiki.page(input('Page to start search from: '))
        page2 = wiki.page(input('Page to end search at: '))
        if not page1.exists():
            print(f'Page "{page1.title}" does not exist.')
            continue
        if not page2.exists():
            print(f'Page "{page2.title}" does not exist.')
            continue
        return (page1, page2)

def chooseSearch():
    print('[1] BFS\n[2] DFS')
    while True:
        option = input()
        if option != '1' and option != '2':
            print('Must be 1 or 2.')
            continue
        return option

def report(result:list):
    print('Distance between pages:', len(result) - 1)
    print('Path:')
    print(*result, sep=' -> ')

def main():
    wiki = wikipediaapi.Wikipedia('pt')

    pages = choosePages(wiki)
    option = chooseSearch()

    print('Finding path...')
    result = bfsPath(pages[0], pages[1]) if option == '1' else dfsPath(pages[0], pages[1], 4)
    
    if result is not None:
        report(result)
    else:
        print(f'{pages[1].title} not found.')

if __name__ == '__main__':
    main()
