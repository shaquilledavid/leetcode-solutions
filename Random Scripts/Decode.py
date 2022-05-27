def decrypt(word):
  #convert first letter to its value, sub 1
  #next letter convert to value, minus the first letter, then continuously add 26 till in range
  
  message = ''

  dp = [ord(word[0]) - 1] + [0]*len(word[1:])

  i = 1
  while i < len(word):
    initial = ord(word[i]) - dp[i-1] - 1
    print("initial = " + str(ord(word[i])) + " - " + str(dp[i-1]))
    while initial not in range(97, 123):
      initial += 26
    
    dp[i] = initial
    print(initial)
    i += 1

  
  for num in dp:
    message += chr(num) 
  
  return message
