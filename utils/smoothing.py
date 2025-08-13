    # src/utils/smoothing.py
class EWMA:
    def __init__(self, alpha=0.2, init_val=0.0):
        self.alpha = alpha
        self.value = init_val
        self.initialized = False

    def update(self, x):
        if not self.initialized:
            self.value = x
            self.initialized = True
        else:
            self.value = self.alpha * x + (1 - self.alpha) * self.value
        return self.value