money = 500
request = 499
if request > money :
    print 'There is no enough money in your account!'
else :
    while request > 0 :
        if request >= 100 :
            print 'Give 100'
            request -= 100
            money -= 100
        elif request >= 50 :
            print 'Give 50'
            request -= 50
            money -= 50
        elif request >= 10 :
            print 'Give 10'
            request -= 10
            money -= 10
        elif request >= 5 :
            print 'Give 5'
            request -= 5
            money -= 5
        else :
            print 'Give ', request
            request = 0
            money -= request
    print 'You have ', money ,' in your account'

