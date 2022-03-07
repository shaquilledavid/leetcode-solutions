def validIPAddress(queryIP):
        """
        :type queryIP: str
        :rtype: str
        """
        split = queryIP.split('.')
        if len(split) == 1:
            split = queryIP.split(':')
            return validateIPv6(split)
        
        return validateIPv4(split)

def validateIPv4(nums):
    if len(nums) != 4:
        return "Neither"

    for num in nums:
        try:
            int(num)
        except:
            return "Neither"
        
        if num.isalpha() or (len(num) > 1 and num[0] == '0') or int(num) not in range(0, 256):
            return "Neither"

    return "IPv4"

def validateIPv6(nums):
    if len(nums) != 8:
        return "Neither"
    
    for num in nums:
        try:
            hex(int(num, 16))
        except:
            return "Neither"
    
    return "IPv6"
            
