try:
    print 'jeden '
    raise Exception()
    print 'dwa '
except Exception:
    print 'trzy '
else:
    print 'cztery '
finally:
    print 'piec '