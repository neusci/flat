def eagle2(picture):
    ''' double the picture with the Eagle alg.
        stackoverflow.com/questions/17487427/scaling-part-of-a-picture
    '''

    w, h = shape(picture)
    w2, h2 = w*2, h*2
    newPicture = zeros([w2, h2])

    for x in range(1, w-1):
        for y in range(1, h-1):
            x2, y2 = (x-1)*2, (y-1)*2

            # Step 1
            c = picture[x, y]
            newPicture[x2, y2] = c
            newPicture[x2+1, y2] = c
            newPicture[x2, y2+1] = c
            newPicture[x2+1, y2+1] = c

            # Step 2
            if (picture[x-1,y] == picture[x-1,y-1]) and (picture[x-1,y-1] == picture[x,y-1]):
                newPicture[x2,y2] = picture[x-1,y-1]

            if (picture[x,y-1] == picture[x+1,y-1]) and (picture[x+1,y-1] == picture[x+1,y]):
                newPicture[x2+1,y2] = picture[x+1,y-1]

            if (picture[x-1,y] == picture[x-1,y+1]) and (picture[x-1,y+1] == picture[x,y+1]):
                newPicture[x2,y2+1] = picture[x-1,y+1]

            if (picture[x+1,y] == picture[x+1,y+1]) and (picture[x+1,y+1] == picture[x,y+1]):
                newPicture[x2+1,y2+1] = picture[x+1,y+1]

    if w==h:
        np2=newPicture[:w,:h]+newPicture[:w,h:]+newPicture[w:,h:]+newPicture[w:,h:]
        return np2
    else:
        return newPicture


def EnlargeNearestNeighbor(picture, multiplier):
    w1, h1 = shape(picture)
    w2, h2 = w1*multiplier, h1*multiplier
    x_ratio = w1/float(w2)
    y_ratio = h1/float(h2)
    newPicture = zeros([w2, h2])

    for x in range(w2):
        for y in range(h2):
            px = int(floor(x*x_ratio))
            py = int(floor(y*y_ratio))
            newPicture[x, y] = picture[px, py]

    if (w1==h1) and (multiplier==2):
        np2=newPicture[:w1,:h1]+newPicture[:w1,h1:]+newPicture[w1:,h1:]+newPicture[w1:,h1:]
        return np2
    else:
        return newPicture

# pic = EnlargeNearestNeighbor(picture, 2)
