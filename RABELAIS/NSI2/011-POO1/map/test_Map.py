import Map

m = Map.Map("img/yosemite.jpg", 500,300)
m.start()
m.draw()
while m.running:
    m.check()
m.stop()
