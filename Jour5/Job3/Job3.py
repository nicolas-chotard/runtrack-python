def draw_diagonal(n):

  for i in range(n + 1):

    for j in range(n + 1):
      if i == j:

        print("*", end="")
      else:

        print(" ", end="")

    print()


draw_diagonal(5)