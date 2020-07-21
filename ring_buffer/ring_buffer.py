class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.storage = []
        # keep track of where to insert new items
        self.next_ix = 1

    def append(self, item):
        if len(self.storage) < self.capacity:
            # if storage has fewer than max items
            # just add the item + increment next_ix
            self.storage.append(item)
            self.next_ix = len(self.storage)
        elif len(self.storage) == self.capacity:
            # if storage is at capacity
            # check next_ix
            if self.next_ix == self.capacity:
                # start overwriting the items
                # in the beginning of the queue
                self.storage[0] = item 
                self.next_ix = 1
            elif self.next_ix < self.capacity:
                # overwrite the item at next_ix
                self.storage[self.next_ix] = item
                self.next_ix += 1

    def get(self):
        result = [each for each in self.storage if each is not None]
        return result