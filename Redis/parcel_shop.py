import redis

redis = redis.Redis(
    host='localhost',
    port='6379')

redis.geoadd("parcel_shop", (9.1584836, 48.7226206, 'Reutlingen'))
redis.geoadd("parcel_shop", (9.2004305, 48.5373555, 'Stuttgart '))
redis.geoadd("parcel_shop", (9.1776059, 49.1376432, 'Heilbronn'))
redis.geoadd("parcel_shop", (9.1776059, 49.1376432, 'Freiburg im Breisgau'))
redis.geoadd("parcel_shop",(9.2415192, 48.8096645, 'Karlsruhe'))
redis.geoadd("parcel_shop", (9.1776059, 49.1376432, 'Stuttgart'))
redis.geoadd("parcel_shop", (8.560081, 49.4637092, 'Mannheim'))
redis.geoadd("parcel_shop", (8.560090, 49.4638079, 'heidelberg'))
