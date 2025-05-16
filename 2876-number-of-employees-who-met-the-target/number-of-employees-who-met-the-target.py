class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        count = 0
        for employee_hours in hours:
            if employee_hours >= target:
                count += 1
        return count