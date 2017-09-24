import redis, time
conn = redis.Redis()
print('Washer is starating')
dishes = ['salad', 'bread', 'entree', 'dessert']
for dish in dishes:
    time.sleep(1)
    msg = dish.encode('utf-8')
    conn.rpush('dishes', msg)
    print('Washed', dish)
conn.rpush('dishes', 'quit')
print('Washer is done')
