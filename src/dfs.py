def dfs(current_page, end_page, visited, path, maxDepth: int, depth: int = 0) -> list:
    path.append(current_page.title)
    if current_page.title == end_page.title:
        return path

    visited.add(current_page.title)

    if depth < maxDepth:
        err = True
        while err:
            try:
                for link in current_page.links.values():
                    try:
                        if link.title not in visited:
                            new_path = dfs(link, end_page, visited, path, maxDepth, depth + 1)
                            if new_path is not None:
                                return new_path
                    except KeyError:
                        pass
                err = False
            except TimeoutError:
                print("timeout")
                err = True

    path.pop()
    return None
