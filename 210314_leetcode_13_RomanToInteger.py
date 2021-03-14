# leetcode 13. Roman to Integer
class Solution:
    def romanToInt(self, s: str) -> int:
        
        status = 0
        s = list(s)
        visit = [0] * len(s)

        for i in range(len(s)):
            
            if visit[i] == 0:
            
                if s[i] == 'I':
                    visit[i] = 1
                    if i != len(s) - 1:
                        if s[i+1] == 'V':
                            status += 4
                            visit[i+1] = 1
                            continue
                        elif s[i+1] == 'X':
                            status += 9
                            visit[i+1] = 1
                            continue
                    status += 1

                if s[i] == 'V':
                    visit[i] = 1
                    status += 5

                if s[i] == 'X':
                    visit[i] = 1
                    if i != len(s) - 1:
                        if s[i+1] == 'L':
                            status += 40
                            visit[i+1] = 1
                            continue
                        elif s[i+1] == 'C':
                            status += 90
                            visit[i+1] = 1
                            continue
                    status += 10

                if s[i] == 'L':
                    visit[i] = 1
                    status += 50

                if s[i] == 'C':
                    visit[i] = 1
                    if i != len(s) - 1:
                        if s[i+1] == 'D':
                            status += 400
                            visit[i+1] = 1
                            continue
                        elif s[i+1] == 'M':
                            status += 900
                            visit[i+1] = 1
                            continue
                    status += 100

                if s[i] == 'D':
                    visit[i] = 1
                    status += 500

                if s[i] == 'M':
                    visit[i] = 1
                    status += 1000
            
        return status             
                