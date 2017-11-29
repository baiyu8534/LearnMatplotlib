from random import choice


class RandomWalk():
    '''生成随机漫步数据的类'''

    def __init__(self, num_points=5000):
        self.num_points = num_points

        # 从0,0开始
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        '''计算随机漫步的所有点'''
        while len(self.x_values) < self.num_points:
            # 决定前进方向和这个方向前进的距离
            x_step = self.get_step()

            y_step = self.get_step()

            if x_step == 0 and y_step == 0:
                continue

            # 新点的x和y

            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)

    def get_step(self):
        x_direction = choice([1, -1])
        x_distance = choice(list(range(5)))
        x_step = x_direction * x_distance
        return x_step
