class Solution(object):
    def angleClock(self, hour, minutes):
        """
        :type hour: int
        :type minutes: int
        :rtype: float
        """
        if abs(minutes * 6 - hour * 30 - 0.5 * minutes)> 180:
        	return 360 - abs(minutes * 6 - hour * 30 - 0.5 * minutes)
    	else:
    		return abs(minutes * 6 - hour * 30 - 0.5 * minutes)

		"""
		return min(abs(minutes * 6 - hour * 30 - 0.5 * minutes), 360-abs(minutes * 6 - hour * 30 - 0.5 * minutes))
		"""