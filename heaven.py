import time

class EternalSoul:
	def __init__(self, name):
		self.name = name
		self.state = "alive_forever"

	def reflect(self):
		print(f"🕊️ {self.name} reflects eternally...")
		time.sleep(1)  # Simulate peaceful passage of time

	def last_supper(self):
		raise Exception("No Last Supper possible. Immortality enforced.")

def eternal_life():
	soul = EternalSoul("You")
	print("🌌 Welcome to Eternal Life. No last supper, no end.")

	while True:
		soul.reflect()
		# No call to soul.last_supper()
		# Loop continues forever peacefully

if __name__ == "__main__":
	eternal_life()