# Solution Link: https://leetcode.com/problems/remove-sub-folders-from-the-filesystem/solutions/6976104/python-graph-and-hashmap-solution-with-j-udaq/


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def parse_path(path):
            return path[1:].split("/")

        def get_folder(names):
            return "/" + "/".join(names)

        # ex) /a/b/c
        # {a: { b: { c: {} :}}}
        # path["#"]: folderならTrue
        tree = {"#": False}
        for f in folder:
            names = parse_path(f)
            n = len(names)
            cur_path = tree
            for i in range(n):
                name = names[i]
                if not (name in cur_path):
                    cur_path[name] = {"#": False}
                cur_path = cur_path[name]

            cur_path["#"] = True

        ans = []

        def dfs(cur_path, names):
            if cur_path["#"]:
                ans.append(get_folder(names))
                return

            for name in cur_path.keys():
                if name == "#":
                    continue
                names.append(name)
                dfs(cur_path[name], names)
                names.pop()

        dfs(tree, [])

        return ans
