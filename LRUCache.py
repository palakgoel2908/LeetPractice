"""

	LRU Cache Implementation
	By: Palak Goel
"""

class LRUCache:
    def __init__(self, capacity : int):
        self.cache = {}                 # To Maintain Key, value pair in Cache
        self.cache_freq = {}            # To capture the frequency 
    
    def get(self, key:int) -> int:
        if key in self.cache.keys():
            self.cache_freq[key] = self.cache_freq[key]+1
            print("Value for key {} : {}".format(key,self.cache[key]))
            return self.cache[key]
        else:
		    print("Key {} Not Found".format(key))
            return -1
    
    def checkfrequency(self, key : int):
        key_min = min(self.cache_freq.keys(), key=(lambda k: self.cache_freq[k]))      # to Invalidate the least used key
        print("Key Invalidated : {}".format(key_min))
        self.cache.pop(key_min)                                                        # Invalidate the key
        self.cache_freq.pop(key_min)
        
    def put(self, key: int, value : int)-> None:
        if len(self.cache) < 2:
            if key not in self.cache.keys():
                self.cache[key] = value
                self.cache_freq[key] = 1
                print(" Key Added : {}".format(key))
        else:
            print("=> Need to Invalidate least recent used key as Cache is full for key : {}".format(key))
            self.checkfrequency(key)
            self.cache[key] = value
            self.cache_freq[key] = 1
            print("Key {} Added".format(key))
    
            
def main():
    c = LRUCache(2)
    c.put(2,2)
    c.put(4,4)
    c.get(2)
    c.put(6,6)


main()