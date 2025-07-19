class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        folder.sort()
        ans = [folder[0]]
        
        for f in folder[1:]:
            if not f.startswith(ans[-1] + "/"):
                ans.append(f)
                
        return ans