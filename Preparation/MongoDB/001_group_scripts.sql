db.***.aggregate([{ "$group": { "_id": { "userid": "$userid", yearMonthDayUTC: 
{ $dateToString: { format: "%Y-%m-%d", date: "$dateCreate" } }}, "count": { "$sum": 1 } } }])
