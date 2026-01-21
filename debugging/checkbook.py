class Checkbook:
	def __init__(self):
		"""
		Initializes a new instance of the Checkbook class with a balance of 0.0.
		"""
		self.balance = 0.0

	def deposit(self, amount):
		"""
		Deposits the specified amount into the checkbook balance.

		Args:
			amount (float): The amount to deposit.
		"""
		self.balance += amount
		print("Deposited ${:.2f}".format(amount))
		print("Current Balance: ${:.2f}".format(self.balance))

	def withdraw(self, amount):
		"""
		Withdraws the specified amount from the checkbook balance.

		Args:
			amount (float): The amount to withdraw.
		"""
		if amount > self.balance:
			print("Insufficient funds to complete the withdrawal.")
		else:
			self.balance -= amount
			print("Withdrew ${:.2f}".format(amount))
			print("Current Balance: ${:.2f}".format(self.balance))

	def get_balance(self):
		"""
		Prints the current balance of the checkbook.
		"""
		print("Current Balance: ${:.2f}".format(self.balance))

def main():
	"""
	Main function to interact with the Checkbook class.
	"""
	cb = Checkbook()
	while True:
		action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
		if action.lower() == 'exit':
			break
		elif action.lower() == 'deposit':
			try:
				amount = float(input("Enter the amount to deposit: $"))
				cb.deposit(amount)
			except ValueError or TypeError:
				print("Invalid amount. Please enter a valid numeric value.")
		elif action.lower() == 'withdraw':
			try:
				amount = float(input("Enter the amount to withdraw: $"))
				cb.withdraw(amount)
			except ValueError or TypeError:
				print("Invalid amount. Please enter a valid numeric value.")
		elif action.lower() == 'balance':
			cb.get_balance()
		else:
			print("Invalid command. Please try again.")

if __name__ == "__main__":
	main()
