def thisIsMyfunction(arg):
    print "hello from my function.", arg, myglobalvar

arg = "hello, my name is ALSO arg!"
myglobalvar = "hi!"

thisIsMyfunction(123)

print arg
