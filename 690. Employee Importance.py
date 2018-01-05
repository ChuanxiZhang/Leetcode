"""
# Employee info
class Employee(object):
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""
class Solution(object):
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        start = ""
        for employee in employees:
            if employee.id == id:
                start = employee

        res = 0
        q = collections.deque()
        q.append(start)
        while q:
            cur = q.popleft()
            res += cur.importance
            for sub in cur.subordinates:
                for employee in employees:
                    if sub == employee.id:
                        q.append(employee)
        return res

        
