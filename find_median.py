import statistics
class Container:
    def __init__(self):
        self.values = []

    def add(self, value: int) -> None:
        print(self.values)
        self.values.append(value)

    def delete(self, value: int) -> bool:
        if self.values.count(value) > 0:
            self.values.remove(value)
            return True
        else:
            return False

    def get_median(self) -> int:
        self.values.sort(reverse=False)
        if not self.values == []:
            return self.values[((len(self.values) + 1) // 2) - 1]
            return statistics.median(self.values)
        else:
            raise RuntimeError(f'{self.values} is Empty')

container = Container()
container.add(3)
container.add(2)
container.add(4)
container.add(7)
# container.add(1)
print(container.delete(1))
print(container.delete(2))
print(container.delete(3))
print(container.delete(4))
print(container.delete(7))
# container.add(70)
print(container.get_median())