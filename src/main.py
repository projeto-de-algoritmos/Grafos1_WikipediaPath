from bfs import bfsPath
from dfs import dfs
import wikipediaapi


def choosePages(wiki: wikipediaapi.Wikipedia) -> tuple:
    page1 = wiki.page(input("Page to start search from: "))
    page2 = wiki.page(input("Page to end search at: "))
    return (page1, page2)

def chooseSearch():
    option = input(f"[1] BFS\n[2] DFS\n")
    return option

def main():
    # wiki = wikipediaapi.Wikipedia("pt", proxies={'https' : 'http://172.31.67.201:8888'})
    wiki = wikipediaapi.Wikipedia("pt")
    visited = set()
    path = []
    result = []

    pages = choosePages(wiki)
    option = chooseSearch()


    result = bfsPath(pages[0], pages[1]) if option == '1' else dfs(pages[0], pages[1], visited, path, depth=0, maxDepth=3)
    if result is not None:
        print(" -> ".join(result))
    else:
        print(f"{pages[1].title} not found.")


if __name__ == "__main__":
    main()
