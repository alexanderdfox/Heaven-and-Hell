import threading
import time
import sys

class ForkbombSoul:
	def __init__(self, name, depth=0):
		self.name = name
		self.depth = depth
		self.alive = True

	def replicate(self):
		print(f"💣 {self.name} at depth {self.depth} replicating...")
		time.sleep(0.1)
		# Spawn two more threads (like forkbomb forks)
		for i in range(2):
			child_name = f"{self.name}.{i}"
			child = ForkbombSoul(child_name, self.depth + 1)
			t = threading.Thread(target=child.replicate, daemon=True)
			t.start()

def chaotic_forkbomb():
	print("⚠️ Starting Forkbomb... System may crash!")
	root = ForkbombSoul("root")
	try:
		root.replicate()
	except Exception as e:
		print(f"🔥 Explosion: {e}")
		sys.exit(1)

if __name__ == "__main__":
	chaotic_forkbomb()
	while True:
		time.sleep(1)  # Keep the main thread alive