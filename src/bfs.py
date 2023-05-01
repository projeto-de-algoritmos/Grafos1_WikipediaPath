from collections import deque

def bfs(start_page, end_page) -> list:
    start_page.parent_page = None
    queue = deque([start_page])
    visited = set()
    
    while queue:
        current_page = queue.popleft()
        if current_page.title == end_page.title:
            return current_page
        visited.add(current_page.title)
        err = True
        while err:
            try:
                for link in current_page.links.values():
                    try:
                        if link.title not in visited:
                            link.parent_page = current_page
                            queue.append(link)
                    except KeyError:
                        # print('keyerror')
                        pass
                err = False
            except TimeoutError:
                # print('timeout')
                err = True
    
    return None

def bfsPath(start_page, end_page) -> list:
    end_page_found = bfs(start_page, end_page)
    if end_page_found is not None:
        path = []
        current_page = end_page_found
        while current_page is not None:
            path.insert(0, current_page.title)
            current_page = current_page.parent_page

    return path
