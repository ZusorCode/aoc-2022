from aocd import lines, submit


class Folder:
    def __init__(self, name: str):
        self.name: str = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def get_child(self, name: str):
        found_children = [child for child in self.children if child.get_name() == name]
        if len(found_children) == 0:
            print(f"Did not find children for {name}")
        return found_children[0]

    def get_size(self):
        curr_size = 0
        for child in self.children:
            curr_size += child.get_size()
        return curr_size

    def get_name(self):
        return self.name

    def resolve_path(self, path: str):
        if path == "root":
            return self

        path_parts = path.split("/")
        if "root" in path_parts:
            path_parts.remove("root")

        if len(path_parts) == 1:
            return self.get_child(path_parts[0])
        else:
            return self.get_child(path_parts[0]).resolve_path("/".join(path_parts[1:]))

    def get_score(self) -> int:
        curr_score = 0
        for child in self.children:
            if isinstance(child, Folder):
                child_size = child.get_size()
                if child_size < 100000:
                    curr_score += child_size
                curr_score += child.get_score()
        return curr_score

    def find_smallest_matching_dir(self, size: int) -> int:
        smallest_fitting = 1000000000000
        for child in self.children:
            if isinstance(child, Folder):
                child_size = child.get_size()
                child_smallest_size = child.find_smallest_matching_dir(size)
                smaller_size = child_size if child_size < child_smallest_size else child_smallest_size
                if size <= smaller_size < smallest_fitting:
                    smallest_fitting = smaller_size

        return smallest_fitting


class File:
    def __init__(self, name: str, size: int):
        self.name: str = name
        self.size: int = size

    def get_size(self):
        return self.size

    def get_name(self):
        return self.name


tree = Folder("root")
current_path = "root"
lines: list[str]
while len(lines) > 0:
    command = lines.pop(0)
    match command.replace("$ ", "").split(" "):
        case ['cd', '/']:
            pass
        case ['cd', '..']:
            current_path = "/".join(current_path.split("/")[:-1])
        case ['ls']:
            for line in lines:
                if not line.startswith("$"):
                    match line.split(" "):
                        case ['dir', dirname]:
                            tree.resolve_path(current_path).add_child(Folder(dirname))
                        case [size, filename]:
                            size = int(size)
                            tree.resolve_path(current_path).add_child(File(filename, size))
                else:
                    break
        case ['cd', directory]:
            current_path += f"/{directory}"

free_space = 70000000 - tree.get_size()
required_to_free = 30000000 - free_space

submit(tree.find_smallest_matching_dir(required_to_free))
