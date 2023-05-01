def dfsPath(start_page, end_page, maxDepth, depth = 0, visited=set(), path=[]) -> list:
    path.append(start_page.title)
    if start_page.title == end_page.title:
        return path

    visited.add(start_page.title)

    if depth < maxDepth:
        err = True
        while err:
            try:
                for link in start_page.links.values():
                    try:
                        if link.title not in visited:
                            new_path = dfsPath(link, end_page, maxDepth, depth=depth+1, visited=visited, path=path)
                            if new_path is not None:
                                return new_path
                    except KeyError:
                        pass
                err = False
            except TimeoutError:
                # print('timeout')
                err = True

    path.pop()
    return None
