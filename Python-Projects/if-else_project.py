# project question
''' ATM Withdrawal System. '''

available_balance = 10000
withdrawal_amount = 10000

if withdrawal_amount < available_balance:
  print("Withdrawal Successful.")
elif withdrawal_amount > available_balance:
  print("Insufficient Balance.")
elif withdrawal_amount == available_balance:
  print("Your account will be empty.")
# else:
#   print("Enter a valid amount.")

remaining_balance = available_balance - withdrawal_amount
print("Remaining Balance:",remaining_balance)

if remaining_balance >= 500:
  print("Safe balance.")
else:
  print("Warning! Low balance.")


