def fav(color):
    color_list = ['blue','orange','green']
    if color in color_list:
        print('this is your favorite color', color)
    else:
        print('sorry')
fav('red')