class DisplayLossTable:
    def __init__(self, width=20):
        self.width = width
        if width < 10:
            self.width = 10
        self.divider = '+' + '-' * (width)
        self.last_row = 0

    def display(self, epoch, iter, data):
        print('\x1b[1A' * self.last_row, end='')
        print(self.divider * 2 + '+')
        epoch_info = 'epoch: {}'.format(epoch)
        epoch_info = epoch_info[:self.width]
        print('|{e_info:<{w}}'.format(e_info=epoch_info, w=self.width), end='')
        iter_info = 'iter: {}'.format(iter)
        iter_info = iter_info[:self.width]
        print('|{i_info:<{w}}'.format(i_info=iter_info, w=self.width), end='|\n')
        self.last_row = 3

        if data:
            if type(data) is dict:
                print(self.divider * max(len(data), 2) + '+')
                self._print_loss_info(data)
                self.last_row += 2
            elif type(data) is list:
                data = [line for line in data if line]
                if data:
                    print(self.divider * max(len(data[0]), 2) + '+')
                    data.append(dict())
                    for i, line in enumerate(data[:-1]):
                        column = max(len(line), len(data[i + 1]))
                        self._print_loss_info(line, column)
                        self.last_row += 2
                else:
                    print(self.divider * 2 + '+')
        else:
            print(self.divider * 2 + '+')

    def end(self):
        self.last_row = 0

    def _print_loss_info(self, loss_dict, column=None):
        loss_info_list = []
        for k, v in loss_dict.items():
            loss_num = '{:.4f}'.format(v)
            loss_name = k[:self.width-len(loss_num)-2]
            loss_info = '{}: {}'.format(loss_name, loss_num)[:self.width]
            print('|{l_info:<{w}}'.format(l_info=loss_info, w=self.width), end='')
        print('|')
        if column is None:
            column = len(loss_dict)
        print(self.divider * column, end='+\n')


if __name__ == '__main__':
    print('01234567890123456789')
    t = DisplayLossTable(20)
    #t.display(0, 0, {'1': 1, '2': 2, '3': 3})
    #t.display(0, 0, {'1': 1})
    #t.display(0, 0, [{'1': 1, '2': 2, '3': 3}])
    #t.display(0, 0, [])
    #t.display(0, 0, [{'1': 1}, {'2': 2}])
    #t.display(0, 0, [{'1': 1, '2': 2, '3': 3}, {'1': 1}])
    #t.display(0, 0, [dict(), {'1': 1}])
    #t.display(0, 0, [dict(), dict()])
    #t.display(0, 0, [{'1': 1}, {'1': 1, '2': 2, '3': 3}])
    for i in range(10):
        t.display(0, i, [{'1': i, '2': i, '3': i}, {'4': i, '5': i, '6': i}])
    t.end()
    print('01234567890123456789')
    for i in range(10):
        t.display(0, i, [{'1': i, '2': i, '3': i}, {'4': i, '5': i, '6': i}])
    t.end()
