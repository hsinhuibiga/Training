#Angle Between Hands of a Clock

class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        if hour == 12:
            hour = 0
        hour = hour * 5
        hour += float(minutes) / float(60) * 5
        res =  abs(minutes - hour)/float(60) * 360
        if res > 180:
            res = 360 - res
        return res