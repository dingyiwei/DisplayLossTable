# Display Loss Table

A tool to display losses in the console when training a model. I prefer a table to display losses rather than a progress bar.

## How to use

1. Create a DisplayLossTable instance.
1. Collect losses and form a table in training.
1. Display losses in every iteration.
1. Call `end()` to terminate a display procedure.

```python
dt = DisplayLossTable(width=20)
for epoch in range(10):
  for iteration in range(100):
    loss1 = compute_loss1(...)
    loss2 = compute_loss2(...)
    loss_data = {'loss1_name': loss1, 'loss2_name': loss2}
    dt.display(epoch, iteration, loss_data)
  val_loss = validate(...)
  print('val: {}'.format(val_loss))
  dt.end()
```

Then the console displays:

```
+--------------------+--------------------+
|epoch: 0            |iter: 99            |
+--------------------+--------------------+
|loss1_name: 0.0396  |loss2_name: 0.2114  |
+--------------------+--------------------+
val: 0.1107722818851471
+--------------------+--------------------+
|epoch: 1            |iter: 99            |
+--------------------+--------------------+
|loss1_name: 0.0847  |loss2_name: 0.3809  |
+--------------------+--------------------+
val: 0.10855870693922043

...

+--------------------+--------------------+
|epoch: 9            |iter: 99            |
+--------------------+--------------------+
|loss1_name: 0.0372  |loss2_name: 0.2032  |
+--------------------+--------------------+
val: 0.1010628417134285
```

The current table refreshes after an iteration.

## Type of loss data

The `display` method receives a `list` or a `dict` as loss data.

### Display a Dict

#### Example 1

```python
...
loss_data = {'a': 1, 'b': 2, 'c': 3}
dt.display(0, 0, loss_data)
...
```

```
+--------------------+--------------------+
|epoch: 0            |iter: 0             |
+--------------------+--------------------+--------------------+
|a: 1.0000           |b: 2.0000           |c: 3.0000           |
+--------------------+--------------------+--------------------+
```

#### Example 2

```python
...
loss_data = {'a': 1}
dt.display(0, 0, loss_data)
...
```

```
+--------------------+--------------------+
|epoch: 0            |iter: 0             |
+--------------------+--------------------+
|a: 1.0000           |
+--------------------+
```

### Display a List

#### Example 1

```python
...
loss_data = [{'a': 1, 'b': 2, 'c': 3}, {'d': 4}]
dt.display(0, 0, loss_data)
...
```

```
+--------------------+--------------------+
|epoch: 0            |iter: 0             |
+--------------------+--------------------+--------------------+
|a: 1.0000           |b: 2.0000           |c: 3.0000           |
+--------------------+--------------------+--------------------+
|d: 4.0000           |
+--------------------+
```

#### Example 2

```python
...
loss_data = [{'a': 1}, {'b': 2, 'c': 3, 'd': 4}]
dt.display(0, 0, loss_data)
...
```

```
+--------------------+--------------------+
|epoch: 0            |iter: 0             |
+--------------------+--------------------+
|a: 1.0000           |
+--------------------+--------------------+--------------------+
|b: 2.0000           |c: 3.0000           |d: 4.0000           |
+--------------------+--------------------+--------------------+
```

## Why need to call `end()` at the end of an epoch

When `display(...)` called, `DisplayLossTable` records how many rows printed this time and print the same number of `\x1b[1A` for the next refreshing. At the end of an epoch, we may have to print some validation information. It `end()` is not called, the information will be print on the first row of the table.

If you do not want to show tables for every epoch, it is unnecessary to call `end()`.